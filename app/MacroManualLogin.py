class MacroManualLogin:

    def __init__(self, command_factory, marionette):
        self.command_factory = command_factory
        self.marionette = marionette

    def execute(self):
        self.command_factory.for_verify_login(\
            marionette = self.marionette,\
            is_manual_verification = True).execute()
