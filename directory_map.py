import os
import json
import smtplib

def file_writer(text):
    with open("tree_directory.txt","a") as f_output:
        f_output.write(text)  
def list_files(startpath):


    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = '\t' * 1 * (level)
        output_string = json.dumps('{}{}/ \n'.format(indent, os.path.basename(root)))
        file_writer(output_string)
        subindent = '\t' * 1 * (level + 1)
        output_string = json.dumps('%s %s \n' %(subindent,[f for f in files]))
        file_writer(''.join(output_string))


list_files("C:\\")



from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'your mail'
email_password = 'your password'
email_send = 'mail address where you want to send'

subject = 'Tree directory map with python'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hey there, a mail from python'
msg.attach(MIMEText(body,'plain'))

filename='tree_directory.txt'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()












