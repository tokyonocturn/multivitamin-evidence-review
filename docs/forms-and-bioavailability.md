# Forms and bioavailability

A multivitamin is not one ingredient. It is 10 to 30 separate chemical decisions
compressed into a tablet. The form of each nutrient determines how much is
absorbed, how much can fit in the pill, how stable it is on the shelf, and what it
costs. This document covers the decisions that actually change what you get.

The full form-by-form dataset is in
[`data/ingredients.csv`](../data/ingredients.csv) and the generated table is
[`docs/generated/ingredient-forms.md`](generated/ingredient-forms.md).

---

## The short version

| Nutrient | Form that matters | Practical difference |
| --- | --- | --- |
| Vitamin D | **D3 (cholecalciferol)**, not D2 | D3 raises 25(OH)D more at the same dose |
| Vitamin K | K1 is enough for clotting; K2 is not proven to add outcome benefit | Warfarin patients need stable intake |
| Vitamin E | Natural d-alpha is about twice as potent per mg as dl-alpha | Labels in mg already correct for this |
| Folate | Folic acid and 5-MTHF are both effective | 5-MTHF avoids unmetabolised folic acid; no outcome trial shows superiority |
| Vitamin B12 | Cyanocobalamin is fine | All forms converge on the same active cobalamins |
| Iron | Bisglycinate is gentler; sulfate is the reference treatment | Form matters most when treating deficiency |
| Calcium | Citrate absorbs without acid; carbonate needs food | A multi's 200-300 mg is a top-up, not a treatment |
| Magnesium | Oxide is cheap and poorly absorbed (~4%) | Soluble salts and chelates deliver more per mg |
| Zinc | Citrate/bisglycinate are well absorbed; oxide is cheap | At 10-15 mg the difference is small; copper balance matters more |
| Selenium | Selenomethionine is retained better than selenite | 200 mcg is already half the UL |

---

## Vitamins

### Vitamin A: preformed versus provitamin

Two different things share the name. **Preformed vitamin A** (retinol, retinyl
palmitate, retinyl acetate) is active and carries the toxicity risk: the adult UL
is 3,000 mcg RAE, based on teratogenicity and liver toxicity. **Provitamin A**
(beta-carotene and other carotenoids) must be converted, and conversion is
regulated and inefficient — beta-carotene from plant food is about 15.6%
bioavailable.

This creates a labelling trap. A product can declare "900 mcg vitamin A (100% as
beta-carotene)" and look equivalent to one declaring 900 mcg of retinyl palmitate.
It is not. The first delivers far less retinol activity and no retinol toxicity;
the second delivers the full dose. The label's mcg RAE is supposed to account for
this, but the conversion assumptions are contested.

The other trap is safety in the opposite direction. High-dose beta-carotene —
20 to 30 mg/day — increased lung cancer risk by 18% in the ATBC trial and 28% in
CARET, with a 17% increase in all-cause mortality in CARET. That is 10 to 30 times
the beta-carotene dose in a typical multivitamin, and it occurred in smokers and
asbestos-exposed men. A standard multi's 0.5-3 mg has not been shown to cause harm.
The distinction matters: "beta-carotene causes cancer" is false as stated, and
"beta-carotene is a safe way to get vitamin A" is false for a smoker taking a
high-dose supplement.

### Vitamin D: D3 wins

A randomised trial in 107 adults compared 50 mcg/day of D2, D3 or placebo for
eight weeks in winter. D3 raised 25(OH)D3 from 41.5 to 88.0 nmol/L. D2 raised
25(OH)D2 but *lowered* 25(OH)D3 from 36.4 to 16.6 nmol/L, and total 25(OH)D was
significantly lower than with D3. The practical conclusion is simple: a
multivitamin should use D3. D2 is not useless, but it is less potent per mcg.

Most mass-market multis supply 400-1,000 IU (10-25 mcg). A product with 400 IU is
using an outdated dose that will not move a low 25(OH)D level much. 1,000-2,000 IU
is the useful range for a maintenance multi, and higher doses belong in a separate
product with monitoring.

### Vitamin E: the potency illusion

Natural *d*-alpha-tocopherol has about twice the biological activity of synthetic
*dl*-alpha-tocopherol per mg, because only four of the eight synthetic
stereoisomers are retained. This is real, but it is already baked into labelling:
"22.5 mg" of dl-alpha and "15 mg" of d-alpha are both 15 mg alpha-tocopherol
equivalent. Paying more for "natural E" in a multivitamin buys a smaller number on
the label, not more vitamin E.

The more important issue is dose. The UL is 1,000 mg/day, and high-dose vitamin E
(400 IU+) has a mortality signal in one meta-analysis and a 17% increase in
prostate cancer in SELECT. A multivitamin's 15-30 mg is nowhere near that.

### Vitamin K: K1, MK-4 and MK-7

