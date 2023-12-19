import requests
from modules.utils import record_log
from configs.configs import bot_token, chat_id


class Notification:
    def __init__(self, message: str, title: str = ""):
        self.title: str = title
        self.message = message

    def send_telegram_msg(self):
        base_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
        payload = {
            "chat_id": chat_id,
            "text": self.message,
            "parse_mode": "markdown",
        }

        response = requests.post(base_url, json=payload)
        if response.status_code == 200:
            record_log(log_str=f"Telegram message sent successfully!")
        else:
            record_log(log_str="Failed to send the message.")
