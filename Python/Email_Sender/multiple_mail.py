import smtplib
try:
    # connecting with gmail server
    server = smtplib.SMTP(host='smtp.gmail.com',port=587)
    # starting the security protocol
    server.starttls()

    # Ask for Reciever mail
    receiver_emails = ['jiradhey402@gmail.com','ranjitsingh97591@gmail.com','ranjit.upflairs@gmail.com']

    # put your mail creditional
    sender_email = 'smartengineer0786@gmail.com'
    password = '## write your password here ##'
    
    #write your mail subject and body
    subject = input('what is your problem 🤣😂  ')
    body = input('Thoda detail me btao 😜 ')
    message = f"Subject: {subject}\n\n{body}"
    server.login(sender_email, password=password)
    for mail in receiver_emails:
        # login in gmail.com with your creditions
        server.sendmail(sender_email, mail, message)
        print(f"Successfully mail has been sent to {mail}😉🤞😉")
    # close connection after sending the mail
    server.quit()
except Exception as e:
    print('Mail was not sent 😒😒!')
