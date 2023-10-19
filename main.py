import logging
import os
import time
from typing import List, Any

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import ssl
import certifi
import Error_Messages
import block_Creator

from flask import Flask, request

logging.basicConfig(level=logging.DEBUG)

app = Flask('SlackReceiver')


@app.route('/slack/message', methods=['POST'])
def incoming_slack_message():
    req = request.get_json()
    return 'action successful'


@app.route('/slack/options', methods=['POST', 'OPTIONS'])
def incoming_slack_options():
    return 'ok'


slack_token = os.environ["SLACK_BOT_TOKEN"]
ssl_context = ssl.create_default_context(cafile=certifi.where())
client = WebClient(token=slack_token, ssl=ssl_context)


def run():
    try:
        f = open("SlackActive.txt", "x")
        f.write("C059ZLLFFHB, 1")
        f.close()

        f2 = open("KeywordMap.txt", "x")
        f2.write(
            "O+I, https://confluence.workday.com/display/ADOPT/CSP%3A+Observability+and+Insights+%28prev.+Product+Adoption%29+Home+Page")
        f2.close()

    except:
        print(Error_Messages.process_error(3))



    x = []
    y = []

    f = open("SlackActive.txt", "r")
    channel = f.readline()
    x = channel.split(", ")
    f.close()

    idlist = ["O+I", "Slackbot Demo"]
    urllist = ["https://confluence.workday.com/display/ADOPT/CSP%3A+Observability+and+Insights+%28prev.+Product+Adoption%29+Home+Page", "https://docs.google.com/presentation/d/1IHx06KGax56RJjBaYoDeWRU4A7umHhFOAWZkJpPU37A/edit#slide=id.g287a19790da_0_73"]

    ''''
    f2 = open("KeywordMap.txt", "r")
    channel2 = f2.readline()
    
    y.append(idlist)
    y.append(urllist)


    f2.close()
    '''''

    try:
        response = client.chat_postMessage(
            channel="C059ZLLFFHB",
            blocks=block_Creator.create_block("button")
        )

    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response[Error_Messages.process_error(0)]  # str like 'invalid_auth', 'channel_not_found'
    append_button(idlist, urllist)

     # str like 'invalid_auth', 'channel_not_found'



def append_button(ids, urls):
    i = 0
    while i < len(ids):
        id = ids[i]
        url = urls[i]
        i = i + 1
        try:
            response = client.chat_postMessage(
                channel="C059ZLLFFHB",
                blocks=block_Creator.button_block(id, url)
            )

        except SlackApiError as e:
            # You will get a SlackApiError if "ok" is False
            assert e.response[Error_Messages.process_error(0)]




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
    app.run('0.0.0.0', 8088, debug=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
