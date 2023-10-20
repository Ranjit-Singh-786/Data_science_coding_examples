import smtplib
try:
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    server.starttls()
    sender_email = input('Sender email :-')
    receiver_email = input('Reciever mail :-')
    server.login("sender_mail_here", "sender_mail_password_here")

    subject = input('what is your problem 🤣😂  ')
    body = input('Thoda detail me btao 😜')
    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, receiver_email, message)
    server.quit()
except Exception as e:
    print('Mail was not sent 😒😒!')
