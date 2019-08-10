import os

from commands.command import CommandResult
from .base_command import SlackCommand
import requests
import random


class GifCommand(SlackCommand):
    def __init__(self):
        super(GifCommand, self).__init__(self)

    @staticmethod
    def execute_command(arguments):
        search_response = requests.get("https://api.gfycat.com/v1/gfycats/search?search_text={}".format(arguments)).json()
        gifs = search_response['gfycats']

        attachment = {
            'image_url': random.choice(gifs)['max2mbGif'],
            'title': 'gif'
        }
        result = CommandResult()
        result.add_attachment(attachment)
        return result
