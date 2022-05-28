import os
import requests

from services.log import logger
from services.send_mail import SendEmail

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
try:
    response = requests.post(url, json=payload, headers=headers)
    print(response.status_code)

    logger.debug(response.text)
    SendEmail.send_email(response.text)

except response.status_code == 400:
    SendEmail.send_email(response.text)
    print("triggered")
