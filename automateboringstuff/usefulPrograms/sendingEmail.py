"""This Program sends an Email"""""

import smtplib

def sendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):

    message = """From: {}
Subject: {}
    
{}
""".format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message.encode('utf8')) #including .encode is important for polish characters
        server.close()
        print("mail sent") #Confirming that it was successful
        return True

    except:

        print('Error sending email') #Informs that there has been error
        return False

mailFrom = 'Your automation system' #From whom email is being send (it can be Your Name)
mailTo = ['exampleEmail@gmail.com'] #Adress that we are sending email to (it is list so can be several)
mailSubject = 'Processing finished successfully' #E-mail subject
mailBody = '''Hello  

This mail confirms that processing has finished without problems,

Have a nice day''' #Email content

user = 'example@gmail.com' #Enter your email here
password = 'examplePassword' #Enter your password here

sendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
