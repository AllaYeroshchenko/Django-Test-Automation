
class SessionHelper:
    def __init__(self, app):
        self.app=app

    def login(self, login, password):
        wd = self.app.wd
        # login
        self.app.open_home_page()
        wd.find_element_by_link_text("Login").click();
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys(login)
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("login").click()


    def logout(self):
        wd = self.app.wd
        # logout
        wd.find_element_by_link_text("Logout").click()
        #wd.find_element_by_name("user")


    def ensure_logout(self):
        wd = self.app.wd
        # logout
        if self.is_logged_in():
            self.logout()
        #wd.find_element_by_name("username")

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements_by_link_text("Logout"))>0


    def is_logged_in_as(self, username):
        wd = self.app.wd
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd
        print(wd.find_element_by_xpath("/html/body/div/header/div/div/div[2]/li/text()"))
        return wd.find_element_by_xpath("/html/body/div/header/div/div/div[2]/li/text()")


    def ensure_login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
