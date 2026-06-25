from src.validator import validate_project_data


def test_valid_project_data():
    item = {
        "name": "Base",
        "category": "Layer 2",
        "status": "Watching"
    }

    assert validate_project_data(item) is True


def test_invalid_project_data():
    item = {
        "name": "",
        "category": "Layer 2",
        "status": "Watching"
    }

    assert validate_project_data(item) is False