Vitamin K1 (phylloquinone) is the dietary form and the one that matters for
clotting. MK-4 and MK-7 are menaquinones with longer half-lives and different
tissue distribution; MK-7 in particular accumulates. The marketing claim is that
K2 "directs calcium into bones and out of arteries". The mechanism is plausible —
osteocalcin and matrix Gla protein are vitamin K-dependent — but the outcome
trials are not there. Adding 90 mcg of MK-7 to a multivitamin is not evidence-based
and makes warfarin management harder, because MK-7's long half-life means a
missed or changed dose alters INR for days.

For everyone else, 20-120 mcg of K1 is a reasonable label amount, and the main
dietary issue is green vegetables, not supplements.

### Vitamin C: ascorbic acid is ascorbic acid

Ascorbic acid, sodium ascorbate and calcium ascorbate deliver the same anion.
Buffered forms are gentler on the stomach. "Food-derived" vitamin C from acerola
or camu camu has no demonstrated absorption advantage in humans; steady-state
studies comparing kiwifruit and synthetic ascorbic acid found no difference in
plasma, urine, white-cell or muscle levels.

Absorption is saturable. A 200 mg dose is almost completely absorbed; at 1 g,
fractional absorption falls and gastrointestinal effects rise. The UL is 2,000
mg/day. A multivitamin's 60-500 mg is well within range.

### B vitamins: the "energy" confusion

B vitamins are cofactors in energy metabolism. They do not supply energy. In a
person who is not deficient, supplementing them does not increase energy, reduce
fatigue or improve exercise performance. A prospective Swiss cohort found no
association between multivitamin use and fatigue severity or incidence. The
"energy metabolism" claim on a label is a description of biochemistry, not a
clinical effect.

Within the B group, the forms that generate the most marketing are folate and B12.

- **Folate.** Folic acid is synthetic, stable, 85% bioavailable and must be reduced
  and methylated. 5-MTHF is already reduced. Short-term bioavailability studies
  find them equivalent at equal doses; some trials find 5-MTHF raises plasma
  folate more, particularly in women with the MTHFR 677TT genotype. No trial shows
  better clinical outcomes with 5-MTHF. It does avoid unmetabolised folic acid in
  plasma, which is a reasonable preference, especially above 400 mcg.
- **B12.** Cyanocobalamin, methylcobalamin, adenosylcobalamin and
  hydroxocobalamin all converge on the same intracellular pools. Cyanocobalamin is
  stable, cheap and effective. Methylcobalamin is not superior for the general
  population, though it is a reasonable choice for the rare patient with a
  conversion defect.
- **B6.** Pyridoxine and P5P both work. The UL is 100 mg/day, based on sensory
  neuropathy; cases have been reported below it. High-potency multis that supply
  50-75 mg are not harmless, and stacking them with a B-complex is how people
  exceed the UL.
- **Niacin.** Nicotinic acid flushes; niacinamide does not. The UL is 35 mg/day for
  synthetic niacin. Several "high-potency" products supply 50-80 mg, which is above
  the UL and, at gram doses, hepatotoxic.

### Choline, biotin and the minor ingredients

Choline is an essential nutrient most people under-consume (the adequate intake is
550 mg/day for men, 425 mg for women). A multivitamin with 10-25 mg is a rounding
error against that gap. Biotin at 30-300 mcg is harmless; at 5,000-10,000 mcg —
common in hair/skin gummies — it interferes with streptavidin-biotin immunoassays
and can produce falsely low TSH and falsely normal troponin.

---

## Minerals

### Calcium

Calcium carbonate needs gastric acid and should be taken with food; calcium citrate
does not. A multivitamin supplies 100-300 mg, which is 8-23% of the 1,300 mg daily
value. It is a top-up for people who eat little dairy, not a treatment for
osteoporosis. The cardiovascular signal from calcium supplements is unsettled: a
2010 meta-analysis raised concern, but a 2023 meta-analysis of 11 trials found no
significant excess of MI, CHD, stroke or mortality. Either way, the doses in a
multi are far below the 1 g/day used in those trials.

### Iron

Iron is the nutrient where "more" is most often wrong. Most men and postmenopausal
women do not need supplemental iron; it causes constipation and nausea, and in
undiagnosed haemochromatosis it accumulates. The UL is 45 mg/day, and 18 mg in a
multivitamin is 40% of it.

Form matters mainly for tolerability. Ferrous sulfate is the reference treatment
but causes more GI effects; ferrous bisglycinate is similarly effective with fewer
symptoms. Carbonyl iron is safer in overdose, which matters in households with
young children, because iron poisoning is a leading cause of fatal supplement
ingestion in children under six.

A men's or 50+ formula without iron is a feature, not a gap.

### Magnesium

Magnesium oxide is about 4% absorbed, versus 9-11% for soluble salts such as
citrate, chloride, lactate and aspartate. It is the default in cheap multis
because it is compact and cheap. Glycinate is gentler on the gut; in the only
direct trial it matched oxide overall, with an advantage in severe malabsorption.
The supplemental UL is 350 mg/day, mostly because of diarrhoea.

A multivitamin with 20-100 mg of magnesium contributes little to a 400 mg
requirement. If magnesium is the goal, a dedicated product is more sensible.

