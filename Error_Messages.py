from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import ssl
import certifi

from flask import Flask, request

def process_error(message):
    if message == 0:
        return 'Error: Invalid Authentication / The Channel is inaccessible'
    elif message == 1:
        return 'Error: There are no links to be displayed'
    elif message == 2:
        return 'Error: You cannot enter this value'
    elif message == 3:
        return 'Error: File Already Exists'

def generic_process_error():
    return 'An Error has occured with this app'