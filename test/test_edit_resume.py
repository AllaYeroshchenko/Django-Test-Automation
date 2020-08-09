# -*- coding: utf-8 -*-
from models.resume import Resume
from models.experience import Experience
from models.education import Education
import time
import os.path
import jsonpickle
import pytest
import random

def load_from_json():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\data\\resumes_for_edit.json")) as fr:
        return jsonpickle.decode(fr.read())

testdata=load_from_json()


@pytest.mark.parametrize("resume", testdata, ids=[repr(x) for x in testdata])
def test_edit_resume(app, db, resume):
	if db.get_quantity_resumes_for_user()==0:
		app.resume.add(Resume(first_name="test", last_name="test", email="test", phone="test", 
			address="test", city="test", state="test", country="test", zip_code="test", 
			job_title="test", summary="test", education=[], experience=[]))
	quantity_resumes_before=db.get_quantity_resumes_for_user()
	resumes_list=app.resume.get_resumes_list()
	random.choice(resumes_list).click()
	resume_id=app.resume.edit_resume(resume)
	assert app.resume.was_edited()==True, "Something went wrong, couldn't find a message that resume was edited."
	quantity_resumes_after=db.get_quantity_resumes_for_user()
	assert quantity_resumes_before==quantity_resumes_after
	#get the edited resume record from database and compare it with data for edit
	edited_resume_rec=db.get_resume_record(resume_id)[0]
	assert edited_resume_rec==(resume.first_name, resume.last_name, resume.email, resume.phone, resume.address,
		resume.city, resume.state, resume.country, resume.zip_code, resume.job_title, resume.summary)
	#get the edited education records from database and compare it with data for edit
	edited_education=db.get_education_record(resume_id)
	for i in range(len(edited_education)):
		assert edited_education[i]==(resume.education[i].organization_name, resume.education[i].description,
		 resume.education[i].title, resume.education[i].start_date, resume.education[i].end_date)
	#get the edited experience records from database and compare it with data for edit
	edited_experience=db.get_experience_record(resume_id)
	for i in range(len(edited_experience)):
		assert edited_experience[i]==(resume.experience[i].position, resume.experience[i].company_name,
		 resume.experience[i].description, resume.experience[i].start_date, resume.experience[i].end_date)	
 


