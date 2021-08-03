import imaplib
from App.Helpers.Config import Config

class Mail:

    def __init__(self):
        self.config = Config()
        self.__imap = imaplib.IMAP4_SSL(self.config.get('mail.host'))
        self.__imap