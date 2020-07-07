from sys import maxsize
from models.resume import Resume

class Education:
    def __init__(self, id=None, resume_id=None, organization_name=None, description=None, title=None,
        start_date=None, end_date=None):
        self.id=id        
        self.resume_id=resume_id
        self.organization_name=organization_name
        self.description=description
        self.title=title
        self.start_date=start_date
        self.end_date=end_date

 
    def __repr__(self):
        return "%s:%s:%s:%s" % (self.id, self.resume_id, self.organization_name)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id==other.id) and (self.resume_id==other.resume_id) and (self.organization_name==other.organization_name)        