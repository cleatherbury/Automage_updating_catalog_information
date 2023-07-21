#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib

def generate(sender, recipient, subject, body, attachment_path):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)

  if attachment_path is not None:
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    # Process the attachment and add it to the email
    with open(attachment_path, 'rb') as attachment_file:
      message.add_attachment(attachment_file.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename=attachment_filename)

  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  try:
    mail_server = smtplib.SMTP('localhost:1025')
    mail_server.send_message(message)
    print('message sent successfully')
  except SMTPResponseException as e:
    error_code = e.smtp_code
    error_messsage = e.smtp_error
    print(str(error_code) + ' - ' + str(error_messsage))
    
    mail_server.quit()

def main():
  sender = 'automation@example.com'
  #username = (on side)
  #recipient = username@example.com
  recipient = "{}@example.com".format(os.environ.get('USER'))
  #Replace username with the username given in the Connection Details Panel on the right hand side.
  subject = "Upload Completed - Online Fruit Store"

  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  attachment_path =  '/tmp/processed.pdf'
  #Attach the path to the file processed.pdf Once you have finished editing the report_email.py script, save the file by typing ':wq'.

if __name__ == '__main__':
  main()