# Brand and product comparison

This is a guide to the data in [`data/products.csv`](../data/products.csv) and the
generated tables in
[`docs/generated/product-comparison.md`](generated/product-comparison.md). It is
not a ranking of brands by health benefit, because the health benefit of a
multivitamin is small and largely independent of brand. It is a ranking by **what
you actually get for the money**, with quality signals where they exist.

Prices are US retail snapshots from 18 November 2026. They move.

---

## What the sample shows

| Metric | Value |
| --- | --- |
| Products | 20 |
| Cost range | $0.05 to $3.30 per daily serving |
| Ratio | 70x |
| Median | $0.28 |
| Third-party certified | 6 of 20 |
| Cheapest certified | Nature Made Multi Complete with Iron, $0.11 |
| Cheapest overall | Kirkland Signature Daily Multi, $0.05 |
| Most expensive | AG1, $3.30 |

The cost spread is the single most striking finding. The most expensive product
costs 70 times the cheapest, and the difference is not explained by superior
ingredients, certification, or evidence. It is explained by format (powder versus
tablet), marketing, and unquantified blends.

---

## Value tiers

### Budget: under $0.15 per serving

**Kirkland Signature Daily Multi — $0.05.** 400 tablets, 25 nutrients, 18 mg iron,
400 IU vitamin D. The vitamin D dose is outdated, the iron is unnecessary for many
buyers, and no certification is documented. It is still an enormous amount of
vitamin per dollar.

**One A Day Women's Complete — $0.09.** Iron 18 mg, folate 400 mcg, D 25 mcg. A
reasonable women's formula at a mass-market price.

**Centrum Adults — $0.10.** 18 mg iron, D 25 mcg, B12 6 mcg. The default general
multi.

**One A Day Men's Complete — $0.10.** No iron, D 25 mcg, magnesium 120 mg, zinc
11 mg. One of the better mass-market men's formulas.

**Centrum Silver Adults 50+ — $0.11.** D 25 mcg, B12 25 mcg, no iron, 28 nutrients.
A sensible 50+ default.

**Nature Made Multi Complete with Iron — $0.11, USP Verified.** 23 nutrients,
D 25 mcg, 18 mg iron. The cheapest certified product in the sample. For a person
who wants a general multi and does need iron, this is the value pick.

**Centrum Silver Women 50+ — $0.11.** 8 mg iron, D 25 mcg, B12 50 mcg, calcium
300 mg.

**One A Day Men's/Women's 50+ — $0.12.** Higher zinc (24 mg), selenium and
chromium; no iron. The zinc dose is 60% of the UL, which is a design choice worth
noticing.

### Mid: $0.15-$0.50

**Centrum Women MultiGummies — $0.26.** A gummy with 2 g sugar, no iron, no
magnesium, 2.5 mg zinc. Convenient, not comprehensive.

**Life Extension One-Per-Day — $0.31.** High-potency B vitamins (B6 75 mg, niacin
50 mg), 50 mcg D, 200 mcg selenium, no calcium or vitamin K. It exceeds the niacin
UL by design and approaches the B6 UL. Good for people who want high B vitamins;
bad for people who stack.

### Premium: $0.50-$1.50

**Opti-Men — $0.60.** Three tablets per day. Vitamin A 3,000 mcg, niacin 75 mg,
B6 50 mg, vitamin E 134 mg. This is a megadose product: it hits the vitamin A UL
and more than doubles the niacin UL. The "amino acid blend" is not quantified.

**Garden of Life mykind Organics Women's Once Daily — $0.67.** USDA Organic,
whole-food matrix, 2.5 mg iron, 3.9 mg zinc, no calcium or magnesium. The organic
seal is a production claim, not a purity certification. You are paying for the
story and the food blend more than for dose.

**Pure Encapsulations O.N.E. — $0.81.** 50 mcg D, 500 mcg B12, 25 mg zinc citrate,
5-MTHF, CoQ10 50 mg, lutein 3 mg. No calcium or magnesium, no certification
documented. A well-designed capsule for people who want activated B vitamins and
antioxidants.

**SmartyPants Women's Multi & Omegas — $1.10.** Three gummies, 3 g sugar, NSF
Contents Certified, 50 mcg D, methylfolate, 4 mg zinc, DHA 55 mg. The best-evidenced
gummy format in the sample, but still a gummy: low minerals, added sugar, overage
risk.

**Ritual Essential for Women/Men 18+ — $1.25.** Nine nutrients, 50 mcg D, 5-MTHF,
methylcobalamin, 90 mcg K2, DHA 330 mg, iron 8 mg (women) or zinc 11 mg (men).
USP Verified. Deliberately minimal, transparent sourcing, expensive per nutrient.

**Thorne Basic Nutrients 2/Day — $1.33.** NSF Certified for Sport, 25 nutrients,
50 mcg D, 5-MTHF, methylcobalamin, 200 mcg K1 + 200 mcg MK-4, 200 mcg selenium,
niacin 80 mg, B6 20 mg. The most complete premium formula in the sample, with a
niacin dose that exceeds the UL.

### Very expensive: above $1.50

