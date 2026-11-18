#!/usr/bin/env python3
"""Validate the multivitamin review datasets and regenerate every derived table.

The CSV files in ``data/`` are the source of truth. This script checks their
schema, cross-references and arithmetic, computes cost and upper-limit metrics,
and renders the Markdown tables used by the report and documentation.

Usage
-----
    python analysis/build_tables.py           # validate and regenerate
    python analysis/build_tables.py --check   # validate; fail if outputs are stale

Only the Python standard library is required (Python 3.10+).
"""

from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path
from statistics import median

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
GEN = ROOT / "docs" / "generated"

# --------------------------------------------------------------------------
# Schema
# --------------------------------------------------------------------------

REFERENCE_COLUMNS = ["id", "authors", "year", "title", "journal", "identifier", "url", "type"]
EVIDENCE_COLUMNS = [
    "id", "domain", "question", "outcome", "population", "evidence_type",
    "studies_participants", "pooled_effect", "effect_measure", "ci",
    "certainty", "status", "source_ids", "notes",
]
CLAIM_COLUMNS = ["id", "claim", "category", "verdict", "explanation", "source_ids"]
PRODUCT_COLUMNS = [
    "id", "brand", "product", "target", "format", "serving_units_per_day",
    "servings_per_container", "price_usd", "price_channel", "price_date",
    "price_verified", "certification",
]
INGREDIENT_COLUMNS = [
    "id", "nutrient", "form", "form_class", "bioavailability",
    "absorption_notes", "adult_ul", "ul_unit", "typical_mvm_dose",
    "evidence_quality", "notes", "source_ids",
]
UL_COLUMNS = ["nutrient", "ul_adult", "unit", "basis", "critical_effect", "notes", "source_ids"]
INTERACTION_COLUMNS = [
    "id", "interacting_pair", "mechanism", "clinical_effect", "severity",
    "management", "source_ids",
]

# (column, label, unit, ul_key)
NUTRIENTS = [
    ("vitamin_a_ug", "Vitamin A", "mcg", "Vitamin A (preformed)"),
    ("vitamin_c_mg", "Vitamin C", "mg", "Vitamin C"),
    ("vitamin_d_ug", "Vitamin D", "mcg", "Vitamin D"),
    ("vitamin_e_mg", "Vitamin E", "mg", "Vitamin E"),
    ("vitamin_k_ug", "Vitamin K", "mcg", "Vitamin K"),
    ("thiamin_mg", "Thiamin", "mg", "Thiamin"),
    ("riboflavin_mg", "Riboflavin", "mg", "Riboflavin"),
    ("niacin_mg", "Niacin", "mg", "Niacin (synthetic)"),
    ("vitamin_b6_mg", "Vitamin B6", "mg", "Vitamin B6"),
    ("folate_ug_dfe", "Folate", "mcg DFE", None),
    ("vitamin_b12_ug", "Vitamin B12", "mcg", "Vitamin B12"),
    ("biotin_ug", "Biotin", "mcg", "Biotin"),
    ("pantothenic_mg", "Pantothenic acid", "mg", "Pantothenic acid"),
    ("calcium_mg", "Calcium", "mg", "Calcium"),
    ("iron_mg", "Iron", "mg", "Iron"),
    ("iodine_ug", "Iodine", "mcg", "Iodine"),
    ("magnesium_mg", "Magnesium", "mg", "Magnesium"),
    ("zinc_mg", "Zinc", "mg", "Zinc"),
    ("selenium_ug", "Selenium", "mcg", "Selenium"),
    ("copper_mg", "Copper", "mg", "Copper"),
    ("manganese_mg", "Manganese", "mg", "Manganese"),
    ("chromium_ug", "Chromium", "mcg", "Chromium"),
    ("molybdenum_ug", "Molybdenum", "mcg", "Molybdenum"),
]

