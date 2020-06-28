import random

from model.project import Project


def test_add_project(app):
    old_list = app.project.get_project_list()
    project = random.choice(old_list)
    app.project.delete_project(project)
    new_list = app.project.get_project_list()
    old_list.remove(project)
    assert sorted(new_list, key=Project.id_or_max) == sorted(old_list, key=Project.id_or_max)
