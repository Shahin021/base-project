import json
from pathlib import Path

from src.models import Project
from src.validator import validate_project_data


def load_projects(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return []

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return []

    projects = []

    for item in data:
        if not validate_project_data(item):
            continue

        projects.append(
            Project(
                name=item.get("name", ""),
                category=item.get("category", ""),
                status=item.get("status", ""),
                website=item.get("website", ""),
                notes=item.get("notes", "")
            )
        )

    return projects
