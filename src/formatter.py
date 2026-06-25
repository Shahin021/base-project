from src.models import Project


def format_project(project: Project) -> str:
    return f"{project.name} | {project.category} | {project.status}"


def format_project_details(project: Project) -> str:
    tags = ", ".join(project.tags) if project.tags else "No tags"

    lines = [
        f"Name: {project.name}",
        f"Category: {project.category}",
        f"Status: {project.status}",
        f"Website: {project.website}",
        f"Tags: {tags}",
        f"Notes: {project.notes}",
    ]

    return "\n".join(lines)
