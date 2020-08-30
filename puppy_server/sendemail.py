import smtplib

def send_email():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()

    server.starttls()
    server.ehlo()

    server.login('thespahrtan@gmail.com', 'gptilepqjytlygqg')

    subject = 'ily part 2'
    body = 'happy birthday you gorgeous beast'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'thespahrtan@gmail.com',
        'bapriborsky@gmail.com',
        msg
    )
    print('sent')

    server.quit()

send_email()