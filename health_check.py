#!/usr/bin/env python3
import shutil
import psutil
from emails import generate_email
from emails import send_message
import os, sys
import socket

def check_disk_usage(disk):
  du = shutil.disk_usage(disk)
  free = du.free/du.total*100
  return free > 20

def check_cpu_usage():
    cp = psutil.cpu_percent(1)
    return cp < 80

def check_memory():
  memory = psutil.virtual_memory()
  return memory.available > 500 / 1024**2

def resolve_host():
  localhostip = socket.gethostbyname("localhost")
  return localhostip == "127.0.0.1"

def auto_warn():
  sender = "automation@example.com"
  recipient = "{}@example.com".format(os.environ["USER"])
  body = "Please check your system and resolve the issue as soon as possible."
  error_list = []

  if not check_cpu_usage():
    error_list.append("Error - CPU usage is over 80%")
  if not check_disk_usage("/"):
    error_list.append("Error - Available disk space is less than 20%")
  if not check_memory():
    error_list.append("Error - Available memory is less than 500MB")
  if not resolve_host:
    error_list.append("Error - localhost cannot be resolved to 127.0.0.1")
  if error_list:
    subject = ', and '.join(error_list)
    message = generate_email(sender, recipient, subject, body)
    send_message(message)

if __name__ == "__main__":
  auto_warn()