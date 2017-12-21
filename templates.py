import os
"""os module is been imported and it interacts with os and we can
access any file and print it using template
further in the method get_template_path os.path.join contains the path of the current
directory and furthe we define the rest of the path in file_ so it fetches the path opens the file reads is and prints the
message
in render_context we create a dictionary bring that and print it. It is basically use
in Jango"""


def get_template_path(path):
    file_path=os.path.join(os.getcwd(),path)
    if not os.path.isfile(file_path):
        raise Exception("this is not a valid path")
    return file_path

def get_template(path):
    file_path= get_template_path(path) 
    return open(file_path).read()             
    
def render_context(template_string,context):
    return template_string.format(**context)

file_="templates\email_message.txt"

file_html="templates\email_message.html"
template=get_template(file_)
template_html=get_template(file_html)
context={
    "name":"Justin",
    "date":None,
    "total":None
    }
print(render_context(template_html,context))
print(render_context(template,context))
