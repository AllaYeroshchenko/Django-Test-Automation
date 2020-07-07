from sys import maxsize

class Resume:
    def __init__(self, id=None, first_name=None, last_name=None, email=None, phone=None,
        address=None, city=None, state=None, country=None, zip_code=None, job_title=None, summary=None,
        education=[], experience=[]):
        self.id=id
        self.first_name=first_name
        self.last_name=last_name
        #self.user_id=user_id
        self.email=email
        self.phone=phone
        self.address=address
        self.city=city
        self.state=state
        self.country=country
        self.zip_code=zip_code
        self.job_title=job_title
        self.summary=summary
        self.education=education
        self.experience=experience


    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.first_name, self.last_name, self.job_title)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id==other.id) and (self.job_title==other.job_title)


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize





