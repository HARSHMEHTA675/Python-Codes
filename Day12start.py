import smtplib
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import  MIMEText


host = "smtp.gmail.com"
port = 587
username="hmehta675@gmail.com"
password="darkchocolate123*"

from_email=username
to_list=["hmehta675@gmail.com"] 

class MessageUsers():
    user_details=[]
    messages=[]
    email_messages=[]
    base_message="""Hi {name}!
Thank You for the purchase on {date},
We hope you excited using it. Just as a
reminder the purchase total was ${total}.
Have a great one!

Team Elina
"""
    def add_user(self,name,amount,email=None):
      
        detail ={
            "name":name,
            "amount":amount,
            }
        name=name[0].upper()+name[1:].lower()
        amount="%.2f" %(amount)
        today= datetime.date.today()
        date_text="{today.month}/{today.day}/{today.year}".format(today=today)
        detail["date"]=date_text
        if email != None:
            detail["email"]=email
            
        self.user_details.append(detail)
    def get_details (self):
        return self.user_details 
    def make_messages(self):
        if len(self.user_details) >0:
            for detail in self.get_details():
                name=detail["name"]
                amount="%.2f"%(detail["amount"])
                date = detail["date"] 
                message= self.base_message
                new_msg= message.format(
                 name=name,
                 date=date,
                 total=amount
                )
                user_email=detail.get("email")
                if user_email:
                    user_data={
                        "email":user_email,
                        "message":new_msg
                    }
                    self.email_messages.append(user_data)
                else:
                    self.messages.append(new_msg)
            return self.messages
        return []
    def send_email(self):
        self.make_messages()
        if len(self.email_messages)>0 :
           for detail in self.email_messages:
               user_email=detail["email"]
               user_message=detail["message"]
               try:
                    email_conn = smtplib.SMTP(host, port)
                    email_conn.ehlo()
                    email_conn.starttls()
                    email_conn.login(username,password)
                    the_msg= MIMEMultipart("alternative")
                    the_msg["Subject"]="Billing Update"
                    the_msg["From"]=from_email
                    the_msg["To"]=user_email
                    part_1= MIMEText(user_message,"plain")
                    the_msg.attach(part_1)
                    print(the_msg.as_string())
                    email_conn.sendmail(from_email,[user_email],the_msg.as_string())
                    email_conn.quit()
               except smtplib.SMTPException:
                    print("error sending message")
           return True 
        return False 
           
        
                    
obj= MessageUsers()
obj.add_user("Harsh",123.32,email="hmehta675@gmail.com")
obj.add_user("Shreya",435.3,email="jainshreya219@gmail.com")
obj.add_user("Priyanka",43.4,email="priyanka27shaha@gmail.com")
obj.add_user("Pratiksha",453.5,email="pratikshashah33@gmail.com")
obj.get_details
obj.send_email()

