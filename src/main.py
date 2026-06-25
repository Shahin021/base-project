from src.config import DATA_FILE
from src.csv_exporter import export_projects_csv
from src.exporter import export_text_report
from src.loader import load_projects
from src.report import build_summary
from src.tracker import ProjectTracker


def main():
    tracker = ProjectTracker()
    projects = load_projects(DATA_FILE)

    for project in projects:
        tracker.add_project(project)

    summary = build_summary(tracker)
    print(summary)

    export_text_report(summary, "reports/summary.txt")
    export_projects_csv(tracker, "reports/projects.csv")


if __name__ == "__main__":
    main()
