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
