from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import os
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
import base64

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.send']
def aunthentication():
    creds = None
    # The file token.json stores the user's access and refresh tokens,and is
# created automatically when the authorization flow completes for thefirst
# time.

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json',SCOPES)
# If there are no (valid) credentials available, let the user log in.   
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('/home/vishesh/gmail_api/client_secrets.json', SCOPES)
            creds = flow.run_local_server(port=0)
# Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return creds

def prepare_and_send_email(recipient, subject, message_text):

    creds = aunthentication()
    try:
        for r in recipient:
            service = build('gmail', 'v1', credentials=creds)
            msg = create_message('vishesh2019cs081@abesit.edu.in', r ,subject, message_text)
            send_message(service, 'vishesh2019cs081@abesit.edu.in', msg)

    except HttpError as error:
        print(f'An error occurred: {error}')

def create_message(sender, to, subject, message_text):


    message = MIMEMultipart()
    message['from'] = sender
    message['to'] = to
    message['subject'] = subject
    message.attach(MIMEText(message_text))

    attachment="/home/vishesh/gmail_api/your_video.mp4"
    with open(attachment,'rb') as fp:
        attachment_data=MIMEApplication(fp.read())

    message.attach(attachment_data)
    
    return {'raw':base64.urlsafe_b64encode(message.as_string().encode()).decode()}

def send_message(service, user_id, message):

    try:
        message = (service.users().messages().send(userId=user_id,body=message).execute())

        print('Message Id: %s' % message['id'])
        return message
    except HttpError as error:
        print('An error occurred: %s' % error)

if __name__ == '__main__':
    import time
while True:
    prepare_and_send_email(['vbhardwaj1305@gmail.com','hamzaaziz822@gmail.com','yashaswi2019cs087@abesit.edu.in','yugansh2019cs181@abesit.edu.in','vaishnavi2019cs164@abesit.edu.in','yash2019cs004@abesit.edu.in','srishti.vishwari@gmail.com'],'!IMPORTANT! ',' tera ek video college m leak ho gya h... ')
    time.sleep(60) # this is in seconds, so 60 seconds x 30 mins

    