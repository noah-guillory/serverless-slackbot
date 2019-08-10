from commands import *
import logging

from commands.command import Command, CommandResult


def extract_command(message_text) -> Command:
    logging.info("Message Text:: {}".format(message_text))
    if len(message_text.split('me')) == 1:
        logging.info('Command Not Found ' + message_text)
        return Command(None, None)
    else:
        return Command(message_text.split('me')[0], message_text.split('me')[1])


def execute_command(bot_command) -> CommandResult:
    response = ''
    if bot_command.command is None:
        return CommandResult("I'm not sure what you meant by that")
    elif 'reverse' in bot_command.command:
        response = reverse.ReverseCommand.execute_command(
            bot_command.arguments)
    elif 'gif' in bot_command.command:
        response = gif.GifCommand.execute_command(bot_command.arguments)

    return response
