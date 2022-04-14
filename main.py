import smtplib
subject = 'Python Email'

body = 'Test'

message = f'Subject: {subject}\n\n{body}'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)

server.login('username', 'pw')

i = 0

while i <= 5:
  server.sendmail(

    'from',

    'to',

    message)

  i += 1

server.quit()
