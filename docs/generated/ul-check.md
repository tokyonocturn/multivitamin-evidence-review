# Upper-limit check

Each product's declared nutrients are compared with the adult tolerable upper intake levels in `data/upper_limits.csv`. Vitamin A is treated as preformed (worst case). Folate is excluded because dietary folate equivalents cannot be compared directly with the folic acid UL.

This is a label arithmetic exercise. It does not account for food, other supplements, or individual absorption.

| Product | Max UL share | Driver | At or above UL | 80-99% of UL |
| --- | --- | --- | --- | --- |
| Thorne Basic Nutrients 2/Day | 229% | Niacin | Niacin 229% | none |
| Optimum Nutrition Opti-Men | 214% | Niacin | Vitamin A 100%; Niacin 214% | none |
| Life Extension One-Per-Day | 143% | Niacin | Niacin 143% | none |
| One A Day Women's Complete | 69% | Niacin | none | none |
| Pure Encapsulations O.N.E. Multivitamin | 62% | Zinc | none | none |
| Huel Daily Greens | 60% | Niacin | none | none |
| One A Day Men's 50+ | 60% | Zinc | none | none |
| One A Day Women's 50+ | 60% | Zinc | none | none |
| Athletic Greens AG1 | 57% | Niacin | none | none |
| Centrum Silver Adults 50+ | 57% | Niacin | none | none |
| Centrum Adults | 57% | Niacin | none | none |
| Kirkland Signature Daily Multi | 57% | Niacin | none | none |
| Nature Made Multi Complete with Iron | 57% | Niacin | none | none |
| Garden of Life mykind Organics Women's Once Daily | 53% | Niacin | none | none |
| One A Day Men's Complete | 50% | Niacin | none | none |
| Ritual Essential for Women 18+ | 50% | Vitamin D | none | none |
| Ritual Essential for Men 18+ | 50% | Vitamin D | none | none |
| SmartyPants Women's Multi & Omegas | 50% | Vitamin D | none | none |
| Centrum Silver Women 50+ | 40% | Niacin | none | none |
| Centrum Women MultiGummies | 25% | Vitamin D | none | none |

## Nutrients with no adult UL

Absence of a UL is not a guarantee of safety; it means the data were insufficient to set one. Vitamin K, B12, biotin, pantothenic acid and chromium fall in this category.

## Where the UL itself is contested

- **Niacin.** The 35 mg UL applies to synthetic nicotinic acid and niacinamide. Flushing is the acute effect; hepatotoxicity appears at gram doses. Several high-potency multis supply 50-80 mg.
- **Vitamin B6.** The 100 mg UL is based on sensory neuropathy. Cases have been reported below it with long-term use, so 50-75 mg in a daily multi is not trivial.
- **Vitamin A.** The 3,000 mcg UL applies to preformed retinol. Beta-carotene is not covered, but high-dose beta-carotene has its own risk in smokers.
- **Zinc.** The 40 mg UL is about copper balance as much as zinc toxicity. A 25 mg zinc multi without copper is a design flaw, not an overdose.
- **Magnesium.** The 350 mg UL applies to supplemental magnesium only. Food magnesium is not restricted.
