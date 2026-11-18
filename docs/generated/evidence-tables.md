# Evidence tables

Generated from `data/evidence.csv`. Effect estimates are as reported by the cited source; `CI` is the 95% interval unless the source states otherwise. Certainty uses GRADE logic and is separate from clinical importance.

## Outcomes

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| mvm-allcause-mortality | Does a daily multivitamin reduce all-cause mortality? | 0.94 (0.87-1.01) | Moderate | Established |
| mvm-cvd-mortality | Does a daily multivitamin reduce cardiovascular mortality? | 0.94 (0.83-1.06) | Moderate | Established |
| mvm-cvd-events | Does a daily multivitamin prevent cardiovascular events? | 1.02 and 0.98 (0.92-1.13 and 0.86-1.12) | High | Established |
| mvm-cancer-incidence | Does a daily multivitamin reduce total cancer incidence? | 0.93 (0.87-0.99) | Moderate | Established |
| mvm-cancer-mortality | Does a daily multivitamin reduce cancer mortality? | 0.94 (0.81-1.09) | Low | Established |
| mvm-lung-cancer | Does a daily multivitamin reduce lung cancer incidence? | 0.75 (0.58-0.95) | Low | Emerging |
| phs2-total-cancer | What did the largest long-term multivitamin trial find for cancer? | 0.92 (0.86-0.998) | Moderate | Established |
| phs2-cvd | What did PHS II find for cardiovascular events? | 1.02 (0.92-1.13) | High | Established |
| cosmos-cancer | Does a modern multivitamin reduce cancer in the largest recent trial? | 0.97 (0.86-1.09) | High | Established |
| cosmos-mortality | Does a modern multivitamin reduce mortality in COSMOS? | 0.93 (0.81-1.08) | Moderate | Established |
| cohort-mortality | Is habitual multivitamin use associated with lower mortality in cohort data? | 1.04 (1.02-1.07) | Low | Established |
| suvimax-cancer | Did the French antioxidant trial reduce cancer? | 0.90 overall; 0.69 men; 1.04 women (0.76-1.06 overall; 0.53-0.91 men) | Low | Mixed |
| suvimax-mortality | Did SU.VI.MAX reduce mortality? | 0.77 overall; 0.63 men (0.57-1.00 overall; 0.42-0.93 men) | Low | Mixed |
| linxian-mortality | Do multivitamins help in a nutritionally deficient population? | 0.91 (0.84-0.99) | Moderate | Established |
| linxian-longterm | Does the Linxian mortality benefit persist? | 0.94 overall (NS) (0.85-1.04) | Low | Mixed |

Interpretation:

- **mvm-allcause-mortality** — Confidence interval crosses 1; the three largest trials dominate. COSMOS alone HR 0.93 (0.81-1.08).
- **mvm-cvd-mortality** — No benefit; estimate consistent across trials.
- **mvm-cvd-events** — PHS II HR 1.02; COSMOS HR 0.98. Neither trial found benefit on any CVD component.
- **mvm-cancer-incidence** — Statistically significant but fragile: PHS II HR 0.92 (0.86-0.998), COSMOS HR 0.97 (0.86-1.09), SU.VI.MAX RR 0.90 (0.76-1.06). Absolute risk difference -0.2% to -1.2%.
- **mvm-cancer-mortality** — No statistically significant reduction. PHS II cancer mortality HR 0.88 (0.77-1.01).
- **mvm-lung-cancer** — COSMOS HR 0.62 (0.42-0.92); absolute difference about 0.2%. Only two trials, both in mostly white older populations.
- **phs2-total-cancer** — Benefit confined to men with a baseline cancer history (HR 0.73) and to non-prostate cancers (HR 0.88); no effect on cancer death.
- **phs2-cvd** — No effect on MI, stroke, or CVD death. MI death HR 0.56 was a subgroup finding with wide CI.
- **cosmos-cancer** — Null for total cancer; breast HR 1.06; colorectal HR 1.30 (0.80-2.12); lung HR 0.62.
- **cosmos-mortality** — No significant effect; trial not powered for mortality and follow-up was short.
- **cohort-mortality** — Observational and confounded, but the direction is opposite to the marketing claim. Time-varying analysis consistent.
- **suvimax-cancer** — Five-ingredient antioxidant mixture, not a broad multivitamin. Significant sex interaction; not replicated.
- **suvimax-mortality** — Overall estimate borderline; apparent benefit restricted to men.
- **linxian-mortality** — Benefit limited to the beta-carotene + vitamin E + selenium arm; not a broad multivitamin, and not generalisable to well-nourished populations.
- **linxian-longterm** — No overall mortality effect at 35 years; heart disease and stroke mortality lower in older men.

