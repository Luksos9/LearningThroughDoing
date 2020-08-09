"""This Program sends an Email"""""

import smtplib
import functools #with this module i can build function .partial


def sendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody):
    message = """From: {}
Subject: {}

{}
""".format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user, password)
        server.sendmail(user, mailTo, message.encode('utf8'))  # including .encode is important for polish characters
        server.close()
        print("mail sent")  # Confirming that it was successful
        return True

    except:

        print('Error sending email')  # Informs that there has been error
        return False


mailFrom = 'Your automation system'  # From whom email is being send (it can be Your Name)
mailTo = ['exampleEmail@gmail.com']  # Adress that we are sending email to (it is list so can be several)
mailSubject = 'Processing finished successfully'  # E-mail subject
mailBody = '''Hello!  

This mail confirms that processing has finished without problems,

Have a nice day'''  # Email content

user = 'example@gmail.com'  # Enter your email here
password = 'examplePassword'  # Enter your password here

# adding this so i dont have to give all the parameters that were required  (like sendInfoEmail orginally had to)
SendInfoEmailFromGmail = functools.partial(sendInfoEmail, user, password, mailSubject='Execution alert')

SendInfoEmailFromGmail(mailFrom=mailFrom, mailTo=mailTo, mailBody=mailBody) #parameters by name

# this one below orginally was sending email but i had to give many parameters
# sendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
