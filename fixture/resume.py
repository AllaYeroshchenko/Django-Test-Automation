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
            


    def add(self, resume):
        wd = self.app.wd
        self.open_resumes_page()
        wd.find_element_by_link_text("Add new resume").click()
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
            #edu_block=wd.find_element_by_id("education"+str(num+1))
            edu_blocks=wd.find_elements_by_css_selector("div.education")
            edu_block=edu_blocks[len(edu_blocks)-1]
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
        num=0
        while number_exp>0:
            #exp_block=wd.find_element_by_id("experience"+str(num+1))
            exp_blocks=wd.find_elements_by_css_selector("div.experience")
            exp_block=exp_blocks[len(exp_blocks)-1]
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

 
    def get_resumes_list(self):
        wd = self.app.wd
        self.open_resumes_page()
        resumes_list=[]
        resumes_locations_list=wd.find_elements_by_css_selector("div.content_inner>p>a")
        for res in resumes_locations_list:
            resumes_list.append(res)
        return resumes_list


    def delete_resume(self):
        wd=self.app.wd
        resume_url=wd.current_url 
        resume_id=resume_url[resume_url.rfind("/", 0, len(resume_url)-2)+1:-1]
        wd.find_element_by_css_selector("form#delete_resume>input[type='submit']").click()
        wd.switch_to.alert.accept()
        return resume_id   

    def edit_resume(self, resume):
        wd=self.app.wd
        resume_url=wd.current_url 
        resume_id=resume_url[resume_url.rfind("/", 0, len(resume_url)-2)+1:-1]
        wd.find_element_by_css_selector("form#edit_resume>input[type='submit']").click()
        del_edu_buttons=wd.find_elements_by_css_selector("button.del_edu")
        num=len(del_edu_buttons)
        while num>2: # 2 because 1 button is in hoden block
            del_edu_buttons[num-2].click()
            del_edu_buttons=wd.find_elements_by_css_selector("button.del_edu")
            num=len(del_edu_buttons)   
        del_exp_buttons=wd.find_elements_by_css_selector("button.del_exp")
        num=len(del_exp_buttons)
        while num>2: # 2 because 1 button is in hoden block
            del_exp_buttons[num-2].click()
            del_exp_buttons=wd.find_elements_by_css_selector("button.del_exp")
            num=len(del_exp_buttons)    
        self.fill(resume)
        wd.find_element_by_xpath("//input[@type='submit']").click()    
        return resume_id   


 