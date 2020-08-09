"""This Program sends an Email"""""

import smtplib

mailFrom = 'Your automation system' #From whom email is being send (it can be Your Name)
mailTo = ['przykladowyEmail@gmail.com'] #Adress that we are sending email to (it is list so can be several)
mailSubject = 'Processing finished successfully' #E-mail subject
mailBOdy = '''Hello  

This mail confirms that processing has finished without problems,

Have a nice day''' #Email content

message = """From: {}
Subject: {}

{}
""".format(mailFrom, mailSubject, mailBOdy)

user = 'uzytkownik123@gmail.com' #Enter your email here
password = "veryConcealedPassword" #Enter your password here

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(user, mailTo, message.encode('utf8')) #including .encode is important for polish characters
    server.close()
    print("mail sent") #Confirming that it was successful

except:

    print('Error sending email') #Informs that there has been error