**Huel Daily Greens — $2.00.** A greens powder with a full vitamin profile,
46 mcg D, 126 mcg MK-7, 2.7 g of blends. It is a multivitamin plus fibre and
powdered vegetables, at eight times the cost of a tablet that delivers similar
vitamins.

**AG1 — $3.30.** 555 mcg vitamin A, 420 mg C, 83 mg E, 20 mg niacin, 680 mcg
folate, 22 mcg B12, 15 mg zinc, 26 mg magnesium, no vitamin D, 1 mg iron, and
7.4 g of unquantified blends. It is the most expensive product in the sample and
not the most complete. The premium is for the powder, the probiotics and the
marketing, not for the vitamin content.

---

## What certification is worth

Six of 20 products carry a third-party certification. The certified group's median
cost is higher, but the cheapest certified product ($0.11) is cheaper than most
uncertified ones.

| Certification | What it verifies | What it does not |
| --- | --- | --- |
| USP Verified | Identity, potency, purity, dissolution, GMP | Efficacy, formula quality |
| NSF/ANSI 173 | Label content, contaminants | Efficacy |
| NSF Certified for Sport | Above plus banned substances | Efficacy |
| Informed Choice/Sport | Banned substances, batch testing | Full label accuracy |
| USDA Organic | Production method | Purity, potency |
| Non-GMO Project | Genetic material | Anything about vitamins |

For tablets, certification also covers disintegration, which matters: 7 of 77
tablets failed USP disintegration in a USDA survey. For capsules, the risk is
lower. For gummies, the main risk is overage, which certification may catch in the
tested lot but not in every lot.

---

## Red flags in the sample

| Product | Flag | Why it matters |
| --- | --- | --- |
| Thorne Basic Nutrients 2/Day | Niacin 80 mg (229% UL) | Above the UL; flushing and, at higher doses, liver risk |
| Opti-Men | Niacin 75 mg, vitamin A 3,000 mcg, B6 50 mg, 3 tablets | Multiple nutrients at or above ULs; megadose design |
| Life Extension One-Per-Day | Niacin 50 mg, B6 75 mg | Above niacin UL, 75% of B6 UL |
| One A Day Men's/Women's 50+ | Zinc 24 mg | 60% of UL; copper present (2.2 mg), which mitigates |
| Pure Encapsulations O.N.E. | Zinc 25 mg, no copper | 62% of UL without the copper that zinc displaces |
| Garden of Life mykind | 2.5 mg iron, 3.9 mg zinc, no calcium/magnesium | Whole-food matrix displaces minerals |
| Centrum Women MultiGummies | 2.5 mg zinc, no iron, no magnesium, 2 g sugar | A vitamin gummy, not a mineral multi |
| AG1 | No vitamin D, 7.4 g unquantified blends | Incomplete for the price; blends unverifiable |
| Kirkland Daily Multi | 400 IU vitamin D | Outdated dose |
| All iron-containing general multis | 18 mg iron | Unnecessary for most men and postmenopausal women |

---

## How to choose, by situation

**If you want the cheapest adequate general multi:** Kirkland ($0.05) or Centrum
Adults ($0.10). Add a separate D3 if 400 IU is too low.

**If you want the cheapest certified multi:** Nature Made Multi Complete with Iron
($0.11, USP). Choose an iron-free certified product if you do not need iron.

**If you are a man or postmenopausal woman:** One A Day Men's Complete ($0.10,
iron-free) or Centrum Silver 50+ ($0.11, iron-free).

**If you are a menstruating woman:** One A Day Women's Complete ($0.09, 18 mg iron)
or Nature Made with Iron ($0.11, USP). Check ferritin before assuming you need
iron.

**If you are pregnant:** a dedicated prenatal with 400-800 mcg folic acid, 150 mcg
iodine, 27 mg iron, D3 and choline. Do not use a general adult multi as a prenatal.

**If you want activated B vitamins and a premium capsule:** Pure Encapsulations
O.N.E. ($0.81) or Thorne ($1.33, NSF Sport). Watch the niacin.

**If you want a gummy:** SmartyPants ($1.10, NSF) is the best-evidenced in the
sample, but pair it with a separate iron and calcium source if you need them.

**If you want a greens powder:** understand that you are buying a multivitamin
plus powdered plants at 8-30 times the cost of the vitamins alone. AG1 is not a
complete multi (no vitamin D) and its blends are unquantified.

**If you want the most nutrients per dollar:** a cheap tablet wins by an order of
magnitude. There is no evidence that the premium formats produce better health
outcomes.

---

## What not to pay for

- **"Whole food" or "food-grown" vitamins.** No demonstrated absorption advantage;
  often lower mineral doses.
- **Proprietary blends.** If the amount is not disclosed, it cannot be evaluated.
- **"Methylated" everything.** 5-MTHF and methylcobalamin are reasonable choices,
  not proven superior for the general population.
- **K2 in a multivitamin.** No outcome evidence at these doses; a problem for
  warfarin patients.
- **Antioxidant extras (CoQ10, alpha-lipoic acid, lycopene, grape seed).** Token
  doses, no outcome evidence in a multi, higher price.
- **"Energy" or "stress" branding.** B vitamins do not provide energy; adaptogens
  in a multivitamin are unquantified and unproven.
- **Subscription convenience.** It is the same tablet at a higher annual cost if
  you do not use it.
