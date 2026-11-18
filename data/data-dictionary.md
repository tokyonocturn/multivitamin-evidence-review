# Data dictionary

Every table and figure in this repository is generated from the seven CSV files in
this directory. The CSV files are the source of truth; the Markdown files under
`docs/generated/` are build artifacts. `analysis/build_tables.py --check` fails if
the two disagree.

All files are UTF-8, comma-separated, with a single header row. Fields containing
commas are quoted. IDs are lowercase kebab-case and unique within their file.

---

## `products.csv` — product database

One row per product, at the label's stated daily serving (not per capsule or
gummy). Nutrient columns give the **declared elemental or active amount per
serving**; `0` means the label does not declare that nutrient. Blanks are not
used, because a zero and a missing value have the same practical meaning on a
multivitamin label: you do not get a declared amount.

| Column | Type | Meaning |
| --- | --- | --- |
| `id` | text | Stable identifier, e.g. `centrum-silver-50plus`. |
| `brand` | text | Brand as printed on the label. |
| `product` | text | Product name. |
| `target` | enum | `general adult`, `men`, `women`, `50+`, `men 50+`, `women 50+`. |
| `format` | enum | `tablet`, `capsule`, `gummy`, `powder`, `softgel`. |
| `serving_units_per_day` | integer | Capsules, tablets or gummies per daily serving. |
| `servings_per_container` | integer | **Daily servings** in the package, after dividing by `serving_units_per_day`. |
| `price_usd` | decimal | Package price in US dollars. |
| `price_channel` | text | Where the price was observed. |
| `price_date` | date | ISO date of the price snapshot. |
| `price_verified` | enum | `yes` if the price was read on the brand or a major retailer page during collection; `no` if it is a shelf estimate. |
| `certification` | text | Third-party quality certification, or `None documented`. Organic and Non-GMO seals are recorded but are **not** purity certifications. |
| `vitamin_a_ug` | decimal | mcg RAE of total vitamin A (preformed plus provitamin A as declared). |
| `vitamin_c_mg` | decimal | mg. |
| `vitamin_d_ug` | decimal | mcg (1,000 IU = 25 mcg). |
| `vitamin_e_mg` | decimal | mg alpha-tocopherol equivalent. |
| `vitamin_k_ug` | decimal | mcg, any form. |
| `thiamin_mg` … `pantothenic_mg` | decimal | B-vitamin amounts as declared. |
| `folate_ug_dfe` | decimal | mcg dietary folate equivalents. |
| `vitamin_b12_ug` | decimal | mcg. |
| `calcium_mg`, `iron_mg`, `magnesium_mg`, `zinc_mg` | decimal | mg elemental mineral. |
| `iodine_ug`, `selenium_ug`, `chromium_ug`, `molybdenum_ug` | decimal | mcg. |
| `copper_mg`, `manganese_mg` | decimal | mg. |
| `folate_form` | text | `folic acid`, `L-5-MTHF`, `L-methylfolate`, `food folate`, etc. |
| `b12_form` | text | `cyanocobalamin`, `methylcobalamin`, etc. |
| `vitamin_a_form` | text | Preformed/provitamin split where the label states it. |
| `iron_form`, `zinc_form`, `magnesium_form` | text | Salt or chelate where disclosed. |
| `has_k2` | text | `yes MK-4`, `yes MK-7`, or `no`. |
| `notes` | text | Serving-size traps, extra ingredients, label quirks. |

### Derived metrics (computed, never stored)

```
cost_per_serving = price_usd / servings_per_container
cost_per_year    = cost_per_serving x 365
cost_per_25ug_D  = cost_per_serving / (vitamin_d_ug / 25)
ul_share[n]      = declared_amount[n] / adult_UL[n]
max_ul_share     = max over nutrients with an established UL
```

`cost_per_25ug_D` normalises by the one nutrient most products under-dose. It is
a value benchmark, not a claim that vitamin D is the only nutrient that matters.

---

## `ingredients.csv` — ingredient-form database

One row per nutrient form, not per product.

| Column | Meaning |
| --- | --- |
| `id`, `nutrient`, `form`, `form_class` | Identity and classification (`Preformed`, `Provitamin A`, `Chelate`, `Organic salt`, `Food-derived`, etc.). |
| `bioavailability` | `High`, `Moderate`, `Low-moderate`, `Low`, `Variable`. A qualitative summary of human data, not a percentage unless stated. |
| `absorption_notes` | Mechanism and the practical consequence. |
| `adult_ul` | Adult UL in `ul_unit`, or `None` where no UL is established. |
| `typical_mvm_dose` | Range observed in the products in this repo and in common US formulas. |
| `evidence_quality` | `High`, `Moderate`, `Low` — confidence in the bioavailability comparison, not in the health benefit. |
| `notes` | Marketing claims that outrun the data, and formulation consequences. |
| `source_ids` | Semicolon-separated reference IDs. |

---

## `evidence.csv` — graded evidence table

