import datetime

class MessageUsers():
    user_details=[]
    messages=[]
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
            detail["email"]:email
            
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
                new_msg= unf_message.format(
                 name=name,
                 date=date,
                 total=amount
                )
                self.messages.append(new_msg)
            return self.messages
        return []
