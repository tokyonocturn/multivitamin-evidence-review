# Multivitamins: An Independent Evidence Review and Product Database

A source-linked review of multivitamin and multimineral supplements — what the
randomised trials actually show, how formulations differ, which ingredient forms
matter, where the upper limits bite, who benefits, and what 20 real products cost
per daily serving. Built as a reproducible repository: every quantitative claim
traces to a reference, and every table is generated from the CSV datasets in
[`data/`](data/).

**No brand funding, affiliate links, or sponsorship.** Prices were collected in
November 2026 and will change.

---

## Bottom line

**Multivitamins are a small-effect intervention with a large marketing budget.**
They do not extend life, prevent heart attacks or strokes, or give you energy. They
produce a small, fragile reduction in cancer incidence without reducing cancer
deaths, and a small cognitive signal in one recent trial. The one unambiguous
benefit is folic acid in pregnancy. The people who benefit most are those with a
real nutritional gap, not those with the best diets.

| Question | Answer | Confidence |
| --- | --- | --- |
| Do they help you live longer? | **No.** Pooled RCTs: OR 0.94 (0.87-1.01), 9 trials, n=51,550. A 390,124-person cohort found 4% *higher* mortality among users. | Moderate |
| Do they prevent heart attacks or strokes? | **No.** PHS II HR 1.02 (0.92-1.13); COSMOS HR 0.98 (0.86-1.12); CVD mortality OR 0.94. | High |
| Do they prevent cancer? | **Slightly fewer cases, no fewer deaths.** Cancer incidence OR 0.93 (0.87-0.99); cancer mortality OR 0.94 (0.81-1.09). Absolute difference 0.2-1.2%. | Moderate |
| Do they improve memory? | **A little, in older adults.** COSMOS: +0.07 SD global cognition, about 2 years less cognitive aging. PHS II found nothing after 12 years. | Moderate / Low |
| Do they give you energy? | **No.** B vitamins are cofactors, not fuel. No effect on fatigue in replete adults. | Moderate |
| Do they boost immunity? | **Not reliably.** The largest nursing-home trial was null; reviews call the evidence weak and conflicting. | Low |
| Do they prevent birth defects? | **Yes.** Folic acid cuts neural tube defects by about 72%. The strongest evidence in the field. | High |
| Which forms matter? | **D3 over D2; iron salts for tolerability; magnesium salts over oxide; zinc with copper.** Folate and B12 forms are mostly marketing. | Moderate-High |
| What is a sensible formula? | D3 ≥ 25 mcg, zinc 8-15 mg with copper, B6 < 50 mg, niacin < 35 mg, iron only if needed, third-party certified. | Moderate |
| Who genuinely benefits? | Pregnancy, documented deficiency, bariatric surgery, malabsorption, vegans (B12), poor intake, nutrient-depleting drugs. | High |
| Who probably does not? | Healthy, well-nourished adults eating a varied diet. | Moderate |
| What does it cost? | **$0.05 to $3.30 per serving — a 70-fold spread.** Median $0.28. Only 6 of 20 products are third-party certified. | Price snapshot |

The detailed argument, caveats and citations are in the
[full report](report/multivitamin-scientific-report.md).

---

## What is in this repository

| Path | Contents |
| --- | --- |
| [`report/multivitamin-scientific-report.md`](report/multivitamin-scientific-report.md) | Comprehensive report: regulation, formulation, bioavailability, every major outcome, safety, interactions, quality, cost, populations, recommendations. |
| [`docs/methodology.md`](docs/methodology.md) | Search strategy, inclusion rules, grading scheme, product sampling, price method, limitations, AI disclosure. |
| [`docs/evidence-review.md`](docs/evidence-review.md) | Domain-by-domain narrative of the trial evidence. |
| [`docs/forms-and-bioavailability.md`](docs/forms-and-bioavailability.md) | Vitamin and mineral forms, absorption, "whole food" claims, gummies versus tablets. |
| [`docs/safety-and-upper-limits.md`](docs/safety-and-upper-limits.md) | Toxicity, ULs, stacking arithmetic, drug interactions, contamination, special populations. |
| [`docs/who-benefits.md`](docs/who-benefits.md) | Population-by-population benefit and harm assessment. |
| [`docs/targeted-vs-general.md`](docs/targeted-vs-general.md) | When targeted supplementation beats a general multi, with a decision framework. |
| [`docs/brand-comparison.md`](docs/brand-comparison.md) | How to read the product data, value tiers, red flags, picks by situation. |
| [`docs/generated/`](docs/generated/) | Generated tables: products, UL checks, ingredient forms, evidence, claims, interactions, references. |
| [`data/products.csv`](data/products.csv) | Product database: 20 products, 23 nutrients, format, certification, price. |
| [`data/ingredients.csv`](data/ingredients.csv) | Ingredient-form database: 55 forms with bioavailability, UL and dose notes. |
| [`data/evidence.csv`](data/evidence.csv) | 67 graded evidence rows across 13 domains. |
| [`data/claims.csv`](data/claims.csv) | 36 common claims adjudicated as supported, partial, unsupported or false. |
| [`data/upper_limits.csv`](data/upper_limits.csv) | 22 upper limits with critical effects. |
| [`data/interactions.csv`](data/interactions.csv) | 24 drug-nutrient and nutrient-nutrient interactions. |
| [`data/references.csv`](data/references.csv) | 72 references with DOI or stable URL. |
| [`data/data-dictionary.md`](data/data-dictionary.md) | Column definitions and grading scheme. |
| [`analysis/build_tables.py`](analysis/build_tables.py) | Validates the datasets, computes cost and UL metrics, regenerates all tables. |