| Column | Meaning |
| --- | --- |
| `id` | Stable identifier. |
| `domain` | `Outcomes`, `Cognition`, `Immunity`, `Energy`, `Cardiovascular`, `Eyes`, `Pregnancy`, `Safety`, `Interactions`, `Quality`, `Forms`, `Deficiency`, `Cost`. |
| `question` | The question being answered. |
| `outcome` | The measured endpoint. |
| `population` | Who was studied. This matters more than the pooled number. |
| `evidence_type` | RCT, pooled RCTs, cohort, meta-analysis, market test, etc. |
| `studies_participants` | Number and size of studies. |
| `pooled_effect` | Point estimate as reported. |
| `effect_measure` | HR, OR, RR, SMD, mean difference, %, narrative. |
| `ci` | 95% CI where reported. |
| `certainty` | `High`, `Moderate`, `Low`, `Very low` (GRADE logic), or `Not graded`. |
| `status` | `Established`, `Emerging`, `Mixed`, `Unsupported`. |
| `source_ids` | Semicolon-separated reference IDs. |
| `notes` | Interpretation, contradictions, and what would change the conclusion. |

### Certainty

- **High** — multiple large trials or a meta-analysis with consistent results,
  precise estimates, and no serious risk of bias.
- **Moderate** — consistent but with imprecision, indirectness, or reliance on one
  trial.
- **Low** — one trial, small samples, large heterogeneity, or observational data.
- **Very low** — hypothesis-generating only.

### Status

`Established` and `Emerging` describe the state of the evidence. They are
deliberately separate from certainty and from clinical importance: a real effect
can be established and still be too small to matter.

- **Established** — replicated, consistent, and unlikely to be reversed by more
  data.
- **Emerging** — human data exist but are limited, inconsistent, or unreplicated.
- **Mixed** — direction depends on outcome, population, or subgroup.
- **Unsupported** — marketed but not supported by controlled human evidence.

---

## `claims.csv` — claim adjudication

| Column | Meaning |
| --- | --- |
| `id`, `claim` | The claim as it is commonly made. |
| `category` | `Marketing`, `Cardiovascular`, `Cancer`, `Longevity`, `Immunity`, `Cognition`, `Policy`, `Formulation`, `Safety`, `Pregnancy`, `Quality`, `Value`, `Interaction`, `Regulation`, `Performance`, `Cosmetic`. |
| `verdict` | `Supported`, `Partially supported`, `Unsupported`, `False`. |
| `explanation` | What the evidence shows and why the verdict was assigned. |
| `source_ids` | Semicolon-separated reference IDs. |

`Partially supported` is used when a claim is true in a specific population, dose
or setting but false as a general statement.

---

## `upper_limits.csv`

| Column | Meaning |
| --- | --- |
| `nutrient` | Nutrient name. |
| `ul_adult` | Adult UL, or `None`. |
| `unit` | Unit of the UL. |
| `basis` | `IOM`, `EFSA`, or both. |
| `critical_effect` | The adverse effect the UL is based on. |
| `notes` | Scope and caveats. |
| `source_ids` | References. |

The script uses this file to compute each product's `max_ul_share`. Where IOM and
EFSA differ, the more conservative adult value is used and the difference is noted.

---

## `interactions.csv`

| Column | Meaning |
| --- | --- |
| `id` | Identifier. |
| `interacting_pair` | The two agents. |
| `mechanism` | Pharmacokinetic or pharmacodynamic explanation. |
| `clinical_effect` | What happens to the patient. |
| `severity` | `High`, `Moderate`, `Low`. |
| `management` | Practical action. |
| `source_ids` | References. |

---

## `references.csv`

| Column | Meaning |
| --- | --- |
| `id` | `R01`-style identifier, stable across versions. |
| `authors`, `year`, `title`, `journal` | Citation metadata. |
| `identifier` | DOI where one exists. |
| `url` | Stable link (publisher, PMC, or government page). |
| `type` | RCT, systematic review, meta-analysis, cohort, government fact sheet, etc. |

---

## Grading rules for this review

1. **Population first.** A trial in nutritionally deficient adults does not
   generalise to well-nourished adults. Every outcome row records the population
   for this reason.
2. **Absolute over relative.** A 7% relative reduction in cancer incidence is
   reported alongside the absolute difference (about 0.2% to 1.2%), because the
   relative figure is what marketing uses.
3. **Mortality is the hardest endpoint.** Morbidity signals that do not move
   mortality, function, or quality of life are labelled as such.
4. **Industry funding is recorded, not disqualifying.** Many supplement trials are
   industry-funded. The review notes funding where it is likely to matter and
   downgrades certainty when a finding rests only on industry data.
5. **No composite marketing endpoints.** "Immune support", "energy" and "metabolic
   support" are not endpoints. They are replaced with infections, fatigue scores,
   and measured nutrient status.

## What the datasets do not contain

- No new laboratory assays. Product-quality statements come from published
  independent testing and certifier databases.
- No individual-patient data.
- No prices for every channel. Retail prices move; the snapshot is dated.
- No products outside the US market, and no prescription products.