## Cognition

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| cosmos-mind-global | Does a multivitamin improve global cognition in older adults? | +0.07 (0.02-0.12) | Moderate | Established |
| cosmos-meta-cognition | Do the three COSMOS cognitive substudies agree? | +0.07 global; +0.06 memory (0.03-0.11; 0.03-0.10) | Moderate | Established |
| cosmos-web-memory | Does a multivitamin improve memory recall? | +0.71 vs +0.44 words (Not reported) | Moderate | Established |
| phs2-cognition | Does long-term multivitamin use prevent cognitive decline in men? | -0.01 (-0.04 to 0.02) | High | Established |
| cognition-meta-older | What does the broader trial literature show for cognition? | 0.09 delayed recall; null other domains (0.05-0.13) | Low | Emerging |

Interpretation:

- **cosmos-mind-global** — Statistically significant; about 0.07 SD, roughly 2 years less cognitive aging. Larger in those with CVD history.
- **cosmos-meta-cognition** — Consistent direction across telephone, web and in-person assessments; all from one trial population.
- **cosmos-web-memory** — About 0.27 words, equivalent to 3.1 years of age-related memory change by cross-sectional calibration.
- **phs2-cognition** — Null. The contrast with COSMOS may reflect population, dose, duration or chance.
- **cognition-meta-older** — Small effect concentrated in one domain; heterogeneous supplements.

## Immunity

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| mvm-infections-elderly | Do multivitamins prevent infection in older people? | Little evidence of benefit (Not pooled) | Low | Mixed |
| mvm-nursing-home | Do multivitamins reduce infections in nursing homes? | 0.92 (0.82-1.03) | Moderate | Established |
| mvm-diabetes-infection | Do multivitamins reduce infection in people with type 2 diabetes? | Fewer infection days (Not reported) | Low | Emerging |
| mvm-ari-symptoms | Do multivitamins reduce acute respiratory infection symptoms? | No reduction in incidence; possible symptom benefit (Not pooled) | Low | Mixed |

Interpretation:

- **mvm-infections-elderly** — Evidence poor to moderate quality, heterogeneous and conflicting; no support for routine use in all older people.
- **mvm-nursing-home** — Null overall; post hoc benefit in residents without dementia (RR 0.81).
- **mvm-diabetes-infection** — Small trial; benefit concentrated in participants with diabetes. Not replicated at scale.
- **mvm-ari-symptoms** — Insufficient evidence for COVID-19 prevention or treatment.

## Energy

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| mvm-fatigue | Do multivitamins improve energy or fatigue in non-deficient adults? | No association (Not significant) | Low | Established |

Interpretation:

- **mvm-fatigue** — No benefit in prospective data; B-vitamin 'energy' claims depend on correcting a deficiency.

## Cardiovascular

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| mvm-bp | Do multivitamins lower blood pressure? | Small reduction (Not pooled here) | Low | Emerging |

Interpretation:

- **mvm-bp** — Signal in at-risk groups; not a treatment for hypertension.

## Eyes

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| mvm-amd-progression | Could multivitamin use worsen AMD progression? | Higher risk reported (Not pooled here) | Very low | Emerging |
| areds-progression | Do high-dose antioxidant formulas slow AMD progression? | 0.72 (0.58-0.90) | Moderate | Established |
| areds2-lutein | Is lutein/zeaxanthin a safer substitute for beta-carotene? | 0.90 (NS primary) (0.76-1.07) | Moderate | Mixed |

