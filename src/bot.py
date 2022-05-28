import os
import requests

from services.log import logger
from services.send_mail import SendEmail
from services.models import Transaction

quidax_base_url = os.environ.get("QUIDAX_BASE_URL")
quidax_secret_key = os.environ.get("QUIDAX_SECRET_KEY")
url = quidax_base_url + "instant_orders"

payload = {
    "bid": "ngn",
    "ask": "btc",
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
