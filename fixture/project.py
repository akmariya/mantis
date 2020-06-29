import re
from model.project import Project


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_project_page(self):
        driver = self.app.driver
        driver.find_element_by_link_text("Управление").click()
        driver.find_element_by_link_text("Управление проектами").click()

    def get_project_list(self):
        driver = self.app.driver
        self.open_project_page()
        group_list = []
        projects = driver.find_elements_by_xpath("//*[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr")
        for each in projects:
            project = each.find_elements_by_css_selector("td")
            adress = project[0].find_element_by_tag_name("a").get_attribute("href")
            project_id_str = re.search("id=.*", adress).group(0)
            project_id = project_id_str[3:len(project_id_str)]
            project_name = project[0].text
            project_description = project[4].text
            group_list.append(Project(id=project_id, name=project_name, description=project_description))
        return group_list

    def count_projects(self):
        driver = self.app.driver
        self.open_project_page()
        try:
            l = len(driver.find_elements_by_xpath("//*[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr"))
        except:
            l = 0
        return l

    def add_project(self, project):
        driver = self.app.driver
        self.open_project_page()
        driver.find_element_by_xpath("//button[@type='submit']").click()
        driver.find_element_by_id("project-name").click()
        driver.find_element_by_id("project-name").send_keys(project.name)
        driver.find_element_by_id("project-description").click()
        driver.find_element_by_id("project-description").send_keys(project.description)
        driver.find_element_by_xpath("//input[@value='Добавить проект']").click()

    def delete_project(self, project):
        driver = self.app.driver
        self.open_project_page()
        projects = driver.find_elements_by_xpath("//*[@id='main-container']/div[2]/div[2]/div/div/div[2]/div[2]/div/div[2]/table/tbody/tr")
        for each in projects:
            project_el = each.find_elements_by_css_selector("td")
            adress = project_el[0].find_element_by_tag_name("a").get_attribute("href")
            project_id_str = re.search("id=.*", adress).group(0)
            project_id = project_id_str[3:len(project_id_str)]
            if project_id == project.id:
                project_el[0].find_element_by_tag_name("a").click()
                break
        driver.find_element_by_xpath("//input[@value='Удалить проект']").click()
        driver.find_element_by_xpath("//input[@value='Удалить проект']").click()
