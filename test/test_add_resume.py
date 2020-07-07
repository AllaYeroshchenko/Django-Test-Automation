# -*- coding: utf-8 -*-
from models.resume import Resume
from models.experience import Experience
from models.education import Education
import time
import os.path
import jsonpickle
import pytest
import importlib
#import allure_pytest
#from data.groups import testdata

def load_from_json():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "data\\resume_random_gen.json")) as fr:
        return jsonpickle.decode(fr.read())

testdata=load_from_json()
# testdata = [
#     Group(name="name1", header="header1", footer="footer1"),
#     Group(name="name2", header="header2", footer="footer2")
# ]


@pytest.mark.parametrize("resume", testdata, ids=[repr(x) for x in testdata])
def test_add_resume(app, resume):
#	print(resume)
	app.resume.add(resume)
	time.sleep(5)
 #    group=json_groups
 
 #    old_groups = db.get_group_list()
 # #   with allure_pytest.step('When I add a group %s to the list' % group):
 #    app.group.create(group)
 #  #  with allure_pytest.step('Then the new group list is equal to the old list with the added group'):
 #    new_groups = db.get_group_list()
 #    old_groups.append(group)
 #    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
 #    def clean(group):
 #        return Group(id=group.id, name=group.name.strip())
    


#def load_from_json():
 #   with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "resume_random_gen.json")) as fr:
  #      return jsonpickle.decode(fr.read())