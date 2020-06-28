
def test_add_project(app):
    old_projects = app.project.get_project_list()
    assert False