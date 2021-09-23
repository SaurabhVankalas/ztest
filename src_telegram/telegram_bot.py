import json
import requests
import time
import urllib
import datetime


TOKEN = "735635203:AAFiTqH4gIXBMAHNj9YNIAokMm0ACWdXBfg"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)


def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content


def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js


def get_updates(offset=None):
    url = URL + "getUpdates"
    if offset:
        url += "?offset={}".format(offset)
    js = get_json_from_url(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)


def echo_all(updates):
    for update in updates["result"]:
        text = update["message"]["text"]
        chat = update["message"]["chat"]["id"]
        date = update["message"]["date"]
        # print(update)
        dt = datetime.datetime.fromtimestamp(int(date)).strftime("%Y-%m-%d %H:%M:%S")

        URL = "http://crudapp:8000/data/"

        temp = {"text": text, "date": dt}
        data = json.dumps(temp)
        print(data)
        r = requests.post(url=URL, data=data)
        send_message(text, chat, dt)
        print(f"response from POST: {r}")


def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    print(text, chat_id)
    return (text, chat_id)


def send_message(text, chat_id, dt):
    text = urllib.parse.quote_plus(text)
    # date = urllib.parse.quote_plus(str(date))
    text = text + dt
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)


def main():
    last_update_id = None
    print("starting telegram bot....")
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            echo_all(updates)
        time.sleep(0.5)


if __name__ == "__main__":
    main()
