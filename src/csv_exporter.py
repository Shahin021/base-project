import csv
from pathlib import Path

from src.tracker import ProjectTracker


def export_projects_csv(tracker: ProjectTracker, output_path: str):
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "category", "status", "website", "tags", "notes"])

        for project in tracker.list_projects():
            writer.writerow([
                project.name,
                project.category,
                project.status,
                project.website,
                ", ".join(project.tags),
                project.notes
            ])
