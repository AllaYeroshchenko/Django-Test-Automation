# -*- coding: utf-8 -*-
from models.resume import Resume
from models.experience import Experience
from models.education import Education
import time
import os.path
import jsonpickle
import pytest
import importlib

def load_from_json():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..\\data\\resumes.json")) as fr:
        return jsonpickle.decode(fr.read())

testdata=load_from_json()


@pytest.mark.parametrize("resume", testdata, ids=[repr(x) for x in testdata])
def test_add_resume(app, db, resume):
	last_id=db.get_last_resume_id()
	app.resume.add(resume)
	last_new_id=db.get_last_resume_id()
	# check that max id is changed
	assert last_id != last_new_id
	#get a new resume record from database and compare it with added data
	new_resume_rec=db.get_resume_record(last_new_id)[0]
	assert new_resume_rec==(resume.first_name, resume.last_name, resume.email, resume.phone, resume.address,
		resume.city, resume.state, resume.country, resume.zip_code, resume.job_title, resume.summary)
	#get a new education records from database and compare it with added data
	new_education_rec=db.get_education_record(last_new_id)
	for i in range(len(new_education_rec)):
		assert new_education_rec[i]==(resume.education[i].organization_name, resume.education[i].description,
		 resume.education[i].title, resume.education[i].start_date, resume.education[i].end_date)
	#get a new experience records from database and compare it with added data
	new_experience_rec=db.get_experience_record(last_new_id)
	for i in range(len(new_experience_rec)):
		assert new_experience_rec[i]==(resume.experience[i].position, resume.experience[i].company_name,
		 resume.experience[i].description, resume.experience[i].start_date, resume.experience[i].end_date)	
 