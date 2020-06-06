#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.utils import parseaddr, formataddr
import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# 输入发件人地址与口令
from_addr = input('From: ')
password = input('password: ')
# 输入收件人地址
to_addr = input('To: ')
# 输入SMTP服务器地址
smtp_server = input('SMTP server: ')

msg_text = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg_html = MIMEText('<html><body><h1>Hello</h1>' +
                    '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
                    '<p><img src="cid:0"></p>' +
                    '</body></html>', 'html', 'utf-8')
msg = MIMEMultipart()
msg.attach(msg_html)

# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('mail/pic.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='mail/pic.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='mail/pic.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

msg['From'] = _format_addr('Dad <%s>' % from_addr)
msg['To'] = _format_addr('Son <%s>' % to_addr)
msg['Subject'] = Header('Regards from Dad......', 'utf-8').encode()

# SMTP协议默认端口 25
server = smtplib.SMTP(smtp_server, 25)  # SMTP协议默认端口 25
# server = smtplib.SMTP(smtp_server, 587)  # 加密发送，qq端口 587
# server.starttls() # STARTTLS加密传输
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
