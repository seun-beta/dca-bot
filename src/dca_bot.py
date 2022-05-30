import os
import requests

from apscheduler.schedulers.blocking import BlockingScheduler


from services.log import logger
from services.send_mail import SendEmail
from services.models import Transaction

job = BlockingScheduler()


def buy_crypto():
    quidax_base_url = os.environ.get("QUIDAX_BASE_URL")
    quidax_secret_key = os.environ.get("QUIDAX_SECRET_KEY")
    url = quidax_base_url + "instant_orders"

    from_currency = os.environ.get("FROM_CURRENCY")
    to_currency = os.environ.get("TO_CURRENCY")

    payload = {
        "bid": from_currency,
        "ask": to_currency,
        "type": "buy",
        "total": "5",
        "unit": "ngn",
    }
    headers = {
        "Accept": "application/json",
        "Authorization": "Bearer " + quidax_secret_key,
    }
    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 200:

        logger.error(response.json())
        data = "😞 Could not buy crypto"
        SendEmail.send_email(data)

    else:
        Transaction.create(from_currency="ngn", to_currency="btc", amount=5)
        SendEmail.send_email(response.text)


job.add_job(
    buy_crypto,
    "cron",
    day_of_week="mon-sun",
    hour="17",
    minute="00",
    timezone="Africa/Lagos",
)
job.start()
