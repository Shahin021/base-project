from collections import Counter

from src.tracker import ProjectTracker


def count_by_category(tracker: ProjectTracker):
    return Counter(project.category for project in tracker.list_projects())


def count_by_status(tracker: ProjectTracker):
    return Counter(project.status for project in tracker.list_projects())


def count_by_tag(tracker: ProjectTracker):
    counter = Counter()

    for project in tracker.list_projects():
        for tag in project.tags:
            counter[tag] += 1

    return counter
