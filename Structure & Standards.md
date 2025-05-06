Absolutely — here's your **HighQ Project Structure Guidelines** doc, designed to standardize every project across GitHub, Notion, or your local dev environment. This ensures your files, folders, and content all follow the same predictable, ADHD-friendly flow.

---

# 📁 Project Structure Guidelines

*A universal system for consistency, speed, and peace of mind.*

---

## 🧱 Folder Architecture (Standard for Every Project)

```
/[ProjectName]/
│
├── 00_ReadMe.md
├── 01_Project_Overview.md
├── 02_ChangeLog.md
├── 03_Sprint_Planner.md
├── 04_Review_Log.md
├── 05_Briefs_&_Breakdowns/
│   ├── FeatureBrief_[feature].md
│   └── BugFix_[bugname].md
├── 06_Assets/
│   ├── logos/
│   ├── banners/
│   ├── icons/
│   └── screenshots/
└── 07_Data/
    ├── inputs/
    └── outputs/
```

---

## 📝 File Naming Conventions

| File Type      | Format Example              | Notes                             |
| -------------- | --------------------------- | --------------------------------- |
| Markdown Files | `00_ReadMe.md`              | Numbers keep order consistent     |
| Images         | `ProjectName_Type_v1.0.png` | Use underscores, not spaces       |
| Scripts / Data | `rri_score_engine_v1.sql`   | lowercase + underscores preferred |
| Assets Folder  | `/06_Assets/`               | Sorted by type                    |
| Versions       | `v1.0`, `v1.1`, etc.        | Use semver-like clarity           |

---

## 🎨 Asset Format Guidelines

| Asset Type  | File Type        | Min Size    | Notes                             |
| ----------- | ---------------- | ----------- | --------------------------------- |
| Logos       | `.png`           | 512x512 px  | Transparent preferred             |
| Banners     | `.png` or `.jpg` | 1200x675 px | For social or homepage use        |
| Icons       | `.svg` or `.png` | 64x64 px    | Use flat or duotone styles        |
| Screenshots | `.jpg`           | 1080p+      | Include filename date/version tag |

---

## 🔁 Versioning and ChangeLog Rules

* Always update `02_ChangeLog.md` **before or after a major edit**
* Format by version + date:

```markdown
## [v1.0.2] – 2025-05-07
### Added
- Initial README and layout structure
### Changed
- Updated RRI formula logic for bullpen tiers
### Fixed
- None
```

---

## 🧠 Best Practices for Structure Consistency

1. ✅ **Always start a new project using the base folder template**
2. ✅ **Never save files directly in the root** unless they’re core docs
3. ✅ **Use the same folder order** across GitHub, Google Drive, and local
4. ✅ **Label asset files clearly** with version tags and usage type
5. ✅ **Sync Sprint Planner and Review Log weekly** with your real work

---

## 🔧 Optional Tools for Automation

* 🐍 Use a Python or PowerShell script to generate new folders using this structure
* 📦 Save this as a GitHub repo starter template
* 🧠 Duplicate a Notion template page per project

---

Would you like me to generate:

* A **starter template ZIP file** with placeholder markdown and folders?
* A **GitHub repo template** with all 9 of your current projects initialized?
* A **custom project setup script** for local use (bash or PowerShell)?

Just say the word and we’ll make deployment seamless.
