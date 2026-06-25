from pathlib import Path

root = Path.cwd()

files = {
    "README.md": """# Base Project

A simple Python project for tracking crypto projects, ecosystem notes, and useful research links.

## What it does

- Stores basic project information
- Tracks project category and status
- Keeps research notes organized
- Helps practice clean Python development

## Run

python -m src.main
""",

    ".gitignore": """__pycache__/
*.pyc
.env
venv/
""",

    "src/__init__.py": "",

    "src/models.py": """from dataclasses import dataclass


@dataclass
class Project:
    name: str
    category: str
    status: str
    website: str = ""
    notes: str = ""
""",

    "src/tracker.py": """from src.models import Project


class ProjectTracker:
    def __init__(self):
        self.projects = []

    def add_project(self, project: Project):
        self.projects.append(project)

    def list_projects(self):
        return self.projects

    def count_projects(self):
        return len(self.projects)
""",

    "src/main.py": """from src.models import Project
from src.tracker import ProjectTracker


def main():
    tracker = ProjectTracker()

    tracker.add_project(
        Project(
            name="Base",
            category="Layer 2",
            status="Watching",
            website="https://base.org",
            notes="Tracking ecosystem activity and builder updates."
        )
    )

    for project in tracker.list_projects():
        print(f"{project.name} | {project.category} | {project.status}")


if __name__ == "__main__":
    main()
""",

    "data/projects.json": """[
  {
    "name": "Base",
    "category": "Layer 2",
    "status": "Watching",
    "website": "https://base.org",
    "notes": "Tracking ecosystem activity and builder updates."
  }
]
""",

    "docs/overview.md": """# Overview

This repository is a small crypto project tracker built with Python.

The goal is to keep project notes, links, categories, and research updates in one clean place.
""",

    "docs/roadmap.md": """# Roadmap

- Add project search
- Add category filters
- Add JSON loading
- Add command line options
- Add simple project reports
"""
}

for file_path, content in files.items():
    path = root / file_path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

print("Project files created successfully.")