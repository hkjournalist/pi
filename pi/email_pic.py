import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

sender = 'wangjianpeng0822@163.com'
receiver = 'wangjianpeng0822@163.com'
subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'wangjianpeng0822@163.com'
password = '19900822a'

msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = '请扫描二维码登录'

#构造附件
# import weixin_login
att = MIMEText(open('G:\\树莓派\\QR.jpg', 'rb').read(), 'base64', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment; filename="QR.jpg"'
msgRoot.attach(att)

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()