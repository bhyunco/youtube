#### 3) Gmail을 활용하기 위한 사전 세팅

#3-1-1) 지메일 로그인
#3-1-2) 메일 설정 클릭(모든설정클릭)
#3-1-3) 전달 및 POP/IMAP 클릭
#3-1-4) Imap 액세스 - IMAP 사용 클릭
#3-1-5) 변경사항 저장

#3-2-1) https://myaccount.google.com/security
#3-2-2) google에 로그인 탭에서 2단계 인증
#3-2-3) 앱 비밀번호 클릭
#3-2-4) 앱 비밀번호 생성 (앱(메일) 선택, 기기선택)
#3-2-5) 생성된 앱 비밀번호 저장



#### 4) Gmail을 활용한 메일전송
import os
import smtplib
from email .mime .multipart import MIMEMultipart
from email .mime .text import MIMEText
from email .mime .base import MIMEBase
from selenium .webdriver.chrome .options import Options
from email import encoders
# (본인이 운영하는 지메일주소)
smtp_user = '' #본인의 Gmail 주소를 집어넣어주세요
# (본인이 운영하는 지메일에서 확보가능한 password)
smtp_password = '' #본인의 password를 집어넣어주세요
emails = [''] # 보내고자 하는 이메일을 적어주세요.
server = 'smtp.gmail.com'
port = 587
for email in emails :
    msg = MIMEMultipart("alternative")
    msg ["Subject"] = '안녕하세요 비현코입니다.'
    msg ["From"] = smtp_user
    msg ["To"] = email
    msg .attach (
    MIMEText (
    "비현코입니다.",
    'plain'
    )
    )
    #워드크라우드 첨부
    # attachment = open ('wordcloud_news2.png', 'rb')
    # part = MIMEBase ('application', 'octet-stream')
    # part .set_payload ((attachment).read ())
    # encoders .encode_base64 (part )
    # part .add_header ('Content-Disposition', "attachment; filename= " + 'wordcloud_news2.png')
    # msg .attach (part )
    # #엑셀첨부
    # attachment = open ('bhyunco_test.xlsx', 'rb')
    # part = MIMEBase ('application', 'octet-stream')
    # part .set_payload ((attachment).read ())
    # encoders .encode_base64 (part )
    # part .add_header ('Content-Disposition', "attachment; filename= " + 'bhyunco_test.xlsx')
    # msg .attach (part )
    s = smtplib .SMTP (server , port )
    s .ehlo ()
    s .starttls ()
    s .login (smtp_user , smtp_password )
    s .sendmail (smtp_user , email , msg .as_string ())
    s .quit ()
