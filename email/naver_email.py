import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('password: ')

message = EmailMessage()
message['Subject'] = 'Email 테스트 입니다.'
message['From'] = 'angelx_try@naver.com'
message['To'] = 'angelxtry@gmail.com'
message.set_content('''
안녕하세요. AskDjango입니다.

이 부분에는 이메일의 내용을 쓰실 수 있으며, HTML은 불가합니다.

HTML을 쓰시면 태그가 그대로 노출됩니다.

여러분의 파이썬/장고 페이스메이커가 되겠습니다.

감사합니다. ;)''')

with smtplib.SMTP_SSL('smtp.naver.com', 465) as mailserver:
    mailserver.ehlo()
    mailserver.login('angelx_try', password)
    mailserver.send_message(message)

print('이메일을 발송했습니다.')
