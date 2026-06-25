from src.tracker import ProjectTracker


def build_summary(tracker: ProjectTracker) -> str:
    total = tracker.count_projects()

    lines = [
        "Project Tracker Summary",
        f"Total projects: {total}",
        ""
    ]

    for project in tracker.list_projects():
        lines.append(f"- {project.name} | {project.category} | {project.status}")

    return "\n".join(lines)
