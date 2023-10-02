import logging
import os
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


def run():
    try:
        f = open("SlackActive.txt", "x")
        f.write("C059ZLLFFHB, 1")
        f.close()

        f2 = open("KeywordMap.txt", "x")
        f.write(
            "O+I, https://confluence.workday.com/display/ADOPT/CSP%3A+Observability+and+Insights+%28prev.+Product+Adoption%29+Home+Page /n"
            "CSP: O+I - App Usage Metrics, https://confluence.workday.com/pages/viewpage.action?pageId=1723141183 /n"
            "Observability - AUM Dashboard Review Sessions, https://confluence.workday.com/display/ADOPT/Observability+-+AUM+Dashboard+Review+Sessions /n")
        f.close()

    except:
        print(Error_Messages.process_error(3))

    slack_token = os.environ["SLACK_BOT_TOKEN"]
    ssl_context = ssl.create_default_context(cafile=certifi.where())
    client = WebClient(token=slack_token, ssl=ssl_context)

    x = []
    y = []

    f = open("SlackActive.txt", "r")
    channel = f.readline()
    x = channel.split(", ")
    f.close()

    f2 = open("KeywordMap.txt", "r")
    channel = f.readline()

    for n in f:
        y += channel.split(", ")

    f.close()

    try:
        response = client.chat_postMessage(
            channel=x[0],
            unfurl_links=True,
            blocks=block_Creator.create_block("button", y[0], y[1]),
            text="Hello I am O&I Bot " "\n"
        )

    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response[Error_Messages.process_error(0)]  # str like 'invalid_auth', 'channel_not_found'


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run()
    app.run('0.0.0.0', 8088, debug=False)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
