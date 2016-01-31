# -*- coding: cp1254 -*-
import smtplib, socket, sys, getpass

def main():
    print

    try:
        smtpserver = smtplib.SMTP('smtp.gmail.com', 587)
        smtpserver.ehlo()
        smtpserver.starttls()
        smtpserver.ehlo()
        print "Connection to Gmail Successfully!"
        print "Connected to Gmail" + "\n"
        try:
            gmail_user = str(raw_input('Enter your Gmail: ')).lower().strip()
            gmail_pwd = getpass.getpass('Enter your pass: ').strip()
            smtpserver.login(gmail_user, gmail_pwd)
        except smtplib.SMTPException:
            print
            print "Authentication failed! :(" + '\n'
            smtpserver.close()
            getpass.getpass('Press ENTER to continue!')
            sys.exit(1)
                
    except (socket.gaierror, socket.error, socket.herror, smtplib.SMTPException), e:
        print "Connection to Gmail Failed! :("
        print e
        getpass.getpass('Press ENTER to continue!')
        sys.exit(1)
    while True:
        to = str(raw_input('Send mail to: ')).lower().strip()
        if to != '': break
        else: print "This field is required!"
    sub = str(raw_input('Subject: ')).strip()
    bodymsg = str(raw_input('Body of mail:'))
    print
    header = 'To: ' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject: ' + sub + '\n' + 'Body message: ' + bodymsg + '\n'
    print header
    msg = header + '\n' + bodymsg + '\n\n'

    try:
        smtpserver.sendmail(gmail_user, to, msg)
    except smtplib.SMTPException:
        print 'Email could not be sent! :(' + '\n'
        smtpserver.close()
        getpass.getpass('Press ENTER to continue!')
        sys.exit(1)

    print "Email Sent Successfully!" + '\n'
    smtpserver.close()
    getpass.getpass('Press ENTER to continue!')
    sys.exit(1)
        
    print '\n'
    raw_input('pause script')
main()
#Author: Nigella
