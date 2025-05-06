---

# 🧭 Step-by-Step AI Prompt Sequence for RRI Calculation

---

## 🔹 **Step 1: Load Player Profile**

```markdown
Load and display player information for RRI evaluation.

Input:
- Player Name
- Team
- xSTATx_ID
- Age
- Role (Closer, Setup, HL, Mid, Mop-Up)
- Previous RRI Score

Return: formatted profile summary.
```

---

## 🔹 **Step 2: Calculate Performance Score (30%)**

```markdown
Using the following inputs:
- ERA, xFIP, WHIP, K/9, BB/9, K-BB%

Calculate a weighted Performance Score:
- ERA and xFIP = 10% each (scale: ERA < 3.00 = elite, 5.00+ = penalty)
- WHIP = 5% (inverse scaled)
- K/9 and BB/9 = 5% combined (reward high K/9 and low BB/9)
- K-BB% = 10% (bucketed, 30%+ = strong bonus)

Return: `Performance_Score` with individual breakdowns.
```

---

## 🔹 **Step 3: Calculate Leverage & Usage Score (20%)**

```markdown
Using:
- aLI (14-day average), pLI, gmLI
- Role type (e.g., Closer, Setup)

Determine:
- If aLI > 1.5 → High Leverage bonus
- If aLI < 0.85 → Penalty
- Use 50% aLI, 25% pLI, 25% gmLI

Return: `Leverage_Usage_Score`, role-based base tier (Closer = 75, HL = 70, etc.)
```

---

## 🔹 **Step 4: Calculate Saves / Holds / IR Score (15%)**

```markdown
Inputs:
- Saves, Save Opportunities
- Holds, Hold Opportunities
- Inherited Runners (IR), Inherited Scored (IS)

Calculate:
- Save% = Saves / SVO
- Hold% = Holds / Opportunities
- IR Prevention % = 1 - (IS / IR)

Blend equally (33% each) into `Saves_Holds_IR_Score`. Note if IR% ranks in top 5% of league.
```

---

## 🔹 **Step 5: Calculate Stuff Quality Score (15%)**

```markdown
Inputs:
- Stuff+, Pitching+, Location+
- CSW%
- Weighted Pitch Value

Logic:
- Scale Stuff+/Pitching+/Location+ (max bonus at 130+)
- If CSW% > 32% → bonus
- Add +2 for Top 5% pitch category (FA, SL, CH, etc.)

Return: `Stuff_Quality_Score` with tier label.
```

---

## 🔹 **Step 6: Calculate Batted Ball Score (10%)**

```markdown
Inputs:
- CSW% (primary)
- Barrel%
- HardHit%

Weighted:
- 80% CSW%
- 10% Inverse Barrel%
- 10% Inverse HardHit%

Return: `Batted_Ball_Score`
```

---

## 🔹 **Step 7: Calculate Clutch & IR Score (10%)**

```markdown
Inputs:
- Clutch Score (FanGraphs or derived metric)
- IR% (Inherited Scored / Inherited Runners)

Logic:
- Blend clutch stat with IR prevention rate
- Reward <25% IR% with strong bonus

Return: `Clutch_IR_Score`
```

---

## 🔹 **Step 8: Calculate Prospect Score (5%)**

```markdown
Inputs:
- Prospect Rank
- Minor League Awards
- MiLB Stats (ERA, K/BB, WHIP)

Scoring:
- Top 10 = +5
- Top 100 = +2.5
- Awards & Stats = minor boosts

Return: `Prospect_Score`
```

---

## 🔹 **Step 9: Calculate Injury Score (5%)**

```markdown
Inputs:
- # of IL stints (last 2 years)
- Duration of IL
- Arm/Shoulder/Elbow tags

Scoring:
- Full year IL = -3
- 2+ stints = -3
- Recurring arm injuries = -1 per year (max -4)

Return: `Injury_Score`
```

---

## 🔹 **Step 10: Calculate Team Standing Score (5%)**

```markdown
Input: Team Tier or Standings Rank

Scoring:
- Top of League = +5
- Contender = +3
- Competitive = +1
- .500 = 0
- Seller = -1
- Non-Competitive = -3
- Tanking = -5

Return: `Team_Standing_Score`
```

---

## 🔹 **Step 11: Calculate Trade Rumors Score (1%)**

```markdown
Input: Is player in active trade rumors? What role?

Apply penalty:
- Closer = -15%
- Setup/HL = -20%
- Middle = -25%

Only apply if in trade season (Late June to Deadline).
Return: `Trade_Rumors_Score`
```

---

## 🔹 **Step 12: Calculate Age Penalty**

```markdown
Input: Player Age

Scoring:
- Age ≤ 35 → 0
- 36 = -2.5%
- 37 = -5%
- 38 = -10%
- 39 = -15%
- 40+ = -20%

Return: `Age_Penalty_Score`
```

---

## 🔹 **Step 13: Calculate Non-Playing Stats Score (25%)**

```markdown
Blend:
- 5% Prospect Score
- 5% Injury Score
- 5% Team Standing Score
- 1% Trade Rumors Score
- 5% Role Tier Score
- Age Penalty Score

Return: `Non_Playing_Stats_Score`
```

---

## 🔹 **Step 14: Calculate Current Season RRI (50%)**

```markdown
Blend the following:
- 30% Performance_Score
- 20% Leverage_Usage_Score
- 15% Saves_Holds_IR_Score
- 15% Stuff_Quality_Score
- 10% Batted_Ball_Score
- 10% Clutch_IR_Score

Return: `Current_Season_RRI`
```

---

## 🔹 **Step 15: Final RRI Score**

```markdown
Final RRI = (0.25 * Previous RRI) + (0.50 * Current Season RRI) + (0.25 * Non-Playing Stats Score)

Return:
- Final RRI Score
- Percentile Rank (optional)
- Tier Label (e.g., Elite, God Tier, Risky)
- Badges: 🌀 Stuff+ | 🧤 IR% | 🎯 CSW%
```

---

Would you like these step-by-step prompts exported as:

* ✅ `.md` for GitHub documentation
* ✅ `.pdf` instructional sheet
* ✅ `.ipynb` notebook template for Python?
