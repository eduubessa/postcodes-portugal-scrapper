import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from App.Helpers.Config import Config


class Mail:

    def send(self):
        mail = MIMEMultipart("alternative")
        mail["Subject"] = "Postcodes Scrapper - Uma região já está pronta!"
        mail["From"] = Config.get('mail.from')
        mail["To"] = Config.get("mail.to")

        text = """\
        Hi,
        How are you?
        Real Python has many great tutorials:
        www.realpython.com"""

        html = """\
        <html>
          <body>
            <p>Hi,<br>
               How are you?<br>
               <a href="http://www.realpython.com">Real Python</a> 
               has many great tutorials.
            </p>
          </body>
        </html>
        """

        # Turn these into plain/html MIMEText objects
        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        # Add HTML/plain-text parts to MIMEMultipart message
        # The email client will try to render the last part first
        mail.attach(part1)
        mail.attach(part2)

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(Config.get("mail.host"), port=465, context=context) as server:
            server.login(Config.get('mail.username'), Config.get('mail.password'))
            server.sendmail(
                mail["From"], mail["To"], mail.as_string()
            )
