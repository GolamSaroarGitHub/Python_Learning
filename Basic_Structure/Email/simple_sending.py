# import smtplib
import getpass
#
# smtpObj=smtplib.SMTP('smtp.gmail.com',587)
#
# smtpObj.ehlo()
# smtpObj.starttls()
# print('Please Enter the password for the Email\n')
# pswd = getpass.getpass('Password:')
# myEmail='golamsaroar89@gmail.com'
# sendTo='syedaabida89@gmail.com'
# body='Subject: So long.\nDear Alice, so long and thanks for all the fish. Sincerely, Bob'
# smtpObj.login(myEmail,pswd)
# smtpObj.sendmail(myEmail,sendTo,body)
# smtpObj.quit()


######  But the authenticatioon need to be approved from the google account for the less secure app######


import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
pswd = getpass.getpass('Password:')
server.login("golamsaroar89@gmail.com",pswd)

msg = "YOUR MESSAGE!"
server.sendmail("golamsaroar89@gmail.com","syedaabida89@gmail.com", msg)
server.quit()
