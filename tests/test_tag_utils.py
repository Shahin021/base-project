from src.models import Project
from src.tag_utils import filter_by_tag, get_all_tags
from src.tracker import ProjectTracker


def test_get_all_tags():
    tracker = ProjectTracker()
    tracker.add_project(Project(name="Base", category="Layer 2", status="Watching", tags=["layer2", "builders"]))

    assert "layer2" in get_all_tags(tracker)


def test_filter_by_tag():
    tracker = ProjectTracker()
    tracker.add_project(Project(name="Startale App", category="Consumer App", status="Testing", tags=["mini-apps"]))

    assert len(filter_by_tag(tracker, "mini-apps")) == 1