---

## Reproduce it

Requires Python 3.10+ and no third-party packages.

```bash
python analysis/build_tables.py           # validate + regenerate tables
python analysis/build_tables.py --check   # fail if data or tables are stale
```

The `--check` command runs in CI on every push
([`.github/workflows/validate.yml`](.github/workflows/validate.yml)). It verifies:

- required columns and allowed categorical values;
- unique IDs and resolvable cross-references between evidence, claims, ingredients,
  interactions and references;
- plausible serving size, package size and price arithmetic;
- that every generated Markdown file is byte-identical to what the data produces.

### Derived cost model

```
cost per serving   = price / daily servings per container
cost per year      = cost per serving x 365
cost per 25 mcg D  = cost per serving / (vitamin D mcg / 25)
UL share           = declared amount / adult upper limit
```

The UL share is computed for every nutrient with an established adult UL. Vitamin A
is treated as preformed (worst case); folate is excluded because dietary folate
equivalents are not comparable with the folic acid UL.

---

## How the evidence was handled

- **Established** findings have multiple consistent RCTs or a meta-analysis, with a
  plausible mechanism and no serious unresolved contradiction.
- **Emerging** findings have human data but small samples, inconsistency, or very
  low certainty.
- **Mixed** means the pooled direction depends on outcome, population or subgroup.
- **Unsupported** means the claim is marketed or repeated but is not supported by
  controlled human evidence.

Certainty is graded High / Moderate / Low / Very low using GRADE logic. The two
axes are deliberately separate: a real but tiny effect can be *established* and
still be clinically unimportant.

Full details, including how contradictions were resolved, are in
[`docs/methodology.md`](docs/methodology.md).

---

## What this review is not

- **Not medical advice.** Supplements can interact with medicines. People who are
  pregnant, take warfarin, levothyroxine, methotrexate or retinoids, have kidney,
  liver or thyroid disease, haemochromatosis, or unexplained symptoms should talk
  to a clinician.
- **Not a primary laboratory study.** Product-quality conclusions come from
  published independent testing (ConsumerLab, USDA, peer-reviewed market surveys)
  and certifier databases; this project did not commission new assays.
- **Not exhaustive.** Twenty products are a purposive sample across price tiers,
  formats and certifications, not a census of the market.
- **Not free of uncertainty.** Supplement research is partly industry-funded,
  publication bias is real, and the largest modern trial followed participants for
  only 3.6 years. Effect estimates should be read as best current approximations.
- **Not a reason to ignore symptoms.** A multivitamin can mask B12 deficiency and
  can delay diagnosis. Fatigue, weight loss, neuropathy and anaemia need
  investigation.

### AI-assistance disclosure

This review was assembled with AI assistance under human direction. Every numeric
claim was checked against the cited abstract, table or dataset; the datasets and
generated tables are machine-validated. It has **not** been peer reviewed. Treat it
as a well-documented starting point, not a substitute for the primary literature or
clinical judgement.

Corrections are welcome: open an issue with the claim, the source, and the proposed
change. See [`CONTRIBUTING.md`](CONTRIBUTING.md).

---

## Citation and license

Citation metadata is in [`CITATION.cff`](CITATION.cff).

- **Text and data:** CC BY 4.0 — share and adapt with attribution.
- **Code:** MIT.

See [`NOTICE`](NOTICE) for the full content-license and medical disclaimer.
