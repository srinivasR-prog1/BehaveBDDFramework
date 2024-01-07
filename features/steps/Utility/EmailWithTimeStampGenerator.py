from datetime import datetime


def get_new_mail_with_timestamp():
    time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    return "chandu" + time_stamp + "@gmail.com"