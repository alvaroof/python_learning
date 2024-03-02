# -*- coding: utf-8 -*-
"""This code snippet is separated from the rest, but is still part of task 1."""

import sys

import pandas as pd
from db_tools import start_connection, upload_to_db
from project import BASE_DIR


def upload_to_db():
    """Upload system information to database."""
    with open(BASE_DIR / "config.yaml") as file:
        config = yaml.safe_load(file)
        username = config["credentials"]["username"]
        pwd = config["credentials"]["password"]
        db = config["credentials"]["database"]

    version_info_dict = {
        "major": sys.version_info.major,
        "minor": sys.version_info.minor,
        "micro": sys.version_info.micro,
        "releaselevel": sys.version_info.releaselevel,
        "serial": sys.version_info.serial,
    }

    version_info_df = pd.DataFrame([version_info_dict])

    conn = start_connection(db, username, pwd)
    upload_to_db(conn, version_info_df)
