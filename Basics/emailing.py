# import smtplib
#
#  HOST = 'mail.gmail.com'
#  SUBJECT = "Test email from Python"
#  TO = "mike@someAddress.org"
#  FROM = "python@mydomain.com"
#  text = "Python 3.4 rules them all!"
#
#  BODY = "\r\n".join((
#  "From: %s" % FROM,
#  "To: %s" % TO,
#  "Subject: %s" % SUBJECT ,
#  "",
#  text
#  ))
#
# server = smtplib.SMTP(HOST)
#  server.sendmail(FROM, [TO], BODY)
# server.quit()


#!/usr/bin/python

import smtplib

sender = 'golamsaroar89@gmail.com'
receivers = ['golamsaroar89@gmail.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com')
   smtpObj.sendmail(sender, receivers, message)
   print ("Successfully sent email")
except EOFError:   print ("Error: unable to send email")