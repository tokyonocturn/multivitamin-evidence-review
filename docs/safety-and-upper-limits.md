# Safety, upper limits and interactions

A standard multivitamin has an excellent safety record. In PHS II, 14,641 men took
Centrum Silver or placebo for a median of 11.2 years with no excess of serious
adverse events. COSMOS reported no safety concerns over 3.6 years. The risks in
this category are not "multivitamins are toxic"; they are specific ingredients at
specific doses in specific people, plus the arithmetic of stacking products.

The full datasets are in [`data/upper_limits.csv`](../data/upper_limits.csv) and
[`data/interactions.csv`](../data/interactions.csv); generated tables are in
[`docs/generated/upper-limits.md`](generated/upper-limits.md) and
[`docs/generated/interactions.md`](generated/interactions.md).

---

## What the upper limit means

The tolerable upper intake level (UL) is the highest daily intake likely to pose no
risk of adverse health effects in almost all people. It is not a target, and it is
not a toxicity threshold. It is a boundary derived from the most sensitive
endpoint — the first thing that goes wrong — usually with an uncertainty factor
applied.

Two consequences:

- Exceeding a UL once is not an emergency. Chronically exceeding it is a reason to
  change the product.
- Being below every UL does not make a product well designed. A formula can be
  under-dosed on vitamin D, over-dosed on zinc and missing copper, all while
  staying under every UL.

---

## The ingredients that actually cause harm

### Beta-carotene in smokers

The clearest harm signal in the entire supplement literature. In ATBC, 29,133 male
smokers took 20 mg/day of beta-carotene with or without vitamin E for 5-8 years;
lung cancer incidence was 18% higher. In CARET, 18,314 smokers, former smokers and
asbestos-exposed men took 30 mg/day beta-carotene plus 7,500 mcg RAE retinyl
palmitate; lung cancer incidence was 28% higher, lung cancer death 46% higher, and
all-cause mortality 17% higher. The trial stopped early.

Pooled across five trials, beta-carotene increased cardiovascular mortality
(OR 1.10, 95% CI 1.02-1.19). The effect appears at doses 10-30 times higher than
those in a multivitamin, and in high-risk populations. A multivitamin with 0.5-3 mg
of beta-carotene is not the same exposure. But a smoker choosing between a
beta-carotene-only "vitamin A" product and a mixed-carotenoid or lower-dose formula
should choose the latter, and should not take a high-dose beta-carotene supplement
at all.

### Vitamin E at high doses

The pooled trial evidence at usual supplement doses shows no mortality benefit
(OR 1.02, 0.97-1.07). An earlier meta-analysis found a small excess mortality at
400 IU/day or more, and SELECT found a 17% increase in prostate cancer with 400
IU/day of vitamin E. These are doses 10-20 times a multivitamin's 15-30 mg. The
practical rule: a multivitamin's vitamin E is not a concern; a standalone 400 IU
capsule taken for years is.

### Iron

Iron is essential and iron deficiency is common in menstruating women, pregnancy
and malabsorption. It is also the supplement most likely to harm people who do not
need it.

- **GI effects.** Constipation, nausea and dark stools are common at 18-65 mg.
- **Overload.** People with hereditary haemochromatosis, chronic liver disease or
  repeated transfusions absorb iron without regulation. Supplemental iron can
  accelerate organ damage.
- **Children.** Iron overdose is a leading cause of fatal poisoning in children
  under six. Prenatal and women's multis should be treated like medication.
- **UL.** 45 mg/day for adults.

A men's or 50+ formula without iron is sensible design. A woman who is still
menstruating may need it; a woman who is postmenopausal usually does not.

### Zinc and copper

Zinc is not very toxic acutely, but chronic high intake interferes with copper.
Doses of 50 mg/day for weeks reduce copper status; copper deficiency causes
anaemia, neutropenia and a myelopathy that can be mistaken for B12 deficiency. The
UL is 40 mg/day, set partly on this basis.

The design rule is simple: if zinc is above 15 mg, copper should be present at
roughly 1 mg per 15-25 mg zinc. Several "immune" formulas in the market supply
25-50 mg zinc with no copper.

### Vitamin B6

Pyridoxine is neurotoxic at high doses. The UL is 100 mg/day, based on sensory
peripheral neuropathy, and cases have been reported below it with prolonged use.
A 50-75 mg dose in a "high-potency" multi is half to three-quarters of the UL
before any other supplement. Stacking a B-complex on top is how people develop
numbness and unsteadiness that resolves only slowly after stopping.

### Niacin

