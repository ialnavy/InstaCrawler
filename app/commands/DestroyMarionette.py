class DestroyMarionette:
    """"Command to destroy the Marionette browser session."""

    def __init__(self, marionette):
        self.marionette = marionette


    def execute(self):
        self.marionette.quit()
