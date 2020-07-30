from models.resume import Resume
from models.experience import Experience
from models.education import Education
import time
import pytest
import random 


#@pytest.mark.parametrize("i", [x for x in range(15)]) #uncomment this if you need to delete many records from resumes
def test_delete_resume(app, db):     #, i):
	# if user don't have resumes yet, add one
	if db.get_quantity_resumes_for_user()==0:
		app.resume.add(Resume(first_name="test", last_name="test", email="test", phone="test", 
			address="test", city="test", state="test", country="test", zip_code="test", 
			job_title="test", summary="test", education=[], experience=[]))
	quantity_resumes_before=db.get_quantity_resumes_for_user()
	resumes_list=app.resume.get_resumes_list()
	random.choice(resumes_list).click()
	resume_id=app.resume.delete_resume()
	deleted_resume_rec=db.get_resume_record(resume_id)
	deleted_education=db.get_education_record(resume_id)
	deleted_experience=db.get_experience_record(resume_id)
	quantity_resumes_after=db.get_quantity_resumes_for_user()
	assert len(deleted_resume_rec)==0, "Resume is still in database"
	assert len(deleted_education)==0, "Education records from deleted resume are still in database"
	assert len(deleted_experience)==0, "Exprrience records from this resume are still in database"
	assert quantity_resumes_before-1==quantity_resumes_after