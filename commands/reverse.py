from commands.base_command import SlackCommand
from commands.command import CommandResult


class ReverseCommand(SlackCommand):
    def __init__(self, arguments):
        super().__init__(arguments)

    @staticmethod
    def execute_command(arguments) -> CommandResult:
        return CommandResult(arguments[::-1])
