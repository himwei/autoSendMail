import os
def qqemail(subject,email,text):
    #无需安装第三方库
    EMAIL_ADDRESS=os.environ["SEND_ADDRESS"]      #换成你的邮箱地址
    EMAIL_PASSWORD=os.environ["STMP_KEY"]      #换成你的邮箱地址
    # EMAIL_PASSWORD=key

    import smtplib
    smtp=smtplib.SMTP('smtp.qq.com',25)

    import ssl
    context=ssl.create_default_context()
    sender=EMAIL_ADDRESS               #发件邮箱
    receiver=email                      #EMAIL_ADDRESS
                                          #收件邮箱
    from email.message import EmailMessage
    subject=subject
    body=text
    msg=EmailMessage()
    msg['subject']=subject       #邮件主题
    msg['From']=sender
    msg['To']=receiver
    msg.set_content(body)         #邮件内容

    with smtplib.SMTP_SSL("smtp.qq.com",465,context=context) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)

if __name__ == "__main__":
    subject = os.environ["SEND_SUBJECT"]#因为$前面是大写所以也是大写
    email = os.environ["RECEIVE_ADDRESS"]#因为$前面是大写所以也是大写
    text = os.environ["SEND_BODY"]#因为$前面是大写所以也是大写
    qqemail(subject,email,text)
