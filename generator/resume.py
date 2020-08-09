# -*- coding: utf-8 -*-
import sys
import os.path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from models.resume import Resume
from models.experience import Experience
from models.education import Education
import random
import string
import jsonpickle
import getopt


try:
    opts, args=getopt.getopt(sys.argv[1:], "n:f:", ["number of resumes", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=3 #quantity of records in the file
f="data/resume_random_gen1.json"

for o, a in opts:
    if o=="-n":
        n=int(a)
    elif o=="-f":
        f=a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters+string.digits
    return prefix+"".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata=[Resume(None, random_string("first_name", 10), random_string("last_name", 15), random_string("email", 20),
        random_string("phone", 12), random_string("address", 50), random_string("city", 30), 
        random_string("state", 30), random_string("country", 20), random_string("zip_code", 5),
        random_string("job_title", 50), random_string("summary", 50),
        [Education(None, None, random_string("organization_name", 20), random_string("description", 20), 
            random_string("title", 20), start_date='2020-01-01', end_date='2020-01-01')], 
        [Experience(None, None, random_string("position", 20), random_string("company_name", 20), 
            random_string("description", 20), start_date='2020-01-01', end_date='2020-01-01')])
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as fw:
    jsonpickle.set_encoder_options("json", indent=2)
    fw.write(jsonpickle.encode(testdata))
