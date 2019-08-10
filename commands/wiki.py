from commands.base_command import SlackCommand
from commands.command import CommandResult
import requests
import urllib.parse

class WikiCommand(SlackCommand):
    def __init__(self, arguments):
        super().__init__(arguments)

    @staticmethod
    def execute_command(arguments) -> CommandResult:
        encoded_query = urllib.parse.urlencode(arguments)
        response = requests.get("https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={}&utf8=&format=json".format(encoded_query)).json()
        result = response['query']['search'][0]['title']



