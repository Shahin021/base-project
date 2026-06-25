from src.config import REPORT_TITLE
from src.formatter import format_project
from src.stats import count_by_category, count_by_status
from src.tracker import ProjectTracker


def build_summary(tracker: ProjectTracker) -> str:
    lines = [
        REPORT_TITLE,
        f"Total projects: {tracker.count_projects()}",
        "",
        "Projects:"
    ]

    for project in tracker.list_projects():
        lines.append(f"- {format_project(project)}")

    lines.append("")
    lines.append("Categories:")

    for category, total in count_by_category(tracker).items():
        lines.append(f"- {category}: {total}")

    lines.append("")
    lines.append("Statuses:")

    for status, total in count_by_status(tracker).items():
        lines.append(f"- {status}: {total}")

    return "\n".join(lines)