Interpretation:

- **mvm-amd-progression** — Unexpected finding in a rapid review; contradicted by AREDS evidence for high-dose antioxidant formulas. Treat as hypothesis, not established harm.
- **areds-progression** — About 78 fewer progressions per 1,000 people with intermediate AMD. Formula is not a standard multivitamin: 500 mg C, 400 IU E, 80 mg zinc, 2 mg copper.
- **areds2-lutein** — Primary analysis not significant; secondary analyses favoured lutein/zeaxanthin, especially in non-smokers.

## Safety

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| beta-carotene-lung | Does high-dose beta-carotene increase lung cancer risk in smokers? | 1.18 and 1.28 (1.03-1.36; 1.04-1.57) | High | Established |
| beta-carotene-cvd | Does beta-carotene increase cardiovascular mortality? | 1.10 (1.02-1.19) | Moderate | Established |
| vitamin-e-mortality | Does vitamin E supplementation affect mortality? | 1.02 (0.97-1.07) | High | Established |
| vitamin-e-prostate | Does vitamin E increase prostate cancer risk? | 1.17 (1.004-1.36) | Moderate | Established |
| selenium-diabetes | Does selenium supplementation increase type 2 diabetes risk? | 1.11 (1.01-1.22) | Low | Emerging |
| calcium-cvd | Do calcium supplements increase cardiovascular risk? | No significant excess (1.15 (0.88-1.51) for MI) | Moderate | Established |
| folic-acid-masking | Can folic acid mask vitamin B12 deficiency? | Masks anaemia while neuropathy progresses (Not pooled) | Moderate | Established |
| folic-acid-prostate | Does high-dose folic acid increase prostate cancer risk? | 2.6-fold increase (1.03-6.60) | Low | Emerging |
| iron-ul | What is the safe upper limit for iron and who is at risk? | 45 mg/day UL (Not applicable) | High | Established |
| zinc-copper | Does high zinc intake impair copper status? | 50 mg/day for weeks lowers copper (Not pooled) | Moderate | Established |
| b6-neuropathy | Can vitamin B6 cause neuropathy? | Reports above 100 mg/day; some below (Not pooled) | Moderate | Established |
| niacin-ul | What are the risks of high-dose niacin? | UL 35 mg/day for synthetic niacin (Not applicable) | High | Established |
| vitamin-a-teratogenic | What is the safe upper limit for preformed vitamin A? | 3000 mcg RAE/day (Not applicable) | High | Established |
| vitamin-k-warfarin | Does vitamin K in a multivitamin interfere with warfarin? | Clinically significant interaction (Not pooled) | High | Established |
| biotin-lab | Does biotin interfere with laboratory tests? | Interference at high doses (Not pooled) | Moderate | Established |

Interpretation:

