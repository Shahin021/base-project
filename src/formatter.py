from src.models import Project


def format_project(project: Project) -> str:
    return f"{project.name} | {project.category} | {project.status}"


def format_project_details(project: Project) -> str:
    lines = [
        f"Name: {project.name}",
        f"Category: {project.category}",
        f"Status: {project.status}",
        f"Website: {project.website}",
        f"Notes: {project.notes}",
    ]

    return "\n".join(lines)
