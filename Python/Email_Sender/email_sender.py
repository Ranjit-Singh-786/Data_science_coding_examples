import smtplib
try:
    # connecting with gmail server
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    # starting the security protocol
    server.starttls()

    # Ask for Reciever mail
    receiver_email = input('Enter Reciever mail :- ')

    # put your mail creditional
    sender_email = 'smartengineer0786@gmail.com'
    password = '######'

    # login in gmail.com with your creditions
    server.login(sender_email, password=password)

    #write your mail subject and body
    subject = input('what is your problem 🤣😂  ')
    body = input('Thoda detail me btao 😜 ')

    message = f"Subject: {subject}\n\n{body}"
    server.sendmail(sender_email, receiver_email, message)
    print('Successfully mail has been sent 😉🤞😉')

    # close connection after sending the mail
    server.quit()
except Exception as e:
    print('Mail was not sent 😒😒!')
