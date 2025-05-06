import os
from tkinter import simpledialog, Tk, messagebox

# Hide the main tkinter window
root = Tk()
root.withdraw()

# Ask for project name
project_name = simpledialog.askstring("HighQ Project Launcher", "Enter new project name:")

if project_name:
    base = os.path.join(os.getcwd(), project_name)
    subfolders = [
        "05_Briefs_&_Breakdowns", "06_Assets/logos", "06_Assets/banners",
        "06_Assets/icons", "06_Assets/screenshots",
        "07_Data/inputs", "07_Data/outputs"
    ]
    files = {
        "00_ReadMe.md": f"# {project_name}\n\nProject initialized with HighQ.",
        "01_Project_Overview.md": "## Overview\n\n> Describe project goal and components.",
        "02_ChangeLog.md": "# 🔄 ChangeLog\n\n## [v0.1.0] - Init",
        "03_Sprint_Planner.md": "# 📆 Sprint Planner – Week of: _____",
        "04_Review_Log.md": "# 🧠 Review Log\n\n> Weekly check-in template."
    }

    # Create folders
    os.makedirs(base, exist_ok=True)
    for folder in subfolders:
        os.makedirs(os.path.join(base, folder), exist_ok=True)

    # Create files
    for filename, content in files.items():
        with open(os.path.join(base, filename), "w") as f:
            f.write(content)

    messagebox.showinfo("✅ Success", f"Project '{project_name}' created successfully.")
else:
    messagebox.showinfo("❌ Cancelled", "No project name entered. Launcher closed.")
