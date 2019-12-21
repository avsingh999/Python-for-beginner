import smtplib
import sys
def sendmail():
	destination = input()
	sender = input()
	password = input()
	try:
		print("서버 접속")
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls() 
		server.ehlo()
		server.login(sender, password)
		msg = input()
		server.sendmail(sender,destination,msg)
		print("서버 나가기")
		server.quit() 
		sys.exit()
	except:
		print("email이 보내지지 않았습니다.")

sendmail()	