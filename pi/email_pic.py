import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from . import config

def submit():
  msgRoot = MIMEMultipart('related')
  msgRoot['Subject'] = '请扫描二维码登录'
  #构造附件
  # import weixin_login
  att = MIMEText(open('QR.jpg', 'rb').read(), 'base64', 'utf-8')
  att["Content-Type"] = 'application/octet-stream'
  att["Content-Disposition"] = 'attachment; filename="QR.jpg"'
  msgRoot.attach(att)
  smtp = smtplib.SMTP()
  smtp.connect('smtp.163.com')
  smtp.login(config.username, config.password)
  smtp.sendmail(config.sender, config.receiver, msgRoot.as_string())
  smtp.quit()