import smtplib

class Notify:
    def __init__(self, to, username, password, phone):
        self.to = to
        self.username = username
        self.password = password
        self.phone = phone
        
    def send_email(self, message):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(self.username, self.password)
        server.sendmail(self.username, self.to, message)
        server.quit()

    def send_text(self):
        pass
