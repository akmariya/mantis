
class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        driver = self.app.driver
        driver.find_element_by_xpath('//*[@id="sidebar"]/ul/li[7]/a/i').click()
        driver.find_element_by_link_text(u"Управление проектами").click()

    def get_project_list(self):
        driver = self.app.driver
        self.open_project_page()


