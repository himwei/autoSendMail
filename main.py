import os
import smtplib
import ssl
from email.message import EmailMessage
import time

def qqemail(subject, email, text):
    max_retries = 3
    retries = 0
    while retries < max_retries:
        try:
            EMAIL_ADDRESS = os.environ["SEND_ADDRESS"]
            EMAIL_PASSWORD = os.environ["SMTP_KEY"]

            context = ssl.create_default_context()

            msg = EmailMessage()
            msg['subject'] = subject
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = email
            msg.set_content(text)

            with smtplib.SMTP_SSL("smtp.qq.com", 465, context=context) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)
            print("邮件发送成功")
            return
        except KeyError:
            print("环境变量未正确设置，请检查 SEND_ADDRESS 和 SMTP_KEY 是否存在。")
            break
        except smtplib.SMTPException as e:
            print(f"邮件发送失败，第 {retries + 1} 次重试: {e}")
            retries += 1
            time.sleep(5)  # 等待 5 秒后重试
        except Exception as e:
            print(f"发生未知错误，第 {retries + 1} 次重试: {e}")
            retries += 1
            time.sleep(5)  # 等待 5 秒后重试
    print("达到最大重试次数，邮件发送失败。")

if __name__ == "__main__":
    try:
        subject = os.environ["SEND_SUBJECT"]
        email = os.environ["RECEIVE_ADDRESS"]
        text = os.environ["SEND_BODY"]
        qqemail(subject, email, text)
    except KeyError:
        print("环境变量未正确设置，请检查 SEND_SUBJECT、RECEIVE_ADDRESS 和 SEND_BODY 是否存在。")