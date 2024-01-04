# smtplib input 

import smtplib

sender_email = input("enter your mail : ")
sender_password = input("enter you password : ")
receiver_email = input("enter receiver mail : ")
subject = input("enter your subject : ")
message = input("enter your message : ")


session  = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()
session.login(sender_email,sender_password)
session.sendmail(sender_email,receiver_email,subject,message) 
print("your mail is sent")