#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 15:49:42
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
    # APScheduler 配置
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 1}
    # SCHEDULER_EXECUTORS = {"default": {"class": "apscheduler.executors.pool:ThreadPoolExecutor", "max_workers": 10}}
    SCHEDULER_JOBSTORES = {"default": {"type": "sqlalchemy", "url": get_database_uri()}}

    # 数据库配置（Flask-SQLAlchemy）
    SQLALCHEMY_DATABASE_URI = get_database_uri()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    TIMEZONE = "Asia/Shanghai"
