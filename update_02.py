from pathlib import Path

root = Path.cwd()

content = '''import json
from pathlib import Path

from src.models import Project


def load_projects(file_path: str):
    path = Path(file_path)

    if not path.exists():
        return []

    data = json.loads(path.read_text(encoding="utf-8"))

    projects = []
    for item in data:
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
'''

(root / "src" / "loader.py").write_text(content, encoding="utf-8")

print("Loader file created.")