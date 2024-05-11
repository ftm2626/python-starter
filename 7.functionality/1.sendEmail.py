import smtplib

sender = "you@gmail.com"
receiver = "them@gmail.com"
password = "1234"
subject = "test email"
body = "this is a test email to check for content"

# header 

message = f"""From:{sender}
To: {receiver}
Subject: {subject}\n
{body}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender,password)
    print("logged in")
    server.send_message(sender,receiver,message)
    print("email has been send")
except smtplib.SMTPAuthenticationError:
    print("unable to signin")

# open less secure access of gmail account to work
