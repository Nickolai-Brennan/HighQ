# 🧠 HighQ Project Structure Guidelines

*A universal, ADHD-friendly documentation framework for managing creative, technical, and strategic projects.*

---

## 🔧 Core Objective

To ensure every project — whether code-based, design-driven, or content-focused — follows the same folder and documentation pattern. This reduces friction, improves onboarding, and helps you stay clear-minded during chaotic weeks.

---

## 📁 Standard Project Folder Architecture

```plaintext
/[ProjectName]/
│
├── 00_ReadMe.md
├── 01_Project_Overview.md
├── 02_ChangeLog.md
├── 03_Sprint_Planner.md
├── 04_Review_Log.md
│
├── 05_Briefs_&_Breakdowns/
│   ├── FeatureBrief_[feature].md
│   ├── StrategyBrief_[component].md
│   └── BugFix_[bugname].md
│
├── 06_Assets/
│   ├── logos/
│   ├── banners/
│   ├── icons/
│   └── screenshots/
│
└── 07_Data/
    ├── inputs/         ← Raw CSVs, scraped data, intake forms
    └── outputs/        ← Final computed tables, dashboards, models
```

---

## 🧩 Core Files and Purpose

### `00_ReadMe.md`

> Lightweight snapshot of the project. Used in GitHub, Notion, or shared folders.

```markdown
# FBCS3 – Fantasy Baseball Championship Series

🎯 **Goal**: Run a 15-league qualifier fantasy system culminating in a championship bracket.
🧰 **Tech Stack**: Sheets, Canva, WordPress, Discord, GitHub
📅 **Status**: In Progress – Signup Phase
📦 **Version**: v1.1.0
```

---

### `01_Project_Overview.md`

> The living blueprint: big picture, stakeholders, system logic.

```markdown
## 🧠 Project Overview
A fantasy baseball mega-league built for high-stakes, cross-league play.

## 📦 Key Components
- 15 regional qualifier leagues
- 1 championship "Super League"
- Built-in marketing, affiliate, and Discord automation

## 🧭 How Users Interact
1. Sign up via form
2. Join Discord
3. Get assigned to a region
4. Draft and compete
```

---

### `02_ChangeLog.md`

> Required on every project. Used to track real history.

```markdown
# 🔄 ChangeLog

## [v1.0.2] – 2025-05-06
### Added
- Sprint template
- Player ranking section on homepage
### Fixed
- Discord webhook errors
```

---

### `03_Sprint_Planner.md`

> Breaks tasks down into a week-by-week focus tracker.

```markdown
# Sprint – Week of 2025-05-06

🎯 Goal: Finalize sign-up flow and launch marketing page

| Day | Task                                | Status  |
|-----|-------------------------------------|---------|
| Mon | Finish signup form + embed          | ✅ Done |
| Tue | Create Discord invite structure     | ☐ To Do |
| Wed | Style homepage layout               | ☐ To Do |
```

---

### `04_Review_Log.md`

> Log your wins, pain points, and weekly resets.

```markdown
# Review – Week Ending May 10

✅ What Worked:
- Launching signup sheet
- Canva branding kit

⚠️ What Didn’t:
- Discord bot auto-assignment

🔁 Plan Next Week:
- Build out announcement script
```

---

### `05_Briefs_&_Breakdowns/`

Use this folder to organize mini-docs around features, ideas, bugs, and workflows.
Common types:

* `FeatureBrief_DiscordBot.md`
* `StrategyBrief_MarketingFunnels.md`
* `BugFix_EmailDuplication.md`

---

## 🎨 06\_Assets Folder – Visuals, Branding, and Creative

| Subfolder      | Contents                             | Naming Convention                |
| -------------- | ------------------------------------ | -------------------------------- |
| `logos/`       | Logos (transparent PNG, 512x512)     | `Project_Logo_v1.0.png`          |
| `banners/`     | Horizontal graphics, headers, social | `FBCS3_Header_1200x675_v1.0.jpg` |
| `icons/`       | Small flat icons (PNG/SVG)           | `icon_dollar.svg`                |
| `screenshots/` | UI/UX, mockups, charts               | `dashboard_preview_0506.jpg`     |

> ✏️ Always export designs in retina resolution when possible (2x scale).

---

## 📊 07\_Data Folder – Technical Content

* `inputs/`
  Raw CSVs, manual entry, scraped stats, user inputs

* `outputs/`
  Cleaned data, formatted dashboards, RRI scores, exports to Sheets or frontend

**Best Practices:**

* Always prefix files with source + date
  e.g., `fangraphs_rp_data_0506.csv`
* Separate raw from edited exports

---

## 🔁 File Naming Standards

| Element           | Rule                                             |
| ----------------- | ------------------------------------------------ |
| Use underscores   | `no spaces in file or folder names`              |
| Semantic versions | `v1.0`, `v1.1.1`, `v2.0-beta`                    |
| File format       | `.md` for text docs, `.png/.jpg` for images      |
| Date format       | `yyyymmdd` or `0506` (month-day)                 |
| Project prefixing | Always start filenames with the project code/tag |

---

## ✅ Team or Solo Use Best Practices

* **Solo Workflow**
  Use `Review_Log.md` and `Sprint_Planner.md` weekly
  Use `ChangeLog.md` for version control
  Store `Data/` outputs in sync with Google Sheets or GitHub

* **Team Workflow**
  Add `CONTRIBUTING.md` and `TEAM_NOTES.md` to root
  Lock image assets and style guides
  Assign sprint tasks inside `03_Sprint_Planner.md` by initials (e.g., `Nick: ☐ Finish banner`)

---

## 🧰 Optional Add-ons

| Doc Name           | Purpose                               |
| ------------------ | ------------------------------------- |
| `LICENSE.md`       | For open-source or shared GitHub work |
| `README_PUBLIC.md` | Clean, polished doc for sharing       |
| `BACKLOG.md`       | Parking lot for future features       |
| `ARCHIVE/`         | Store old versions of dashboards/docs |

