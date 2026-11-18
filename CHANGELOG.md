# Changelog

All notable changes to this review are recorded here. The datasets are versioned
with the release; reference IDs are stable across versions.

## 1.0.0 — 2026-11-18

Initial release.

### Report

- Comprehensive scientific report covering regulation, formulation, ingredient
  forms and bioavailability, randomised evidence for mortality, cardiovascular
  disease, cancer, cognition, immunity, energy, pregnancy and AMD, safety and upper
  limits, drug interactions, product quality, cost, populations and practical
  recommendations.

### Data

- `data/products.csv`: 20 products across mass-market, premium, whole-food, gummy
  and powder formats, with 23 declared nutrients, format, certification and price.
- `data/ingredients.csv`: 55 nutrient forms with bioavailability, absorption notes,
  adult UL and typical multivitamin dose.
- `data/evidence.csv`: 67 graded evidence rows across 13 domains.
- `data/claims.csv`: 36 claims adjudicated as supported, partially supported,
  unsupported or false.
- `data/upper_limits.csv`: 22 adult upper limits with critical effects.
- `data/interactions.csv`: 24 drug-nutrient and nutrient-nutrient interactions.
- `data/references.csv`: 72 references with DOI or stable URL.

### Analysis

- `analysis/build_tables.py`: schema validation, cross-reference checking, cost and
  UL-share metrics, and deterministic generation of eight Markdown tables.
- CI workflow runs `--check` on every push.

### Documentation

- Methodology and grading scheme.
- Domain-by-domain evidence review.
- Forms and bioavailability guide.
- Safety and upper-limit assessment.
- Population benefit assessment.
- Targeted versus general supplementation framework.
- Brand and product comparison guide.

### Known limitations

- Twenty products are a purposive sample, not a census.
- Prices are US retail snapshots from November 2026.
- The underlying trials tested a narrow slice of the market.
- The review has not been peer reviewed.
