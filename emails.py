#!/usr/bin/env python3
import email.message
import mimetypes
import os.path
import smtplib

def generate_email(sender, recipient, subject, body, attachment_path=None):
  """Creates an email with an attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["Subject"] = subject
  message["From"] = sender
  message["To"] = recipient
  message.set_content(body)
  # Adding email attahment
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

def send_message(message):
  """Sends the message to the configured SMTP server."""
  try:
    mail_server = smtplib.SMTP('localhost') #Connect to SMTP and sends the email
    mail_server.send_message(message)
    print('message sent successfully')
  except SMTPResponseException as e: #Checks exceptions
    error_code = e.smtp_code
    error_messsage = e.smtp_error
    print(str(error_code) + ' - ' + str(error_messsage))
  finally:
    if mail_server is not None:  # Check if mail_server was created before attempting to quit
      mail_server.quit()