from pathlib import Path

root = Path.cwd()

main_content = '''from src.loader import load_projects
from src.tracker import ProjectTracker


def main():
    tracker = ProjectTracker()
    projects = load_projects("data/projects.json")

    for project in projects:
        tracker.add_project(project)

    print(f"Loaded projects: {tracker.count_projects()}")

    for project in tracker.list_projects():
        print(f"{project.name} | {project.category} | {project.status}")


if __name__ == "__main__":
    main()
'''

overview_content = '''# Overview

This repository is a small crypto project tracker built with Python.

The tracker now supports loading project data from a JSON file, which makes it easier to update the project list without changing the main application logic.

## Current Features

- Project data model
- Project tracker class
- JSON project loader
- Basic command-line output
'''

(root / "src" / "main.py").write_text(main_content, encoding="utf-8")
(root / "docs" / "overview.md").write_text(overview_content, encoding="utf-8")

print("Main file updated to use JSON loader.")