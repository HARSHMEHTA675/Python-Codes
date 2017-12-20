from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username="hmehta675@gmail.com"
password="darkchocolate123*"

from_email=username
to_list=["hmehta675@gmail.com"]

email_conn = smtplib.SMTP(host, port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
the_msg= MIMEMultipart("alternative")
the_msg["Subject"]="Hello"
the_msg["From"]=from_email
the_msg["To"]=to_list[0]

plain_txt = "Testing the Message"
html_txt="""\
<html>
    <head></head>
        <body>
            <p>HEy!<br>
                Testing the email<b>message</b>.
            </p>
        </body>
</html>
"""
part_1= MIMEText(plain_txt,"plain")
part_2 = MIMEText(html_txt,"html")

the_msg.attach(part_1)
the_msg.attach(part_2)
print(the_msg.as_string())

email_conn.sendmail(from_email,to_list,the_msg.as_string())
email_conn.quit()
