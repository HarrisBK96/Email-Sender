import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

#Using html to make it more dynamic
html = Template (Path('index.html').read_text())

#Email description
email = EmailMessage()
email['from'] = 'Harris'
email['to'] = 'abc_123@gmail.com'
email['subject'] = 'Dynamic Email'

#Setting the email content using html file 
email.set_content(html.substitute(name='mr_xyz'), 'html')

#Accessing gmail server to login to your account and send email 
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	#login with your email and password
	smtp.login('abc_456@gmail.com', 'password123')
	smtp.send_message(email)
	print('All good boss!')
