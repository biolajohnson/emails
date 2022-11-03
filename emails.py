import os, smtplib
from dotenv import load_dotenv

# set up
load_dotenv()

port = os.getenv("port")
password = os.getenv("password")
user = os.getenv("sender")
server = smtplib.SMTP("smtp.gmail.com", port)
server.starttls()
server.login(user, password)
receiver = input("Type the reciever: ")
message = input("Type your message: ")
server.sendmail(user, receiver, message)
    
    




