import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
import os
from datetime import datetime
from dotenv import load_dotenv
# import upload_report_to_cloud_storage
load_dotenv()



email_sender = "arunrout9295@gmail.com"
email_password = os.getenv('GMAIL_16_DIGIT_PASSWORD')
email_receiver = 'arunrout76@gmail.com'
print(email_password)


def generate_mailer_body():
    """This Method returns Email message Subject, mail Body of the mail"""
    subject = f"Automation Status | Browser: Edge | {datetime.now().strftime('%d/%m/%y %I:%M %p')}"
    body = f"""
    <h3>Automation Run is completed.</h3>
    Please find the report <a href="adwesdsefw">here.</a><br>
    <p style="font-size:10px">Thanks & Regards,<br>
    Automation Team</p>
    """
    em = EmailMessage()
    html_body = MIMEText(body, 'html')
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(html_body)
    return em.as_string()


def send_mail():
    """This Method sends mail"""
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, generate_mailer_body())
        print("Mail sent")
    except Exception as e:
        print(f"Exception occurred while sending mail: {e}")



send_mail()