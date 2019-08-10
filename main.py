import os
import logging
import urllib
from utils.command_parser import *
import requests
import slack

BOT_TOKEN = os.environ["BOT_TOKEN"]
SLACK_URL = "https://slack.com/api/chat.postMessage"
slack_client = slack.WebClient(token=BOT_TOKEN)


def slack_bot(request):
    """Responds to any HTTP request..
    Args:
        request (flask.Request): HTTP request object.
    Returns:
        The response text or any set of values that can be turned into a
        Response object using
        `make_response <http://flask.pocoo.org/docs/1.0/api/#flask.Flask.make_response>`.
    """
    request_json = request.get_json()
    logging.info("Slack Request:: {}".format(request_json))

    slack_event = request_json["event"]

    if "bot_id" in slack_event:
        logging.warn("Ignored bot event")
    else:
        # Get the text of the message the user sent to the bot,
        # and reverse it.
        text = slack_event["text"]
        command = extract_command(text)

        logging.info("Parsed Command :: {}".format(command))

        command_results = execute_command(command)

        logging.info("Command Results:: {}".format(command_results))

        try:
            send_slack_message(slack_event, command_results)
        except Exception as e:
            logging.error("Problem sending slack message: ".format(e))
            return "500"
    return "200 OK"


def send_slack_message(slack_event, command_results):
    """
    Sends message to slack channel
    :param slack_event: Incoming message event
    """
    # Get the ID of the channel where the message was posted.

    channel_id = slack_event["channel"]
    #
    # data = {
    #     'token': BOT_TOKEN,
    #     'channel': channel_id,
    # }
    #
    # if len(command_results.attachments) > 0:
    #     data['attachments'] = command_results.attachments
    # else:
    #     data['text'] = command_results.message_text
    #
    # logging.info('Outgoing Request:: {}'.format(data))

    # requests.post(SLACK_URL, data=data)
    slack_client.chat_postMessage(
        channel=channel_id,
        text=command_results.message_text,
        attachments=command_results.attachments
    )



    # # Construct the HTTP request that will be sent to the Slack API.
    # request = urllib.request.Request(
    #     SLACK_URL,
    #     data=data,
    #     method="POST"
    # )
    # # Add a header mentioning that the text is URL-encoded.
    # request.add_header(
    #     "Content-Type",
    #     "application/x-www-form-urlencoded"
    # )
    #
    # # Fire off the request!
    # urllib.request.urlopen(request).read()