PRODUCT_FIELDS = [n[0] for n in NUTRIENTS]
TARGETS = {"general adult", "men", "women", "50+", "men 50+", "women 50+"}
FORMATS = {"tablet", "capsule", "gummy", "powder", "softgel"}
CERTAINTY = {"High", "Moderate", "Low", "Very low", "Not graded"}
STATUS = {"Established", "Emerging", "Mixed", "Unsupported"}
VERDICTS = {"Supported", "Partially supported", "Unsupported", "False"}
SEVERITY = {"High", "Moderate", "Low"}
BIOAVAILABILITY = {"High", "Moderate", "Low-moderate", "Low", "Variable"}
EVIDENCE_QUALITY = {"High", "Moderate", "Low"}


class ValidationError(Exception):
    pass


def fail(message: str) -> None:
    raise ValidationError(message)


def load(name: str, columns: list[str]) -> list[dict[str, str]]:
    path = DATA / name
    if not path.exists():
        fail(f"missing dataset: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        header = reader.fieldnames or []
        missing = [c for c in columns if c not in header]
        if missing:
            fail(f"{name}: missing columns {missing}")
        rows = list(reader)
    if not rows:
        fail(f"{name}: no data rows")
    return rows


def num(value: str, field: str, row_id: str) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        fail(f"{row_id}: {field} is not numeric ({value!r})")


def money(value: float) -> str:
    return f"${value:,.2f}"


def pct(value: float) -> str:
    return f"{value * 100:,.0f}%"


def md_table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |",
           "| " + " | ".join("---" for _ in headers) + " |"]
    for row in rows:
        out.append("| " + " | ".join(str(cell).replace("|", "/") for cell in row) + " |")
    return "\n".join(out)


