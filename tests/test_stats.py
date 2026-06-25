from src.models import Project
from src.stats import count_by_category, count_by_status, count_by_tag
from src.tracker import ProjectTracker


def test_count_by_category():
    tracker = ProjectTracker()
    tracker.add_project(Project(name="Base", category="Layer 2", status="Watching"))

    assert count_by_category(tracker)["Layer 2"] == 1


def test_count_by_status():
    tracker = ProjectTracker()
    tracker.add_project(Project(name="Base", category="Layer 2", status="Watching"))

    assert count_by_status(tracker)["Watching"] == 1


def test_count_by_tag():
    tracker = ProjectTracker()
    tracker.add_project(Project(name="Base", category="Layer 2", status="Watching", tags=["layer2"]))

    assert count_by_tag(tracker)["layer2"] == 1
