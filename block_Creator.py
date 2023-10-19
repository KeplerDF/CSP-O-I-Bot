import logging

logging.basicConfig(level=logging.DEBUG)
import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import ssl
import certifi
import Error_Messages

from flask import Flask, request


def create_block(type):
    if type == "button":
        result = ""
        result = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Choose a link"
                }
            }
        ]
        return result


def button_block(id, url):
    return [
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": id
                        },
                        "value": id,
                        "url": url,
                        "action_id": "actionId-0"
                    }
                ]
            }
        ]

