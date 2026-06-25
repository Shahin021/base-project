from src.loader import load_projects
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
