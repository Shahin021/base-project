from src.models import Project
from src.tracker import ProjectTracker


def test_filter_by_status():
    tracker = ProjectTracker()
    tracker.add_project(Project(name="Base", category="Layer 2", status="Watching"))
    assert len(tracker.filter_by_status("Watching")) == 1


def test_filter_by_category():
    tracker = ProjectTracker()
    tracker.add_project(Project(name="Soneium", category="Layer 2", status="Researching"))
    assert len(tracker.filter_by_category("Layer 2")) == 1


def test_search():
    tracker = ProjectTracker()
    tracker.add_project(Project(name="Startale App", category="Consumer App", status="Testing"))
    assert len(tracker.search("Startale")) == 1
