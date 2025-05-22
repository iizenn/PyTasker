#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 12:58:36
@File    :   config.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent.parent.as_posix()


def get_database_uri():
    url = os.getenv("DATABASE_URL", f"sqlite:///{BASE_DIR}/instance/pytasker.db")
    return url


class Config:
    SCHEDULER_API_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 1}
    TIMEZONE = "Asia/Shanghai"