def ref_ids(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


# --------------------------------------------------------------------------
# Load and validate
# --------------------------------------------------------------------------

def load_all() -> dict[str, list[dict[str, str]]]:
    refs = load("references.csv", REFERENCE_COLUMNS)
    evidence = load("evidence.csv", EVIDENCE_COLUMNS)
    claims = load("claims.csv", CLAIM_COLUMNS)
    products = load("products.csv", PRODUCT_COLUMNS + PRODUCT_FIELDS)
    ingredients = load("ingredients.csv", INGREDIENT_COLUMNS)
    ul_rows = load("upper_limits.csv", UL_COLUMNS)
    interactions = load("interactions.csv", INTERACTION_COLUMNS)

    for name, rows in [
        ("references", refs), ("evidence", evidence), ("claims", claims),
        ("products", products), ("ingredients", ingredients),
        ("interactions", interactions),
    ]:
        seen = set()
        for row in rows:
            rid = row.get("id", "")
            if not rid:
                fail(f"{name}: row with empty id")
            if rid in seen:
                fail(f"{name}: duplicate id {rid}")
            seen.add(rid)

    ref_index = {r["id"]: r for r in refs}
    if len(ref_index) != len(refs):
        fail("references: duplicate ids")

    for row in evidence:
        if row["certainty"] not in CERTAINTY:
            fail(f"evidence {row['id']}: bad certainty {row['certainty']!r}")
        if row["status"] not in STATUS:
            fail(f"evidence {row['id']}: bad status {row['status']!r}")
        for rid in ref_ids(row["source_ids"]):
            if rid not in ref_index:
                fail(f"evidence {row['id']}: unknown reference {rid}")

    for row in claims:
        if row["verdict"] not in VERDICTS:
            fail(f"claims {row['id']}: bad verdict {row['verdict']!r}")
        for rid in ref_ids(row["source_ids"]):
            if rid not in ref_index:
                fail(f"claims {row['id']}: unknown reference {rid}")

    for row in ingredients:
        if row["bioavailability"] not in BIOAVAILABILITY:
            fail(f"ingredients {row['id']}: bad bioavailability {row['bioavailability']!r}")
        if row["evidence_quality"] not in EVIDENCE_QUALITY:
            fail(f"ingredients {row['id']}: bad evidence_quality {row['evidence_quality']!r}")
        for rid in ref_ids(row["source_ids"]):
            if rid not in ref_index:
                fail(f"ingredients {row['id']}: unknown reference {rid}")

    for row in interactions:
        if row["severity"] not in SEVERITY:
            fail(f"interactions {row['id']}: bad severity {row['severity']!r}")
        for rid in ref_ids(row["source_ids"]):
            if rid not in ref_index:
                fail(f"interactions {row['id']}: unknown reference {rid}")

    for row in ul_rows:
        for rid in ref_ids(row["source_ids"]):
            if rid not in ref_index:
                fail(f"upper_limits {row['nutrient']}: unknown reference {rid}")

    # Products: numeric and arithmetic sanity.
    nutrient_columns = PRODUCT_FIELDS + [
        "serving_units_per_day", "servings_per_container", "price_usd"
    ]
    for row in products:
        rid = row["id"]
        if row["target"] not in TARGETS:
            fail(f"products {rid}: bad target {row['target']!r}")
        if row["format"] not in FORMATS:
            fail(f"products {rid}: bad format {row['format']!r}")
        if row["price_verified"] not in {"yes", "no"}:
            fail(f"products {rid}: bad price_verified {row['price_verified']!r}")
        for col in nutrient_columns:
            value = num(row[col], col, rid)
            if value < 0:
                fail(f"products {rid}: negative {col}")
        price = num(row["price_usd"], "price_usd", rid)
        servings = num(row["servings_per_container"], "servings_per_container", rid)
        units = num(row["serving_units_per_day"], "serving_units_per_day", rid)
        if not 1 <= units <= 6:
            fail(f"products {rid}: implausible serving_units_per_day {units}")
        if not 5 <= servings <= 2000:
            fail(f"products {rid}: implausible servings_per_container {servings}")
        if not 1 <= price <= 500:
            fail(f"products {rid}: implausible price {price}")
        cost = price / servings
        if not 0.01 <= cost <= 10:
            fail(f"products {rid}: implausible cost per serving {cost:.2f}")
        if num(row["vitamin_d_ug"], "vitamin_d_ug", rid) > 250:
            fail(f"products {rid}: vitamin D above 10,000 IU; check units")

    if not any(r["type"] == "RCT" for r in refs):
        fail("references: no RCTs recorded")

    return {
        "refs": refs, "evidence": evidence, "claims": claims,
        "products": products, "ingredients": ingredients,
        "ul": ul_rows, "interactions": interactions,
    }


# --------------------------------------------------------------------------
# Metrics
# --------------------------------------------------------------------------

def ul_index(rows: list[dict[str, str]]) -> dict[str, tuple[float, str, str]]:
    index = {}
    for row in rows:
        if row["ul_adult"] in {"None", "", "none"}:
            continue
        index[row["nutrient"]] = (
            float(row["ul_adult"]), row["unit"], row["critical_effect"]
        )
    return index


def metrics(product: dict[str, str], uls: dict[str, tuple[float, str, str]]) -> dict:
    servings = float(product["servings_per_container"])
    cost = float(product["price_usd"]) / servings
    vit_d = float(product["vitamin_d_ug"])
    shares = {}
    for column, label, _unit, ul_key in NUTRIENTS:
        if not ul_key or ul_key not in uls:
            continue
        amount = float(product[column])
        if amount <= 0:
            continue
        shares[label] = amount / uls[ul_key][0]
    driver = max(shares, key=shares.get) if shares else ""
    return {
        "cost": cost,
        "cost_year": cost * 365,
        "cost_per_25ug_d": (cost / (vit_d / 25)) if vit_d > 0 else None,
        "max_share": shares[driver] if driver else 0.0,
        "driver": driver,
        "shares": shares,
        "declared": sum(1 for c in PRODUCT_FIELDS if float(product[c]) > 0),
    }


def flags(product: dict[str, str]) -> list[str]:
    out = []
    d = float(product["vitamin_d_ug"])
    zinc = float(product["zinc_mg"])
    copper = float(product["copper_mg"])
    b6 = float(product["vitamin_b6_mg"])
    niacin = float(product["niacin_mg"])
    vit_a = float(product["vitamin_a_ug"])
    iron = float(product["iron_mg"])

    if d == 0:
        out.append("no vitamin D declared")
    elif d < 25:
        out.append("vitamin D below 1,000 IU")
    if zinc >= 25:
        out.append("zinc 25 mg or more")
    if zinc >= 15 and copper == 0:
        out.append("zinc 15 mg+ without copper")
    if b6 >= 50:
        out.append("vitamin B6 50 mg or more")
    if niacin > 35:
        out.append("niacin above the UL")
    if vit_a >= 1500:
        out.append("vitamin A 1,500 mcg or more")
    if iron > 0 and product["target"] in {"men", "men 50+", "50+"}:
        out.append("iron in a men's or 50+ formula")
    if float(product["serving_units_per_day"]) >= 3:
        out.append("3+ units per serving")
    return out


# --------------------------------------------------------------------------
# Renderers
# --------------------------------------------------------------------------

def render_products(data, uls) -> str:
    products = sorted(data["products"], key=lambda p: (float(p["price_usd"]) / float(p["servings_per_container"]), p["brand"]))
    lines = ["# Product comparison", "",
             "Generated from `data/products.csv`. Prices are US retail snapshots from "
             "November 2026 and will change. `Cost per year` is a 365-day projection at "
             "the same price.", "",
             "`Max UL share` is the largest declared amount of any nutrient with an "
             "established adult upper limit, as a fraction of that limit. Vitamin A is "
             "counted as if it were all preformed, so formulas that use beta-carotene are "
             "overstated. Folate is excluded because DFE and folic acid are not "
             "interchangeable against the 1,000 mcg folic acid UL.", ""]

    rows = []
    for p in products:
        m = metrics(p, uls)
        rows.append([
            f"{p['brand']} {p['product']}", p["target"], p["format"],
            p["serving_units_per_day"], money(m["cost"]), money(m["cost_year"]),
            p["certification"], pct(m["max_share"]),
        ])
    lines.append(md_table(
        ["Product", "Target", "Format", "Units/day", "Cost/serving", "Cost/year", "Certification", "Max UL share"],
        rows,
    ))
    lines.append("")

    lines += ["## Cost by format", "",
              "Median cost per daily serving, with the range across the sampled products.", ""]
    by_format = {}
    for p in products:
        m = metrics(p, uls)
        by_format.setdefault(p["format"], []).append(m["cost"])
    rows = []
    for fmt in sorted(by_format):
        costs = by_format[fmt]
        rows.append([fmt, len(costs), money(median(costs)), money(min(costs)), money(max(costs))])
    lines.append(md_table(["Format", "Products", "Median", "Minimum", "Maximum"], rows))
    lines.append("")

    lines += ["## Cost by target group", ""]
    by_target = {}
    for p in products:
        m = metrics(p, uls)
        by_target.setdefault(p["target"], []).append(m["cost"])
    rows = [[t, len(c), money(median(c)), money(min(c)), money(max(c))]
            for t, c in sorted(by_target.items())]
    lines.append(md_table(["Target", "Products", "Median", "Minimum", "Maximum"], rows))
    lines.append("")

    lines += ["## Certification", "",
              "Organic and Non-GMO seals are excluded: they certify production method, "
              "not content or purity.", ""]
    certified = [p for p in products if p["certification"] not in {"None documented", "USDA Organic"}]
    rows = []
    for label, group in [("Third-party certified", certified),
                         ("No certification documented", [p for p in products if p not in certified])]:
        costs = [metrics(p, uls)["cost"] for p in group]
        rows.append([label, len(group), money(median(costs)) if costs else "n/a"])
    lines.append(md_table(["Group", "Products", "Median cost/serving"], rows))
    lines.append("")

    lines += ["## Key nutrient doses", "",
              "Only the nutrients that most often differentiate formulas. A blank cell "
              "means the label does not declare it.", ""]
    rows = []
    for p in products:
        def cell(field):
            value = float(p[field])
            return "" if value == 0 else f"{value:g}"
        rows.append([
            f"{p['brand']} {p['product']}", cell("vitamin_d_ug"), cell("vitamin_b12_ug"),
            cell("iron_mg"), cell("zinc_mg"), cell("vitamin_b6_mg"),
            cell("niacin_mg"), p["folate_form"], p["has_k2"],
        ])
    lines.append(md_table(
        ["Product", "D mcg", "B12 mcg", "Iron mg", "Zinc mg", "B6 mg", "Niacin mg", "Folate form", "K2"],
        rows,
    ))
    lines.append("")

    lines += ["## Value benchmark: cost per 25 mcg (1,000 IU) of vitamin D", "",
              "A normaliser, not a claim that vitamin D is the only nutrient that matters. "
              "Products that do not declare vitamin D are omitted.", ""]
    rows = []
    for p in products:
        m = metrics(p, uls)
        if m["cost_per_25ug_d"] is None:
            continue
        rows.append([f"{p['brand']} {p['product']}", f"{float(p['vitamin_d_ug']):g}",
                     money(m["cost"]), money(m["cost_per_25ug_d"])])
    rows.sort(key=lambda r: float(r[3].replace("$", "").replace(",", "")))
    lines.append(md_table(["Product", "D mcg", "Cost/serving", "Cost per 25 mcg D"], rows))
    lines.append("")

    lines += ["## Formulation red flags", "",
              "Mechanical checks against the upper limits in `data/upper_limits.csv` "
              "and against label design. A flag is not proof of harm; it is a reason to "
              "look at the label.", ""]
    rows = []
    for p in products:
        f = flags(p)
        rows.append([f"{p['brand']} {p['product']}", "; ".join(f) if f else "none"])
    lines.append(md_table(["Product", "Flags"], rows))
    lines.append("")
    return "\n".join(lines)


def render_ul_check(data, uls) -> str:
    products = sorted(data["products"], key=lambda p: (-metrics(p, uls)["max_share"], p["brand"]))
    lines = ["# Upper-limit check", "",
             "Each product's declared nutrients are compared with the adult tolerable "
             "upper intake levels in `data/upper_limits.csv`. Vitamin A is treated as "
             "preformed (worst case). Folate is excluded because dietary folate "
             "equivalents cannot be compared directly with the folic acid UL.", "",
             "This is a label arithmetic exercise. It does not account for food, other "
             "supplements, or individual absorption.", ""]
    rows = []
    for p in products:
        m = metrics(p, uls)
        over = [f"{k} {pct(v)}" for k, v in m["shares"].items() if v >= 1.0]
        near = [f"{k} {pct(v)}" for k, v in m["shares"].items() if 0.8 <= v < 1.0]
        rows.append([
            f"{p['brand']} {p['product']}", pct(m["max_share"]), m["driver"] or "n/a",
            "; ".join(over) if over else "none",
            "; ".join(near) if near else "none",
        ])
    lines.append(md_table(
        ["Product", "Max UL share", "Driver", "At or above UL", "80-99% of UL"], rows))
    lines.append("")

    lines += ["## Nutrients with no adult UL", "",
              "Absence of a UL is not a guarantee of safety; it means the data were "
              "insufficient to set one. Vitamin K, B12, biotin, pantothenic acid and "
              "chromium fall in this category.", ""]

    lines += ["## Where the UL itself is contested", "",
              "- **Niacin.** The 35 mg UL applies to synthetic nicotinic acid and "
              "niacinamide. Flushing is the acute effect; hepatotoxicity appears at gram "
              "doses. Several high-potency multis supply 50-80 mg.",
              "- **Vitamin B6.** The 100 mg UL is based on sensory neuropathy. Cases have "
              "been reported below it with long-term use, so 50-75 mg in a daily multi is "
              "not trivial.",
              "- **Vitamin A.** The 3,000 mcg UL applies to preformed retinol. Beta-carotene "
              "is not covered, but high-dose beta-carotene has its own risk in smokers.",
              "- **Zinc.** The 40 mg UL is about copper balance as much as zinc toxicity. "
              "A 25 mg zinc multi without copper is a design flaw, not an overdose.",
              "- **Magnesium.** The 350 mg UL applies to supplemental magnesium only. Food "
              "magnesium is not restricted.", ""]
    return "\n".join(lines)


def render_ingredients(data) -> str:
    lines = ["# Ingredient forms", "",
             "Generated from `data/ingredients.csv`. Bioavailability ratings summarise "
             "human data; they are not percentages unless stated. `Evidence quality` "
             "refers to confidence in the comparison, not in a health benefit.", ""]
    by_nutrient: dict[str, list[dict[str, str]]] = {}
    for row in data["ingredients"]:
        by_nutrient.setdefault(row["nutrient"], []).append(row)
    for nutrient in by_nutrient:
        lines += [f"## {nutrient}", ""]
        rows = []
        for row in by_nutrient[nutrient]:
            ul = row["adult_ul"]
            if ul not in {"None", ""}:
                ul = f"{ul} {row['ul_unit']}"
            else:
                ul = "none established"
            rows.append([row["form"], row["form_class"], row["bioavailability"],
                         ul, row["typical_mvm_dose"], row["notes"]])
        lines.append(md_table(
            ["Form", "Class", "Bioavailability", "Adult UL", "Typical multi dose", "Notes"], rows))
        lines.append("")
    return "\n".join(lines)


def render_evidence(data) -> str:
    lines = ["# Evidence tables", "",
             "Generated from `data/evidence.csv`. Effect estimates are as reported by the "
             "cited source; `CI` is the 95% interval unless the source states otherwise. "
             "Certainty uses GRADE logic and is separate from clinical importance.", ""]
    by_domain: dict[str, list[dict[str, str]]] = {}
    for row in data["evidence"]:
        by_domain.setdefault(row["domain"], []).append(row)
    for domain in by_domain:
        lines += [f"## {domain}", ""]
        rows = []
        for row in by_domain[domain]:
            effect = row["pooled_effect"]
            if row["ci"]:
                effect = f"{effect} ({row['ci']})"
            rows.append([row["id"], row["question"], effect, row["certainty"], row["status"]])
        lines.append(md_table(["ID", "Question", "Result", "Certainty", "Status"], rows))
        lines.append("")
        lines += ["Interpretation:", ""]
        for row in by_domain[domain]:
            lines.append(f"- **{row['id']}** — {row['notes']}")
        lines.append("")
    return "\n".join(lines)


def render_claims(data) -> str:
    lines = ["# Claim adjudication", "",
             "Generated from `data/claims.csv`. `Partially supported` means the claim is "
             "true in a specific population, dose or setting but false as a general "
             "statement.", ""]
    order = ["Supported", "Partially supported", "Unsupported", "False"]
    counts = {v: sum(1 for c in data["claims"] if c["verdict"] == v) for v in order}
    lines.append(md_table(["Verdict", "Claims"], [[v, counts[v]] for v in order]))
    lines.append("")
    rows = []
    for claim in sorted(data["claims"], key=lambda c: (order.index(c["verdict"]), c["id"])):
        rows.append([claim["id"], claim["claim"], claim["verdict"], claim["explanation"]])
    lines.append(md_table(["ID", "Claim", "Verdict", "Why"], rows))
    lines.append("")
    return "\n".join(lines)


def render_upper_limits(data, uls) -> str:
    lines = ["# Upper limits", "",
             "Adult tolerable upper intake levels used in this review, with the critical "
             "effect each is based on.", ""]
    rows = []
    for row in data["ul"]:
        rows.append([row["nutrient"], row["ul_adult"], row["unit"], row["basis"],
                     row["critical_effect"], row["notes"]])
    lines.append(md_table(["Nutrient", "UL", "Unit", "Basis", "Critical effect", "Notes"], rows))
    lines.append("")
    lines += ["## Products at or above 80% of a UL", ""]
    rows = []
    for p in data["products"]:
        m = metrics(p, uls)
        hits = [f"{k} ({pct(v)})" for k, v in m["shares"].items() if v >= 0.8]
        if hits:
            rows.append([f"{p['brand']} {p['product']}", "; ".join(hits)])
    if rows:
        lines.append(md_table(["Product", "Nutrients at 80%+ of UL"], rows))
    else:
        lines.append("None.")
    lines.append("")
    return "\n".join(lines)


def render_interactions(data) -> str:
    lines = ["# Interactions", "",
             "Generated from `data/interactions.csv`. Severity reflects the consequence of "
             "missing the interaction, not the likelihood that a standard multivitamin "
             "causes it.", ""]
    for severity in ["High", "Moderate", "Low"]:
        group = [r for r in data["interactions"] if r["severity"] == severity]
        if not group:
            continue
        lines += [f"## {severity} severity", ""]
        rows = [[r["interacting_pair"], r["mechanism"], r["clinical_effect"], r["management"]]
                for r in group]
        lines.append(md_table(["Pair", "Mechanism", "Effect", "Management"], rows))
        lines.append("")
    return "\n".join(lines)


def render_references(data) -> str:
    lines = ["# References", "",
             "Numbered as in `data/references.csv`. DOIs resolve at `doi.org`; URLs point "
             "to the publisher, PubMed Central, or the issuing agency.", ""]
    for ref in data["refs"]:
        link = f"https://doi.org/{ref['identifier']}" if ref["identifier"] else ref["url"]
        lines.append(
            f"{ref['id']}. {ref['authors']} ({ref['year']}). *{ref['title']}*. "
            f"{ref['journal']}. [{link}]({link})"
        )
    lines.append("")
    return "\n".join(lines)


def build(data) -> dict[str, str]:
    uls = ul_index(data["ul"])
    return {
        "product-comparison.md": render_products(data, uls),
        "ul-check.md": render_ul_check(data, uls),
        "ingredient-forms.md": render_ingredients(data),
        "evidence-tables.md": render_evidence(data),
        "claims-table.md": render_claims(data),
        "upper-limits.md": render_upper_limits(data, uls),
        "interactions.md": render_interactions(data),
        "references.md": render_references(data),
    }


def summary(data, uls) -> str:
    products = data["products"]
    costs = [metrics(p, uls)["cost"] for p in products]
    cheapest = min(products, key=lambda p: metrics(p, uls)["cost"])
    dearest = max(products, key=lambda p: metrics(p, uls)["cost"])
    certified = [p for p in products if p["certification"] not in {"None documented", "USDA Organic"}]
    return "\n".join([
        f"products: {len(products)}",
        f"references: {len(data['refs'])}",
        f"evidence rows: {len(data['evidence'])}",
        f"claims: {len(data['claims'])}",
        f"ingredient forms: {len(data['ingredients'])}",
        f"interactions: {len(data['interactions'])}",
        f"cost range: {money(min(costs))} to {money(max(costs))} per serving",
        f"cost ratio: {max(costs) / min(costs):.0f}x",
        f"cheapest: {cheapest['brand']} {cheapest['product']} at {money(metrics(cheapest, uls)['cost'])}",
        f"dearest: {dearest['brand']} {dearest['product']} at {money(metrics(dearest, uls)['cost'])}",
        f"third-party certified: {len(certified)} of {len(products)}",
        f"median cost: {money(median(costs))}",
    ])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="validate and fail if generated files are stale")
    args = parser.parse_args()

    try:
        data = load_all()
        uls = ul_index(data["ul"])
        outputs = build(data)
    except ValidationError as exc:
        print(f"validation failed: {exc}", file=sys.stderr)
        return 1

    GEN.mkdir(parents=True, exist_ok=True)
    stale = []
    for name, content in outputs.items():
        path = GEN / name
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                stale.append(name)
        else:
            path.write_text(content, encoding="utf-8", newline="\n")

    if args.check:
        if stale:
            print("stale generated files: " + ", ".join(stale), file=sys.stderr)
            print("run: python analysis/build_tables.py", file=sys.stderr)
            return 1
        print("datasets valid; generated tables up to date")
        return 0

    print(summary(data, uls))
    print(f"wrote {len(outputs)} files to {GEN.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
