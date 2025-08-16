import csv
from datetime import datetime
import os
import re


class ExportUsers:
    def __init__(self, factory_hub, subdir, pojo, users = []):
        self.export_dir = factory_hub.for_config()['paths']['export_dir']
        self.subdir = subdir
        self.pojo = pojo
        self.users = users

    def execute(self):
        if not os.path.exists(self.export_dir):
            os.makedirs(self.export_dir)

        user_folder = str(self.export_dir) + "/"\
            + re.sub(r'[^a-zA-Z0-9]', '', str(self.pojo.username))
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        final_export_folder = user_folder + "/" + self.subdir
        if not os.path.exists(final_export_folder):
            os.makedirs(final_export_folder)
        
        export_file_name = str(datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + '.csv'
        with open(final_export_folder + "/" + export_file_name, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames = ['User ID', 'Full Name'])
            writer.writeheader()
            writer.writerows([user.as_dict() for user in self.users])
