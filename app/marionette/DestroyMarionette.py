class DestroyMarionette:
    """"Command to destroy the Marionette browser session."""

    def __init__(self, marionette):
        self.marionette = marionette


    def execute(self):
        print(r"""
[InstaCrawler] Destroying marionette...
""")
        self.marionette.quit()
