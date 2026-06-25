from src.tracker import ProjectTracker


def get_all_tags(tracker: ProjectTracker):
    tags = set()

    for project in tracker.list_projects():
        for tag in project.tags:
            tags.add(tag)

    return sorted(tags)


def filter_by_tag(tracker: ProjectTracker, tag: str):
    tag = tag.lower()

    return [
        project for project in tracker.list_projects()
        if tag in [item.lower() for item in project.tags]
    ]
