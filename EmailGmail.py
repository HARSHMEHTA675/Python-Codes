import smtplib

host="smtp.gmail.com"
port=587
username="hmehta675@gmail.com"
password="darkchocolate123*"
from_email=username
to_list=["jainshreya219@gmail.com"]

email_conn=smtplib.SMTP(host,port)
email_conn.ehlo()
email_conn.starttls()
email_conn.login(username,password)
email_conn.sendmail(from_email,to_list,"Hey I am very hungry can u owe me a dinner")
email_conn.quit()