- **beta-carotene-lung** — Effect appears with 20-30 mg/day; risk persists after stopping in CARET women. Relevant to 'vegetarian' multis that use beta-carotene as the only vitamin A.
- **beta-carotene-cvd** — Absolute risk difference -0.8% to 0.8% across trials.
- **vitamin-e-mortality** — No benefit. An earlier meta-analysis found a small excess at doses of 400 IU/day or more; that signal is not confirmed in the largest pooled analyses.
- **vitamin-e-prostate** — SELECT: 17% relative increase with 400 IU/day vitamin E. A reason to avoid high-dose E, not standard multivitamin doses.
- **selenium-diabetes** — Small relative increase; relevant to 200 mcg selenium in some multis and to people already selenium-replete.
- **calcium-cvd** — Earlier meta-analysis raised concern; the larger 2023 analysis found no significant hazard. Calcium in a multivitamin is far below trial doses.
- **folic-acid-masking** — Relevant at 1,000 mcg/day folic acid; less likely with 5-MTHF, though not proven to eliminate the risk.
- **folic-acid-prostate** — Small trial, unexpected secondary finding; not confirmed. A reason to avoid 1 mg folic acid without an indication.
- **iron-ul** — Iron in a multivitamin is unnecessary for most men and postmenopausal women; harmful in undiagnosed haemochromatosis.
- **zinc-copper** — UL 40 mg/day. Many 'immune' multis supply 25-50 mg zinc without copper.
- **b6-neuropathy** — UL 100 mg/day. Several 'high-potency' multis supply 50-75 mg.
- **niacin-ul** — Niacinamide is better tolerated but still exceeds the UL in several high-potency multis (50-80 mg).
- **vitamin-a-teratogenic** — Beta-carotene is not subject to this UL, but high-dose beta-carotene has its own risk in smokers.
- **vitamin-k-warfarin** — Small stable amounts (10-25 mcg) are usually tolerated; sudden changes are the danger. K2 MK-7 has a longer half-life and is harder to manage.
- **biotin-lab** — Relevant to 5,000-10,000 mcg hair/skin gummies more than to standard multis (30-300 mcg).

## Pregnancy

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| folic-acid-ntd | Does periconceptional folic acid prevent neural tube defects? | 72% reduction (Relative risk 0.28) | High | Established |
| mvm-pregnancy-paediatric-cancer | Does maternal multivitamin use affect childhood cancer risk? | Reduced risk reported (Not pooled) | Very low | Emerging |

Interpretation:

- **folic-acid-ntd** — The strongest evidence in the entire multivitamin literature. 400-800 mcg/day before conception and through the first trimester.
- **mvm-pregnancy-paediatric-cancer** — Observational-dominated; confounding by indication and diet is likely.

## Interactions

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| levothyroxine-minerals | Do minerals in a multivitamin reduce levothyroxine absorption? | Calcium and iron bind levothyroxine (Not pooled) | High | Established |
| ppi-b12 | Do proton pump inhibitors cause B12 deficiency? | Reduced food-bound B12 absorption (Not pooled) | Moderate | Established |
| metformin-b12 | Does metformin lower vitamin B12? | Modest reduction (Not pooled) | Moderate | Established |

Interpretation:

- **levothyroxine-minerals** — Separate by at least 4 hours.
- **ppi-b12** — Supplemental crystalline B12 is absorbed without gastric acid, so a multivitamin can help here.
- **metformin-b12** — Periodic B12 measurement is reasonable; a multivitamin containing B12 may be insufficient if deficient.

## Quality

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| mvm-label-accuracy | How often do multivitamins fail independent testing? | 32% not approved (Not applicable) | Moderate | Established |
| gummy-overage | Are gummies more likely to contain excess nutrients? | 3 gummies near double folate (Not applicable) | Moderate | Established |
| tablet-disintegration | Do multivitamin tablets always dissolve? | 92.6% pass (Not applicable) | Moderate | Established |
| heavy-metals-prenatal | Do prenatal multivitamins contain heavy metals? | Lead in 68%; none above USP limits (Not applicable) | Moderate | Established |

Interpretation:

- **mvm-label-accuracy** — Failures included 11.8% of claimed vitamin A, four times claimed folate or zinc, and a tablet that failed disintegration.
- **gummy-overage** — Nutrient instability in gummies leads manufacturers to add large overages; some exceed the UL.
- **tablet-disintegration** — All capsules passed; 7 of 77 tablets failed. A coated tablet that does not dissolve delivers little.
- **heavy-metals-prenatal** — Detectable is not unsafe. The finding argues for certified products and against unbounded 'greens' blends.

