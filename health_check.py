#!/usr/bin/env python3

import shutil
import psutil
import os
import socket
import emails

cpu_pctg_threshold = 80
disk_space_pctg_threshold = 20
avail_memory_threshold = 500
host_resolution = "127.0.0.1"


def cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage > cpu_pctg_threshold

def avail_disk_space():
    disk_space = psutil.disk_usage("/")
    avail_space = (disk_space.free / disk_space.total) * 100
    return avail_space > disk_space_pctg_threshold

def avail_memory():
    avail_memory = psutil.virtual_memory().available/(2**20)
    return avail_memory > avail_memory_threshold

def localhost_resolution():
    localhost = socket.gethostbyname('localhost')
    return localhost == host_resolution

if cpu_usage():
    subject_line = "Error - CPU usage is over {}%".format(cpu_pctg_threshold)
if avail_disk_space():
    subject_line = "Error - Available disk space is less than {}%".format(disk_space_pctg_threshold)
if avail_memory():
    subject_line = "Error - Available memory is less than 500MB"
if localhost_resolution():
    subject_line = "Error - localhost cannot be resolved to {}".format(host_resolution)
else:
    pass

if __name__ == "__main__":
    try:
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        subject = "Error - {}".format(subject_line)
        body = "Please check your system and resolve the issue as soon as possible"
        message = emails.generate_error_report(sender, receiver, subject, body)
        emails.send(message)
    except:
        print("unable to sent email notification")

