import argparse

from src.config import DATA_FILE
from src.loader import load_projects
from src.tracker import ProjectTracker
from src.formatter import format_project


def build_tracker() -> ProjectTracker:
    tracker = ProjectTracker()

    for project in load_projects(DATA_FILE):
        tracker.add_project(project)

    return tracker


def main():
    parser = argparse.ArgumentParser(description="Crypto project tracker")
    parser.add_argument("--status", help="Filter projects by status")
    parser.add_argument("--category", help="Filter projects by category")
    parser.add_argument("--search", help="Search projects by keyword")

    args = parser.parse_args()
    tracker = build_tracker()

    projects = tracker.list_projects()

    if args.status:
        projects = tracker.filter_by_status(args.status)

    if args.category:
        projects = tracker.filter_by_category(args.category)

    if args.search:
        projects = tracker.search(args.search)

    for project in projects:
        print(format_project(project))


if __name__ == "__main__":
    main()
