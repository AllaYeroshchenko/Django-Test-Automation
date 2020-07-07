from sys import maxsize
from models.resume import Resume


class Experience:
    def __init__(self, id=None, resume_id=None, position=None, company_name=None, description=None, start_date=None, end_date=None):
        self.id=id        
        self.resume_id=resume_id
        self.position=position
        self.company_name=company_name
        self.description=description
        self.start_date=start_date
        self.end_date=end_date

    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.resume_id, self.company_name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id==other.id) and (self.resume_id==other.resume_id) and (self.company_name==other.company_name)

