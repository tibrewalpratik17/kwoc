# import gmail
import smtplib
import json
from email.mime.text import MIMEText
import os
import requests

def slack_notification(message):
    headers = {
        "Content-Type": "application/json"
    }
    data = json.dumps({
        "text": "In KWOC Website following error occured :\n{}".format(message)
    })
    r = requests.post(
        os.environ["SLACK_WEBHOOK_URL"], headers=headers, data=data)

    if r.status_code != 200:
        print("in slack_notification : {}".format(r.status_code))
        print(r.text)

def send_mail(mail_subject, mail_body, to_email):
	# credentials = json.load(open('CONFIG', 'r'))
	msg = MIMEText(mail_body)
	msg['Subject'] = mail_subject
    # print (msg)
	# sending mail
	try:
		server = smtplib.SMTP('smtp.gmail.com:587')
		server.starttls()
		server.login(os.environ["EMAIL"],os.environ["PASSWORD"])
		server.sendmail(os.environ["EMAIL"], to_email, msg.as_string())
		server.quit()
		return True
	except :
		slack_notification("Got following error while sending email : \n{}".format(traceback.format_exc()))
		return False
