import random
import string
from model.project import Project


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def test_add_project(app):
    old_list = app.project.get_project_list()
    project = Project(name=random_string("name", 10), description=random_string("description", 10))
    app.project.add_project(project)
    new_list = app.project.get_project_list()
    old_list.append(project)
    assert sorted(new_list, key=Project.id_or_max) == sorted(old_list, key=Project.id_or_max)
