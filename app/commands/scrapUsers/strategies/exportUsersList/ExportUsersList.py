import csv


class ExportUsersList:
    
    def __init__(self, marionette, collection_name, users = []):
        self.marionette = marionette
        self.collection_name = collection_name
        self.users = users

    def execute(self):
        # List of strings to write (as rows)
        data = [
            ["Hello", "World"],
            ["Python", "CSV"],
            ["Export", "Success"]
        ]

        with open("output.csv", mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data)
