import smtplib
import email.mime.multipart
import email.mime.text

msg = email.mime.multipart.MIMEMultipart()
msg['from'] = 'a421318584@163.com'
msg['to'] = '421318584@qq.com'
msg['subject'] = 'test'
content = "你好,这是一封自动发送的邮件。"
txt = email.mime.text.MIMEText(content)
msg.attach(txt)
smtp = smtplib
smtp = smtplib.SMTP()
smtp.connect('smtp.163.com','25')
smtp.login('a421318584@163.com','1617193104')
smtp.sendmail('a421318584@163.com','421318584@qq.com',str(msg))
smtp.quit()
