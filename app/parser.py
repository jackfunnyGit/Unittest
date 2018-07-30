import mimetypes
import os
import re
import calendar
from datetime import datetime
from app.configuration import *

PDF_FOLDER = "PI_folder"
# OlAddressEntryUserType Enumeration (Outlook)
# Ref: https://msdn.microsoft.com/en-us/vba/outlook-vba/articles/oladdressentryusertype-enumeration-outlook
OUTLOOK_olExchangeUserAddressEntry = 0
OUTLOOK_olExchangeRemoteUserAddressEntry = 5

folder_location = os.path.join(os.getcwd(), PDF_FOLDER)
if not os.path.isdir(folder_location):
    os.mkdir(folder_location)


def get_file_type(filename):
    file_type = mimetypes.guess_type(filename)[0]
    if file_type is not None:
        # mime type長得像這樣'image/png'
        return file_type
    # .msg檔案會無法解析mime type
    else:
        name, extension = os.path.splitext(filename)
        return extension


def parsed_attachment(attachment):
    d = dict()
    d['attachment_id'] = attachment.Index
    d['display_name'] = attachment.DisplayName
    d['file_name'] = attachment.FileName
    d['type'] = get_file_type(d['file_name'])
    d['size'] = attachment.Size
    return d


def parse_message_attachment(msg):
    attachments = []
    if msg.Attachments.count > 0:
        print(msg.Subject)
        print("email att count=", msg.Attachments.count)
        for attachment in msg.Attachments:
            d = parsed_attachment(attachment)
            d['message_id'] = get_message_id((msg))
            attachments.append(d)
    return attachments


def get_sender_mail_address(msg):
    if msg.SenderEmailType == 'EX':
        try:
            sender = msg.Sender

            if sender.AddressEntryUserType == OUTLOOK_olExchangeUserAddressEntry \
                    or sender.AddressEntryUserType == OUTLOOK_olExchangeRemoteUserAddressEntry:
                exch_user = sender.GetExchangeUser()
                if exch_user:
                    return exch_user.PrimarySmtpAddress
                else:
                    return 'exch_user is null'
            else:
                return sender.PropertyAccessor.GetProperty(PR_TRANSPORT_MESSAGE_HEADERS)
        except AttributeError:
            # TODO 會議通知的 From 目前會抓錯
            print("AttributeError: Subject=>", msg.Subject)
            print("msg.SenderEmailAddress==>", msg.SenderEmailAddress)
            return msg.SenderEmailAddress
    else:
        return msg.SenderEmailAddress


def transform_time_format_to_timestamp(received_time):
    # time format is like: "2018-07-13 14:42:13+00:00"
    # TODO Does any recieved time is not +00:00?
    received_time_str = re.sub("\+00:00$", "", str(received_time))
    print(received_time_str)
    dt = datetime.strptime(received_time_str, "%Y-%m-%d %H:%M:%S")
    utctime = calendar.timegm(dt.utctimetuple())
    return utctime


def get_message_id(msg):
    matched = re.findall(r'^Message-ID:.*', msg.PropertyAccessor.GetProperty(PR_TRANSPORT_MESSAGE_HEADERS),
                         flags=re.MULTILINE)[0].strip()
    message_id = re.findall(r"<.*>", matched)[0].strip('>').strip('<')
    return message_id


def parse_message_info(msg):
    d = dict()
    d['message_id'] = get_message_id(msg)
    d['timestamp'] = transform_time_format_to_timestamp(msg.ReceivedTime)
    d['subject'] = msg.Subject
    d['body'] = msg.Body
    d['html_body'] = msg.HTMLBody
    d['_from'] = get_sender_mail_address(msg)
    #TODO fixed in the future
    d['parsable'] = 0
    return d
