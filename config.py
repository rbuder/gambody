import os
config = {
    "username": os.getenv('GMAIL_USER'),
    "password": os.getenv('GMAIL_PASSWORD'), # base64 
    "sender": os.getenv('GMAIL_SENDER'),
    "receivers": os.getenv('GMAIL_RECIPIENTS').split(',')
}