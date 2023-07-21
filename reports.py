#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
import datetime
import os

#def create_dd(osld, fd):# Iterate over the files in the feedback directory
  #ddl = []
  #for fi in osld:
    #filepath = os.path.join(fd, fi)
    #if not fi.startswith('.'):
      #with open(filepath, "r") as f:
      # Extract the title, name, date, and feedback 
        #fruit = f.readline().strip()
        #weight = int(f.readline().strip().replace('lbs', ''))
        #description = f.read().strip()
        #img = os.path.splitext(fi)[0] + 'jpeg'
        #dd = {"name": fruit, "weight": weight, "description": description,"image": img}
        #ddl.append(dd)
  #print(ddl)  
  #return ddl

def make_body(dictionary):
  body = ''
  """Turns the data in dictionary into a list of lists."""
  for item in dictionary:
    name = item['name']
    #weight = f"{item['weight']} lbs"  # Use 'N/A' if 'weight' key is missing
    weight = f"{item['weight']} lbs" if 'weight' in item else 'N/A'
    entry = f"{name}<br/><br/> {weight}<br/><br/>"
    body += entry
  print(body)
  return body



def generate(filename, title, body):
    styles = getSampleStyleSheet()
    report = SimpleDocTemplate(filename)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(body, styles["BodyText"])
    #report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info])

def main():
  """Process the JSON data and generate a full report out of it."""
  
  #fd = os.path.join(os.getcwd(), 'supplier-data', 'descriptions')
  #osld = os.listdir(fd)
  #ddl = create_dd(osld, fd)
  #filename = '/tmp/processed.pdf'
  #title = f"Processed Update on {datetime.datetime.today().date()}."
  #body = make_body(ddl)
  #generate(filename, title, body)
  

if __name__ == '__main__':
    main()