### Zinc

Zinc oxide is cheap and less well absorbed; citrate, picolinate and bisglycinate
are better. At the 8-15 mg in most multis the difference is small. The important
issue is copper. Zinc induces metallothionein in enterocytes, which binds copper
and prevents its absorption; 50 mg/day for weeks can cause copper deficiency,
anaemia and neuropathy. The UL is 40 mg/day, and a formula supplying 25 mg zinc
should include 1-2 mg copper. Several "immune" multis supply 25-50 mg zinc with no
copper at all.

### Selenium, iodine, copper, manganese, chromium, molybdenum

- **Selenium.** Selenomethionine is incorporated into proteins and retained better
  than selenite. The UL is 400 mcg; 200 mcg is half of it, and supplementation at
  that level was associated with an 11% relative increase in type 2 diabetes in a
  meta-analysis of trials. There is no reason for a general multi to exceed 55-70
  mcg unless the population is selenium-deficient.
- **Iodine.** Potassium iodide is reliable; kelp is not, because iodine content
  varies by species, season and lot. The UL is 1,100 mcg, and prenatal products
  have been found to contain 88% more iodine than labelled. 150 mcg is the right
  order of magnitude for most adults.
- **Copper.** 0.5-1 mg is a sensible match for 10-25 mg zinc. The UL is 10 mg.
- **Manganese.** 2-4 mg is common and unnecessary; the UL is 11 mg.
- **Chromium.** No established UL and no reliable evidence of glycaemic benefit in
  people without deficiency. 35-400 mcg appears in products; the higher end is
  marketing, not pharmacology.
- **Molybdenum.** 45-90 mcg; deficiency is essentially unknown outside parenteral
  nutrition.

---

## Whole-food, "food-based" and synthetic

The claim is that vitamins grown in yeast, cultured on a food matrix or extracted
from plants are "recognised by the body" and better absorbed. The evidence does not
support a general advantage.

A 30-day single-blind randomised trial in 62 adults compared an organically sourced
multivitamin with a synthetic one. Circulating micronutrient changes were
comparable, with no significant between-group differences for any vitamin or
mineral. Smaller studies of fat-soluble vitamins extracted from foods show
comparable digestive recovery to synthetic forms.

What whole-food products do offer is a story, a shorter ingredient list in some
cases, and often a much higher price. What they often do not offer is dose: the
Garden of Life product in this sample supplies 2.5 mg iron, 3.9 mg zinc and no
calcium or magnesium, because the food matrix takes up tablet mass.

The one place "natural" genuinely matters is vitamin E potency (already reflected
on labels) and, arguably, folate forms. Everywhere else, the molecule is the
molecule.

---

## Gummies versus tablets versus capsules

Gummies are popular and usually fine for the nutrients they contain. Three caveats:

1. **They are less stable.** Nutrients degrade in a gelatin/pectin matrix, so
   manufacturers add overages. ConsumerLab has repeatedly found gummies with
   nearly double the labelled folate, and one review found a gummy with almost
   twice the labelled vitamin D.
2. **They cannot carry much.** Iron is usually absent because it tastes bad and is
   dangerous in a candy-like product. Minerals are token amounts. A gummy is
   typically a vitamin product with a little zinc.
3. **They carry sugar.** Two to three gummies usually contain 2-4 g of added sugar.

Bioequivalence studies sponsored by a gummy manufacturer found equivalent total
absorption (AUC and Cmax) of vitamin E, folate and B12 from gummies and tablets;
folate peaked earlier with the gummy. So the *absorption* is not the problem. The
formulation and the overage are.

Tablets are the cheapest way to deliver a large number of nutrients, but they can
fail to disintegrate. A USDA survey of 94 adult multivitamin samples found 92.6%
passed USP disintegration; all capsules passed and 7 of 77 tablets failed. A
coated tablet that does not break down delivers little. This is one reason a
third-party certification, which includes a disintegration test, is worth more
for tablets than for capsules.

Capsules cost more per dose and hold less, which is why premium capsules tend to
have fewer nutrients at higher doses rather than a long list.

---

## Reading a label in 60 seconds

1. **Serving size.** Two capsules, three gummies or a scoop changes the cost and
   the dose. Multiply.
2. **Vitamin D form and dose.** D3, and at least 25 mcg.
3. **Vitamin A form.** How much is preformed? Is it near 3,000 mcg?
4. **Iron.** Does this person need it? If not, choose a formula without it.
5. **Zinc and copper.** More than 15 mg zinc without copper is a design flaw.
6. **B6 and niacin.** Above 50 mg B6 or above 35 mg niacin deserves a second look.
7. **Folate form.** Folic acid or 5-MTHF are both acceptable; the dose and the
   reason matter more.
8. **Certification.** USP, NSF/ANSI 173, NSF Certified for Sport or Informed
   Choice/Sport.
9. **"Other ingredients."** Blends with no amounts are unverifiable. Count them as
   marketing until proven otherwise.
