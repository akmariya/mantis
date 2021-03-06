from suds.client import Client
from suds import WebFault

from model.project import Project


class SoaHelper:

    def __init__(self, app):
        self.app = app
        self.base_url = app.base_url

    def can_login(self, username, password):
        client = Client(self.base_url + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client(self.base_url + "/api/soap/mantisconnect.php?wsdl")
        list_projects = client.service.mc_projects_get_user_accessible(username, password)
        projects = []
        for project in list_projects:
            projects.append(Project(id=project.id, name=project.name, description=project.description))
        return projects
