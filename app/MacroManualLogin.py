from app.commands.CommandFactory import CommandFactory


class MacroManualLogin:

    def execute(self):
        marionette = CommandFactory.for_create_marionette().execute()
        CommandFactory.for_verify_login(\
            marionette = marionette,\
            is_manual_verification = True).execute()
