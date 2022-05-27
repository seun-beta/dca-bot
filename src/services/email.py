import requests
import os
from dotenv import load_dotenv


load_dotenv()

from log import logger


class SendEmail:
    def __init__(
        self,
        mailgun_base_url=os.environ.get(""),
        mailgun_api_key=os.environ.get(""),
    ) -> None:
        self.mailgun_base_url = mailgun_base_url
        self.mailgun_api_key = mailgun_api_key

    @staticmethod
    def send_email(data):
        try:
            mailgun_base_url = ""
            api_key = ""
            to = data["to_email"]
            subject = data["email_subject"]
            body = data["email_body"]

            mailing_data = {
                "from": "sender",
                "to": to,
                "subject": subject,
                "text": body,
            }
            response = requests.post(
                mailgun_base_url, auth=api_key, data=mailing_data
            )
        except:
            logger.exception(response.json())
