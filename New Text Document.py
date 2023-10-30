import pandas as pd
import smtplib
import main as p1

SenderAddress = "<Email Address of sender>"
password = "password of sender"

e = pd.read_excel("Email.xls")
emails = e['Emails'].values
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("krishnakrish100108@gmail.com", "nfhxorpvmzshunro")
msg = p1.text
if msg == "MH 20 EE 7598":
    print("boom")
subject = "Hello world"
body = "Subject: {}\n\n{}".format(subject,msg)
for email in emails:
    server.sendmail("krishnakrish100108@gmail.com", email, body)
server.quit()
