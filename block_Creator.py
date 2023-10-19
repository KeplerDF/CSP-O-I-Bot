import logging

logging.basicConfig(level=logging.DEBUG)
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import ssl
import certifi
import Error_Messages

from flask import Flask, request

def create_block(type, id_list, url_list):
    if type == "button":
        result = ""
        result =[
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Choose a link"
                        }
                    },
                    button_block(id_list, url_list)
    ]
        return result


def button_block(id, url):
    result = ""
    result = {
                "type": "actions",
                "block_id": id,
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": id
                        },
                        "url": url
                    }
                ]
            }
    return result