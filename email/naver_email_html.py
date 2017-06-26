import smtplib
from email.message import EmailMessage
import getpass
password = getpass.getpass('password: ')

message = EmailMessage()
message['Subject'] = 'Email 테스트 입니다.'
message['From'] = 'angelx_try@naver.com'
message['To'] = 'angelxtry@gmail.com'
message.add_alternative('''

<h1>AskDjango VOD</h1>

<ul>

<li>장고 기본편</li>

<li>크롤링 차근차근 시작하기</li>

<li>파이썬으로 업무 자동화</li>

</ul>

''', subtype='html')

with smtplib.SMTP_SSL('smtp.naver.com', 465) as mailserver:
    mailserver.ehlo()
    mailserver.login('angelx_try', password)
    mailserver.send_message(message)

print('이메일을 발송했습니다.')
