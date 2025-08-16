import csv
import glob
import os
import re

from entities.InstagramUser import InstagramUser


class ReadUsers:
    def __init__(self, factory_hub, subdir, pojo, users = []):
        self.export_dir = factory_hub.for_config()['paths']['export_dir']
        self.subdir = subdir
        self.pojo = pojo
        self.users = users

    def execute(self):
        if not os.path.exists(self.export_dir):
            os.makedirs(self.export_dir)

        if self.pojo.username is None or self.pojo.username == "":
            subfolders = [
                name for name in os.listdir(self.export_dir)
                if os.path.isdir(os.path.join(self.export_dir, name))
            ]
            if len(subfolders) == 0:
                raise FileNotFoundError("Not any info about user found in export directory.")
            self.pojo.set_username(subfolders[0])

        user_folder = str(self.export_dir) + "/"\
            + re.sub(r'[^a-zA-Z0-9]', '', str(self.pojo.username))
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        final_export_folder = user_folder + "/" + self.subdir
        if not os.path.exists(final_export_folder):
            os.makedirs(final_export_folder)

        csv_files = glob.glob(os.path.join(final_export_folder, '*.csv'))
        if not csv_files:
            raise FileNotFoundError(f'No CSV files found in directory: {final_export_folder}')
        csv_files.sort()
        latest_file = csv_files[-1]

        users = []
        with open(latest_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                users.append(InstagramUser(
                    user_id = re.sub(r'\s+', ' ', row['User ID']),
                    full_name = re.sub(r'\s+', ' ', row['Full Name'])
                ));

        if self.users is None:
            self.users = []
        self.users[:] = users

        return self.users
