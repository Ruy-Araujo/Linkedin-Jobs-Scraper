import os
import json
import logging


def create_folder(path):
    if not os.path.isdir(path):
        os.makedirs(path)


def save_data(path, file_name, blob):
    if not os.path.isdir(path):
        os.makedirs(path)

    if 'json' in file_name:
        with open(f"{path}/{file_name}", "w", encoding="utf-8") as file:
            json.dump(blob, file, indent=2, ensure_ascii=False)


def append_data(path, file_name, blob):
    logging.info(f"Appending data to file {file_name}...")

    if not os.path.isdir(path):
        os.makedirs(path)

    if path.endswith("/"):
        path = path[:-1]

    try:
        with open(f"{path}/{file_name}", "r", encoding="utf-8") as file:
            data = json.load(file)
    except:
        data = []

    data.extend(blob)

    with open(f"{path}/{file_name}", "w", encoding="utf-8") as file:
        json.dump(blob, file, indent=2, ensure_ascii=False)
