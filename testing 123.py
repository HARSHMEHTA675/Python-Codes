from py_day_test import MessageUsers,make_messages
from py_day_mod.make_messages import MessageUsers
print(123)
obj= MessageUsers()
obj.add_user("harsh",123.32,email="hmehta675@gmail.com")
obj.add_user("yash",435.3)
obj.add_user("abhishek",43.4)
obj.add_user("prakhar",453.5)
obj.get_details
print(obj.make_messages())
default_names=["Harsh","Yash","Abhishek","Prakhar"]
default_amounts=[123.32,435.3,43.4,453.5]
make_messages(default_names,default_amounts)
