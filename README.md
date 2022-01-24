# Synopsis

This is just a small little Python app to get weekly Happy Monday Deals from https://www.gambody.com

More info here: https://www.gambody.com/blog/happy-monday-update/

The script is hardcoded to send the results via Gmail. Feel free to change in any way you feel right.

# Usage

Set your Gmail credentials:

```
export GMAIL_USER="jane.doe@gmail.com"
export GMAIL_PASSWORD=$(echo 'P@$$W0rd'|base64)
export GMAIL_SENDER="jane.doe@gmail.com"
export GMAIL_RECIPIENTS="jane.doe@gmail.com,john.doe@gmail.com"
```
