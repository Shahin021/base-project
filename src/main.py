from src.loader import load_projects
from src.report import build_summary
from src.tracker import ProjectTracker


def main():
    tracker = ProjectTracker()
    projects = load_projects("data/projects.json")

    for project in projects:
        tracker.add_project(project)

    print(build_summary(tracker))


if __name__ == "__main__":
    main()
