import smtplib
import sys
def sendmail():
	destination = input()
	sender = input()
	password = input()
	try:
		print("server in")
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls() 
		server.ehlo()
		server.login(sender, password)
		msg = input()
		server.sendmail(sender,destination,msg)
		print("server out")
		server.quit() 
		sys.exit()
	except:
		print("email not sent")

sendmail()	