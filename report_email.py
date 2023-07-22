#!/usr/bin/env python3
import os, datetime
import reports
import emails

def generate_pdf(fd):# Iterate over the files in the feedback directory
  pdf = ''
  for fi in osld:
    if fi.endswith('.txt'):
      with open(os.path.join(fd, fi), "r") as f:
        #Extract the name, and weight
        lines = f.readlines()
        fruit = lines[0].strip()
        weight = int(lines[1].strip().replace('lbs', ''))
        pdf += f"{fruit}<br/><br/> {weight} lbs<br/><br/>"
  print(pdf)
  return pdf

if __name__ == "__main__":
    #directory information
  cwd = os.getcwd()
  fd = cwd + '/supplier-data/descriptions/'
  osld = os.listdir(fd)
  #report data
  title = "Process Updated on {}".format(datetime.date.today())
  pdf = generate_pdf(fd)
  #generate pdf report
  reports.generate_report("/tmp/processed.pdf", title, pdf)
  #email data
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ["USER"])
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  #generate email for the online fruit store report and pdf attachment
  message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
  emails.send_message(message)
