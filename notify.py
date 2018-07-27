import smtplib
from twilio.rest import Client

class Notify:
    def __init__(self, to, username, password, phone):
        self.to = to
        self.username = username
        self.password = password
        self.phone = phone
        self._email_template ="SUBJECT:CLASS OPENING\n\n{}"

    def send_email(self, message):
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(self.username, self.password)
        server.sendmail(self.username, self.to, self._email_template.format(message))
        server.quit()

    def send_text(self, message):
        client = Client("ACbac21979971e63686b9382491e65e816","803f476b9677cb0154c55cac8759c223")
        client.messages.create(to=self.phone, from_ = "+15862572502", body = message)
