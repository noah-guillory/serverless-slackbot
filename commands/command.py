class Command(object):
    def __init__(self, command, arguments):
        self.command = command
        self.arguments = arguments

    def __str__(self):
        return "(command={}, arguments={})".format(self.command, self.arguments)




class CommandResult(object):
    def __init__(self, message=None):
        self.message_text = message
        self.attachments = []

    def add_attachment(self, attachment):
        self.attachments.append(attachment)

    def __str__(self):
        return "(message_text={}, attachments={})".format(self.message_text, self.attachments)
