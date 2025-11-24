import smtplib
from email.message import EmailMessage
from config_example import Config
import os




def send_admin_notification(subject, body):
if not Config.MAIL_USERNAME or not Config.MAIL_PASSWORD or not Config.ADMIN_EMAIL:
print('Mail settings not configured; skipping admin email.')
return


msg = EmailMessage()
msg['Subject'] = subject
msg['From'] = Config.MAIL_USERNAME
msg['To'] = Config.ADMIN_EMAIL
msg.set_content(body)


try:
server = smtplib.SMTP(Config.MAIL_SERVER, Config.MAIL_PORT)
server.starttls()
server.login(Config.MAIL_USERNAME, Config.MAIL_PASSWORD)
server.send_message(msg)
server.quit()
except Exception as e:
print('Failed to send admin email:', e)
