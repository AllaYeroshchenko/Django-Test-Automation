from models.resume import Resume
import time

class ResumeHelper:

    def __init__(self, app):
        self.app=app

    def open_resumes_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/resume"): 
            self.app.open_home_page()
            wd.find_element_by_id("resume_app").click()
            wd.find_element_by_link_text("Add new resume").click()


    def add(self, resume):
        wd = self.app.wd
        self.open_resumes_page()
        # fill group form
        self.fill(resume)
        wd.find_element_by_xpath("//input[@type='submit']").click()        


    def fill(self, resume):
        wd = self.app.wd
        # fill group form
        self.change_field_value(wd, "first_name", resume.first_name)
        self.change_field_value(wd, "last_name", resume.last_name)
        self.change_field_value(wd, "email", resume.email)
        self.change_field_value(wd, "phone", resume.phone)
        self.change_field_value(wd, "address", resume.address)
        self.change_field_value(wd, "city", resume.city)
        self.change_field_value(wd, "state", resume.state)
        self.change_field_value(wd, "country", resume.country)
        self.change_field_value(wd, "zip_code", resume.zip_code)
        self.change_field_value(wd, "job_title", resume.job_title)
        self.change_field_value(wd, "summary", resume.summary)
        #fill education block
        number_edu=len(resume.education)
        num=0
        while number_edu>0:
            edu_block=wd.find_element_by_id("education"+str(num+1))
            self.change_field_value(edu_block, "year_start", resume.education[num].start_date)
            self.change_field_value(edu_block, "year_end", resume.education[num].end_date)
            self.change_field_value(edu_block, "organization", resume.education[num].organization_name)
            self.change_field_value(edu_block, "title", resume.education[num].title)
            self.change_field_value(edu_block, "description", resume.education[num].description)
            number_edu=number_edu-1
            num=num+1
            if number_edu>0:
                wd.find_element_by_id("edu").click()
        #fill experience block
        number_exp=len(resume.experience)
        print("number= ", number_exp)
        num=0
        while number_exp>0:
            exp_block=wd.find_element_by_id("experience"+str(num+1))
            self.change_field_value(exp_block, "ex_year_start", resume.experience[num].start_date)
            self.change_field_value(exp_block, "ex_year_end", resume.experience[num].end_date)
            self.change_field_value(exp_block, "company", resume.experience[num].company_name)
            self.change_field_value(exp_block, "position", resume.experience[num].position)
            self.change_field_value(exp_block, "ex_description", resume.experience[num].description)
            number_exp=number_exp-1
            num=num+1
            if number_exp>0:
                wd.find_element_by_id("exp").click()
                
        

    def change_field_value(self, location, fieldname, text):
        #wd = self.app.wd
        if text is not None:
            location.find_element_by_name(fieldname).clear()
            location.find_element_by_name(fieldname).send_keys(text)

 
    # def to_group_page(self):
    #     wd = self.app.wd
    #     if not (wd.current_url.endswith("/group.php") and (len(wd.find_elements_by_name("new")))>0):
    #         wd.find_element_by_link_text("group page").click()




    # def delete_first_group(self):
    #     self.delete_group_by_index(0)

    # def delete_group_by_index(self, index):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_index(index)
    #     wd.find_element_by_name("delete").click()
    #     self.to_group_page()
    #     self.group_cache = None


    # def delete_group_by_id(self, id):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_id(id)
    #     wd.find_element_by_name("delete").click()
    #     self.to_group_page()
    #     self.group_cache = None


    # def edit_group_by_id(self, id, group_new):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_id(id)
    #     wd.find_element_by_name("edit").click()
    #     self.fill(group_new)
    #     wd.find_element_by_name("update").click()
    #     self.to_group_page()
    #     self.group_cache = None

    # def select_group_by_index(self, index):
    #     wd = self.app.wd
    #     wd.find_elements_by_name("selected[]")[index].click()

    # def select_group_by_id(self, id):
    #     wd = self.app.wd
    #     wd.find_element_by_css_selector("input[value='%s']" % id).click()


    # def edit_first_group(self, group):
    #     self.edit_group_by_index(group, 0)


    # def edit_group_by_index(self, group, index):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_group_by_index(index)
    #     wd.find_element_by_name("edit").click()
    #     self.fill(group)
    #     # submit
    #     wd.find_element_by_name("update").click()
    #     self.to_group_page()
    #     self.group_cache = None



    # def select_first_group(self):
    #     wd = self.app.wd
    #     wd.find_element_by_name("selected[]").click()

    # def modify_first_group(self, new_group_data):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     self.select_first_group()
    #     #open modification form
    #     wd.find_element_by_name("edit").click()
    #     #fill group form
    #     self.fill(new_group_data)
    #     #submit modification
    #     wd.find_element_by_name("update").click()
    #     self.to_group_page()
    #     self.group_cache = None

    # def count(self):
    #     wd = self.app.wd
    #     self.open_groups_page()
    #     return len(wd.find_elements_by_name("selected[]"))

    # group_cache = None

    # def get_group_list(self):
    #     if self.group_cache is None:
    #         wd = self.app.wd
    #         self.open_groups_page()
    #         self.group_cache = []
    #         for element in wd.find_elements_by_css_selector("span.group"):
    #             text = element.text
    #             id = element.find_element_by_name("selected[]").get_attribute("value")
    #             self.group_cache.append(Group(name=text, id=id))
    #     return list(self.group_cache)
