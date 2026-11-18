# Contributing

Corrections are the point of a review like this. If a number is wrong, a citation
does not support its claim, or a product label has changed, please open an issue.

## Reporting a correction

Include:

1. The file and row (for example, `data/evidence.csv`, id `mvm-cancer-incidence`).
2. The claim as written.
3. The source that contradicts it, with a DOI, PMID or stable URL.
4. The proposed replacement text or value.

Claims that a supplement "works" or "does not work" without a specific outcome,
population and effect size cannot be adjudicated. Please be specific.

## Changing data

The CSV files are the source of truth. After any change:

```bash
python analysis/build_tables.py
python analysis/build_tables.py --check
```

The first command regenerates the tables; the second must pass. CI runs `--check`
on every push and will fail if the generated files are stale.

### Rules for dataset changes

- Keep IDs stable. If a row must be replaced, add a new ID rather than reusing an
  old one for a different claim.
- Every `source_ids` entry must resolve to a row in `data/references.csv`.
- Use the categorical values defined in `data/data-dictionary.md`.
- For product data, record the label date and the price channel. Do not guess a
  form the label does not disclose; use `not stated`.
- Do not add affiliate links, referral codes or brand sponsorship.

## Style

- Report absolute effects alongside relative effects.
- State the population and the dose. "Multivitamins reduce cancer" is not a finding;
  "daily Centrum Silver reduced total cancer incidence in male physicians, HR 0.92
  (0.86-0.998), with no reduction in cancer mortality" is.
- Separate certainty from clinical importance.
- Avoid marketing language in both directions. Neither "miracle" nor "scam" is an
  evidence claim.

## Scope

In scope: adult multivitamin and multimineral products, their ingredients, forms,
doses and outcomes; product quality and cost; safety and interactions.

Out of scope: paediatric products, single-nutrient supplements except where they
establish a principle, herbal and botanical products without declared vitamins, and
personal medical advice.

## License

By contributing, you agree that text and data contributions are licensed under
CC BY 4.0 and code contributions under the MIT License.
