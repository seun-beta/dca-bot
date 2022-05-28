import requests
import os

from services.log import logger


class SendEmail:
    @staticmethod
    def send_email(data):
        try:

            mailgun_base_url = os.environ.get("MAILGUN_BASE_URL")
            mailgun_api_key = os.environ.get("MAILGUN_API_KEY")
            sender = os.environ.get("SENDER")
            reciever = os.environ.get("RECIEVER")

            mailing_data = {
                "from": sender,
                "to": reciever,
                "subject": "DCA Bot",
                "text": data,
            }
            response = requests.post(
                mailgun_base_url,
                auth=("api", mailgun_api_key),
                data=mailing_data,
            )
            logger.debug(response.text)
        except:
            logger.exception(response.text)
