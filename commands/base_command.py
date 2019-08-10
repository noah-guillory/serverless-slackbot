from abc import ABC, abstractstaticmethod

from commands.command import CommandResult


class SlackCommand(ABC):
    def __init__(self, arguments):
        self.arguments = arguments
        super().__init__()

    @staticmethod
    def execute_command(arguments) -> CommandResult:
        pass
