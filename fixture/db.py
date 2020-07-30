from models.resume import Resume
from models.education import Education
from models.experience import Experience
import mysql.connector
import sshtunnel

sshtunnel.SSH_TIMEOUT = 5.0
sshtunnel.TUNNEL_TIMEOUT = 5.0

class DbFixture:
    def __init__(self, ssh, ssh_host, ssh_user, ssh_password, host, database_name, user, password, user_id):
        self.ssh=ssh
        self.ssh_host=ssh_host
        self.ssh_user=ssh_user
        self.ssh_password=ssh_password
        self.host=host
        self.database_name=database_name
        self.user=user
        self.password=password
        self.user_id=user_id
        #use ssh tunnel
        self.tunnel=sshtunnel.SSHTunnelForwarder((ssh), 
            ssh_username=ssh_user, 
            ssh_password=ssh_password, 
            remote_bind_address=(ssh_host, 3306))
        self.tunnel.start()
        #connect with database
        self.connection = mysql.connector.connect(user=user, password=password, 
            host=host, port=self.tunnel.local_bind_port, 
            database=database_name, autocommit=True)


    def get_last_resume_id(self):
        last_id=0
        cursor = self.connection.cursor()
        try:    
            cursor.execute("select max(id) from resume_resume")
            row=cursor.fetchone()
            last_id=row[0]
        finally:
            cursor.close()
        return last_id

    def get_resume_record(self, id):
        cursor = self.connection.cursor()
        try:    
            cursor.execute("""select first_name, last_name, email, phone, 
                address, city, state, country, zip_code, job_title, 
                summary from resume_resume where id=%s""", (id,))
            rows=cursor.fetchall()
        finally:
            cursor.close()
        return rows

    def get_education_record(self, resume_id):
        cursor = self.connection.cursor()
        try:    
            cursor.execute("""select organization_name, description, title,
                date_format(start_date, '%Y-%m-%d'), date_format(end_date,'%Y-%m-%d') from resume_education where resume_id_id=%s""", (resume_id,))
            rows=cursor.fetchall()
        finally:
            cursor.close()
        return rows

    def get_experience_record(self, resume_id):
        cursor = self.connection.cursor()
        try:    
            cursor.execute("""select position, company_name, description,
                date_format(start_date, '%Y-%m-%d'), date_format(end_date,'%Y-%m-%d') from resume_experience where resume_id_id=%s""", (resume_id,))
            rows=cursor.fetchall()
        finally:
            cursor.close()
        return rows     

    def get_quantity_resumes(self):
        quantuty=0
        cursor = self.connection.cursor()
        try:    
            cursor.execute("select count(*) from resume_resume")
            row=cursor.fetchone()
            quantuty=row[0]
        finally:
            cursor.close()
        return quantuty

    def get_quantity_resumes_for_user(self):
        quantuty=0
        cursor = self.connection.cursor()
        try:    
            cursor.execute("select count(*) from resume_resume where user_id_id=%s", (self.user_id, ))
            row=cursor.fetchone()
            quantuty=row[0]
        finally:
            cursor.close()
        return quantuty



    def destroy(self):
        self.connection.close()
        self.tunnel.stop()



