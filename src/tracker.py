from src.models import Project


class ProjectTracker:
    def __init__(self):
        self.projects = []

    def add_project(self, project: Project):
        self.projects.append(project)

    def list_projects(self):
        return self.projects

    def count_projects(self):
        return len(self.projects)

    def filter_by_status(self, status: str):
        return [
            project for project in self.projects
            if project.status.lower() == status.lower()
        ]

    def filter_by_category(self, category: str):
        return [
            project for project in self.projects
            if project.category.lower() == category.lower()
        ]

    def search(self, keyword: str):
        keyword = keyword.lower()

        return [
            project for project in self.projects
            if keyword in project.name.lower()
            or keyword in project.category.lower()
            or keyword in project.notes.lower()
        ]
