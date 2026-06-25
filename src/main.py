from src.models import Project
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