## Forms

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| whole-food-vs-synthetic | Are whole-food vitamins better absorbed than synthetic? | No significant difference (Not reported) | Low | Established |
| gummy-vs-tablet-bioequivalence | Are gummies bioequivalent to tablets? | Bioequivalent for AUC/Cmax (Not reported) | Low | Established |
| folate-forms-equivalent | Is 5-MTHF better absorbed than folic acid? | Equivalent at equal doses; 5-MTHF may raise plasma folate slightly more (Not reported) | Moderate | Established |
| vitamin-d2-vs-d3 | Is vitamin D3 better than D2 at raising 25(OH)D? | D3 raised total 25(OH)D more; D2 lowered 25(OH)D3 (Significant) | Moderate | Established |
| natural-vs-synthetic-e | Is natural vitamin E more potent than synthetic? | Natural about 2x labelled activity; 1.36x by some estimates (Not applicable) | High | Established |
| b12-forms | Is methylcobalamin better than cyanocobalamin? | All forms raise B12; no consistent clinical difference (Not reported) | Moderate | Established |
| magnesium-oxide-absorption | Is magnesium oxide absorbed? | About 4% vs 9-11% for soluble salts (Not reported) | Moderate | Established |
| zinc-forms | Are chelated zinc forms better absorbed than oxide? | Chelates and citrate modestly better; differences small at 10-15 mg (Not reported) | Low | Emerging |
| iron-bisglycinate | Is iron bisglycinate better tolerated than ferrous sulfate? | Similar efficacy, fewer GI effects (Not reported) | Moderate | Established |
| calcium-carbonate-vs-citrate | Is calcium citrate better absorbed than carbonate? | Citrate better without food or with acid suppression (Not reported) | Moderate | Established |

Interpretation:

- **whole-food-vs-synthetic** — Organic-sourced and synthetic multis produced comparable changes. Whole-food multis cost more for the same actives.
- **gummy-vs-tablet-bioequivalence** — Folate peaked earlier with gummies; total absorption was equivalent. Industry-funded.
- **folate-forms-equivalent** — Both work. 5-MTHF avoids unmetabolised folic acid and is preferable in MTHFR TT, but the clinical difference is unproven.
- **vitamin-d2-vs-d3** — Use D3 in a multivitamin. D2 is acceptable but less potent at the same dose.
- **natural-vs-synthetic-e** — Labels use mg alpha-tocopherol, which already accounts for the difference; dl-alpha is not 'fake', just less potent per mg.
- **b12-forms** — Cyanocobalamin is cheap, stable and effective. Methylcobalamin matters mainly for the rare patient who cannot convert cyanocobalamin.
- **magnesium-oxide-absorption** — Most multis use oxide because it is compact and cheap. It still contributes magnesium, just less per mg.
- **zinc-forms** — Form matters less than dose and copper balance in a multivitamin.
- **iron-bisglycinate** — Relevant to prenatal and women's multis; 18-27 mg elemental iron is common.
- **calcium-carbonate-vs-citrate** — A multivitamin's 200-300 mg calcium is a supplement to diet, not a treatment for osteoporosis.

## Deficiency

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| mvm-deficiency-correction | Does a multivitamin correct low micronutrient status? | Raises status in deficient individuals (Not pooled) | Moderate | Established |
| mvm-food-insecure | Do multivitamins help people with poor diet quality? | Improves intake adequacy (Not pooled) | Low | Emerging |
| mvm-bariatric | Are multivitamins required after bariatric surgery? | Standard of care (Not pooled) | High | Established |

Interpretation:

- **mvm-deficiency-correction** — The clearest mechanistic case: a multivitamin is a delivery vehicle for nutrients a person is not getting.
- **mvm-food-insecure** — Benefit scaled to the size of the dietary gap; not a substitute for food.
- **mvm-bariatric** — Sleeve and bypass patients need lifelong MVM, often at higher doses with iron, B12, D and calcium.

## Cost

| ID | Question | Result | Certainty | Status |
| --- | --- | --- | --- | --- |
| mvm-cost | What does a daily multivitamin cost? | $0.05 to $3.30 per serving (Not applicable) | Not graded | Established |

Interpretation:

- **mvm-cost** — A 66-fold spread. The cheapest certified products cost less than one-tenth of the most expensive powders.