Nicotinic acid causes prostaglandin-mediated flushing, which is uncomfortable but
harmless. The serious toxicity is hepatotoxicity at gram doses, sometimes with
fulminant failure. The UL is 35 mg/day for synthetic niacin. Niacinamide is better
tolerated but still appears at 50-80 mg in high-potency multis, above the UL.

### Vitamin A

Preformed retinol is teratogenic and hepatotoxic. The UL is 3,000 mcg RAE/day, and
it applies to pregnant women as well. High-dose retinol also increases hip fracture
risk in older adults in some observational data. Beta-carotene is not subject to
this UL, but has its own risk in smokers.

A multivitamin with 750-1,050 mcg RAE (mostly or partly beta-carotene) is well
within range. A product with 3,000 mcg of preformed retinol is at the UL before
food.

### Selenium

Selenosis — hair loss, nail brittleness, garlic breath, neuropathy — appears at
intakes above 400 mcg/day. More subtly, a meta-analysis of trials found that
200 mcg/day of selenium increased type 2 diabetes risk by 11% (RR 1.11, 1.01-1.22).
In a selenium-replete population, that is a reason not to take 200 mcg in a daily
multi.

### Calcium

Calcium supplements cause constipation and, at high doses, kidney stones. The
cardiovascular signal is contested: a 2010 meta-analysis suggested an increase in
MI, but a 2023 meta-analysis of 11 trials found no significant excess of MI, CHD,
stroke or mortality. A multivitamin's 100-300 mg is not the exposure those trials
tested (about 1 g/day).

### Folic acid

Folic acid at 1,000 mcg/day can mask the anaemia of B12 deficiency while
neurological damage progresses. It does not treat B12 deficiency; it hides it. This
is why the UL is 1,000 mcg and why B12 status matters in people at risk (older
adults, vegans, metformin users, pernicious anaemia).

A secondary signal: a small trial in men with colorectal adenomas found a
2.6-fold increase in prostate cancer with 1 mg/day folic acid (HR 2.63, 1.03-6.60,
n=643). It has not been replicated, and it is a reason not to take 1 mg without an
indication, not a reason to avoid 400 mcg in a prenatal vitamin.

### Water-soluble does not mean harmless

B6, niacin and vitamin C all have real toxicity at high doses. "Your body excretes
what it doesn't need" is true for the excess of a normal dose and false as a
general principle.

---

## Stacking: the arithmetic that catches people

The most common avoidable problem is not a bad product. It is three good products
taken together.

### Worked example 1: the "immune stack"

| Product | Vitamin D | Zinc | Vitamin C |
| --- | --- | --- | --- |
| Multivitamin | 25 mcg | 11 mg | 90 mg |
| Vitamin D3 capsule | 125 mcg (5,000 IU) | — | — |
| Zinc lozenge (4/day) | — | 40 mg | — |
| Vitamin C 1,000 mg | — | — | 1,000 mg |
| **Total** | **150 mcg (6,000 IU)** | **51 mg** | **1,090 mg** |
| **UL** | **100 mcg** | **40 mg** | **2,000 mg** |

Vitamin D is 150% of the UL and zinc is 128%. Neither is immediately dangerous —
vitamin D toxicity generally requires sustained intakes above 10,000 IU — but this
is a stack that should be deliberate, monitored and time-limited, not an everyday
routine.

### Worked example 2: the "high-potency" overlap

A Thorne Basic Nutrients 2/Day (niacin 80 mg, B6 20 mg) plus a B-complex with
50 mg B6 and 50 mg niacin gives 100 mg B6 and 130 mg niacin. B6 is at the UL;
niacin is 3.7 times it. Add a "stress" formula with another 50 mg B6 and the
person is at 150 mg — the range where neuropathy appears.

### Worked example 3: iron plus calcium plus levothyroxine

A multivitamin with 18 mg iron and 200 mg calcium, taken with levothyroxine,
reduces levothyroxine absorption. The fix is timing, not avoidance: levothyroxine
on an empty stomach, at least four hours before the multivitamin. The same rule
applies to tetracycline and quinolone antibiotics, which chelate calcium, iron,
magnesium and zinc.

---

## Drug interactions worth knowing

