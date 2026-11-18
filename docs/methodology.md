# Methodology

## Question

Do multivitamin and multimineral (MVM) supplements improve meaningful health
outcomes in adults, which formulations and ingredient forms are better, who
actually benefits, and what are the risks and costs?

The review deliberately separates four questions that marketing merges:

1. **Efficacy** — does the product change a health outcome in a randomised trial?
2. **Nutrition** — does it correct or prevent a deficiency?
3. **Formulation** — does the form, dose or combination change absorption or safety?
4. **Value** — what does a daily dose cost, and what does that money buy?

## Evidence search

Sources were searched to November 2026:

- PubMed/MEDLINE and PubMed Central
- Cochrane Library
- Google Scholar for citation chasing
- ClinicalTrials.gov and ISRCTN for registered trials and substudies
- NIH Office of Dietary Supplements (ODS) fact sheets and the Dietary Supplement
  Label Database (DSLD)
- EFSA and Institute of Medicine (IOM) upper-limit documents
- USP, NSF and ConsumerLab certification and testing records
- FDA labelling and GMP regulations

Search terms combined `multivitamin`, `multivitamin-mineral`, `MVM`, `dietary
supplement`, and `micronutrient` with `mortality`, `cardiovascular`, `cancer`,
`cognition`, `infection`, `fatigue`, `pregnancy`, `bioavailability`, `upper
limit`, `heavy metals`, and `cost`.

### Inclusion

- Randomised controlled trials in adults, of any duration, testing a supplement
  with at least five vitamins and/or minerals.
- Systematic reviews and meta-analyses of such trials.
- Large prospective cohorts where RCTs do not exist (mortality, long-term use).
- Government and expert-body documents for reference intakes and upper limits.
- Independent laboratory testing and peer-reviewed market surveys for product
  quality.

### Exclusion

- Single-nutrient trials, except where they establish a principle (beta-carotene
  in smokers, vitamin E and prostate cancer, folic acid and neural tube defects)
  or a safety boundary that applies to multis.
- Paediatric formulations, sports-only products, herbal "greens" without declared
  vitamin amounts, and prescription products.
- Animal and in vitro studies, except for mechanism.
- Marketing material, retailer copy, and influencer content as evidence. These
  were used only to identify claims to adjudicate.

## Grading

Certainty follows GRADE logic: risk of bias, inconsistency, indirectness,
imprecision and publication bias. The four levels are defined in
[`data/data-dictionary.md`](../data/data-dictionary.md).

Two axes are kept separate on purpose:

- **Status** (`Established`, `Emerging`, `Mixed`, `Unsupported`) describes what the
  evidence says.
- **Certainty** (`High` to `Very low`) describes how much to trust it.

A finding can be established and clinically trivial; a finding can be uncertain
and still worth acting on. Merging the two is how supplement marketing turns
"trend toward fewer colds in a subgroup" into "supports immune health".

Absolute effects are reported wherever the source provides them. A relative risk
of 0.93 sounds larger than "about 2 to 12 fewer cancers per 1,000 people over 3 to
11 years", which is the same finding.

## Product sample

Twenty products were selected purposively, not randomly, to cover:

- the mass-market tablet duopoly (Centrum, One A Day, Nature Made, Kirkland);
- premium capsules (Thorne, Pure Encapsulations, Ritual, Life Extension);
- whole-food and organic tablets (Garden of Life);
- gummies (SmartyPants, Centrum MultiGummies);
- powders marketed as multis (AG1, Huel Daily Greens);
- a high-potency sports formula (Opti-Men).

Selection was driven by market share, availability, and whether the product
illustrates a formulation pattern the report discusses. It is not a census, and
the cost medians are not market-wide averages.

### Label data

Nutrient amounts, forms and serving sizes were taken from the product label, via
the NIH DSLD where available and the manufacturer's Supplement Facts panel
otherwise. Where a label declares a nutrient in IU, it was converted (vitamin D:
1,000 IU = 25 mcg; vitamin E: 1 IU natural = 0.67 mg alpha-tocopherol).

Where the label does not disclose a form (for example, the iron salt in a tablet),
the field says `not stated` rather than guessing.

### Price data

Prices are US retail snapshots from 18 November 2026. `price_verified = yes`
means the price was read on the brand store or a major retailer listing during
collection. `no` marks shelf estimates, which vary by channel and promotion. The
`price_channel` column records where each price came from.

Cost per serving is package price divided by the number of **daily servings** in
the package, after accounting for products that require two or three capsules or
gummies per serving. Cost per year is a 365-day projection at the same price.

## Upper-limit arithmetic

Each product's declared nutrients are compared with the adult UL in
[`data/upper_limits.csv`](../data/upper_limits.csv). The script reports the
largest ratio and the nutrient driving it.

Three deliberate choices:

- **Vitamin A is treated as preformed.** This overstates the UL share of products
  that use beta-carotene, because beta-carotene has no UL. It is the conservative
  direction, and the report says so.
- **Folate is excluded.** Dietary folate equivalents and folic acid are not
  interchangeable against the 1,000 mcg folic acid UL. Folate is discussed
  separately.
- **Food is excluded.** The calculation is label arithmetic only. A person eating
  liver, fortified cereal and a multivitamin has a different total intake.

## Verification

- Every numeric claim in the report traces to a row in `data/evidence.csv` and a
  reference in `data/references.csv`.
- Cross-references are checked mechanically: every `source_ids` entry must resolve.
- IDs are unique; categorical values are constrained; product arithmetic is
  range-checked.
- `python analysis/build_tables.py --check` verifies that the generated tables are
  byte-identical to what the datasets produce. CI runs it on every push.

## Limitations

1. **The trials are not the market.** PHS II tested Centrum Silver; COSMOS tested
   Centrum Silver plus cocoa extract; SU.VI.MAX tested a five-ingredient
   antioxidant mixture. None tested the premium capsules, gummies or greens
   powders that dominate advertising.
2. **Follow-up is short relative to the outcome.** Cancer and cardiovascular
   disease develop over decades; COSMOS followed participants for 3.6 years.
3. **Populations are narrow.** PHS II was male physicians; COSMOS was mostly white,
   well-educated older adults. Neither is a representative sample.
4. **Publication and funding bias.** Industry funds many supplement trials.
   Negative trials are less likely to be published. Certainty was downgraded where
   a finding rested only on industry data.
5. **Product quality is a moving target.** Formulations change without notice;
   ConsumerLab's failure rate has varied between 27% and 44% across reviews.
6. **Prices are snapshots.** They differ by retailer, country, subscription and
   package size.
7. **No new laboratory work.** Contaminant and label-accuracy statements come from
   published testing, not from assays commissioned for this review.
8. **Nutrigenomics is not ready.** MTHFR genotyping is sometimes used to sell
   methylfolate. The evidence that genotype-guided multivitamin choice improves
   outcomes is not there.

## AI-assistance disclosure

This review was assembled with AI assistance under human direction. Every
quantitative claim was checked against the cited abstract, table or dataset, and
the datasets and generated tables are machine-validated. It has **not** been peer
reviewed. Treat it as a well-documented starting point, not a substitute for the
primary literature or clinical judgement.

## Corrections

Open an issue with the claim, the source, and the proposed change. See
[`CONTRIBUTING.md`](../CONTRIBUTING.md). Corrections that change a number in
`data/` also require regenerating the tables.