| Drug | Interaction | Action |
| --- | --- | --- |
| Warfarin | Vitamin K changes INR; high-dose vitamin E and vitamin C may add bleeding risk | Keep vitamin K intake stable; tell the anticoagulation service before switching products |
| Levothyroxine | Calcium, iron and magnesium reduce absorption | Separate by 4 hours |
| Tetracyclines, quinolones | Minerals chelate the antibiotic | Separate by 2-6 hours per labelling |
| Proton pump inhibitors | Reduce food-bound B12 and iron absorption | Crystalline B12 in a multi is absorbed; monitor B12 and iron |
| Metformin | Lowers B12 status | Measure B12 periodically; a multi may prevent but not treat deficiency |
| Methotrexate | Folate antagonism is therapeutic | Do not add high-dose folate without oncology guidance |
| Isotretinoin/acitretin | Additive retinoid toxicity | Avoid preformed vitamin A supplements |
| Laboratory immunoassays | High-dose biotin causes false results | Stop 48-72 hours before tests; tell the lab |

Nutrient-nutrient interactions matter too: calcium and iron compete, iron at 25 mg
or more reduces zinc absorption, and zinc at 50 mg or more reduces copper. A
well-designed multivitamin avoids putting therapeutic doses of competing minerals
in the same pill, which is one argument for a moderate-dose multi plus targeted
single nutrients rather than a "everything at maximum" formula.

---

## Contamination and label accuracy

Independent testing finds problems in roughly one quarter to one third of
multivitamins:

- **ConsumerLab 2026:** 7 of 22 products (32%) failed. One contained 11.8% of its
  claimed vitamin A; some contained up to four times the labelled folate or zinc;
  one had almost twice the labelled vitamin D.
- **ConsumerLab 2025:** 8 of 29 (27.6%) failed. Three gummies had nearly double the
  labelled folic acid; a prenatal had 88% more iodine than labelled; one product
  had 14% of its expected vitamin D; one tablet failed disintegration.
- **USDA disintegration survey:** 92.6% of 94 samples passed USP disintegration;
  all capsules passed, 7 of 77 tablets failed.
- **Prenatal heavy-metal survey (2025):** across 47 products, lead was detectable
  in 68%, cadmium in 62% and arsenic in 15%, but none exceeded USP permitted daily
  exposure limits. Iodine was under-labelled by more than 20% in 80% of the
  products that declared it.

The pattern is consistent: most products are fine, a minority are not, and the
failures are not predictable from price or brand size. Certification reduces but
does not eliminate the risk, because it tests a lot, not every lot.

What certification means:

- **USP Verified** — identity, potency, purity, dissolution and manufacturing
  review, with random off-shelf testing.
- **NSF/ANSI 173** — contaminant and label-content testing for dietary supplements.
- **NSF Certified for Sport** — the above plus banned-substance screening.
- **Informed Choice / Informed Sport** — banned-substance screening, batch-based.
- **USDA Organic, Non-GMO Project** — production-method claims, not purity or
  potency.

A seal does not mean the formula is good. It means the bottle contains what it says
it contains. Those are different questions.

---

## Special populations

- **Pregnancy.** Folic acid 400-800 mcg before conception and through the first
  trimester reduces neural tube defects by about 72%. Avoid preformed vitamin A
  above 3,000 mcg RAE and avoid high-dose beta-carotene. Iodine 150 mcg is
  recommended in many guidelines. Iron needs rise; 27 mg is a common prenatal dose.
- **Older adults.** Lower gastric acid reduces calcium carbonate, iron and
  food-bound B12 absorption. Citrate, bisglycinate and crystalline B12 are better
  choices. Kidney function declines, so high-dose magnesium and potassium deserve
  caution.
- **Chronic kidney disease.** Potassium, magnesium, phosphorus and some
  fat-soluble vitamins accumulate. Multis should be chosen with a nephrologist;
  standard products are not designed for this.
- **Liver disease.** Avoid high-dose niacin and preformed vitamin A.
- **Haemochromatosis.** Avoid iron, including in "general" multis.
- **Bariatric surgery.** Lifelong MVM is standard of care, often at higher doses
  with iron, B12, D and calcium, in forms that are absorbed after the anatomy has
  changed.
- **Children.** Adult multis are not children's products. Iron overdose is
  particularly dangerous. Keep all supplements out of reach.
- **Pets.** Human multis contain xylitol in some gummies and doses of vitamin D and
  iron that are toxic to dogs and cats. Do not give human supplements to animals.

---

## When to seek advice

- You take warfarin, levothyroxine, methotrexate, isotretinoin, or an antibiotic
  from the tetracycline/quinolone class.
- You have kidney, liver or thyroid disease, haemochromatosis, or a history of
  kidney stones.
- You are pregnant, planning pregnancy, or breastfeeding.
- You have unexplained fatigue, neuropathy, anaemia, or bruising — these are
  findings to investigate, not to self-treat with a multivitamin.
- You are considering doses above the UL, or stacking multiple products with
  overlapping nutrients.
