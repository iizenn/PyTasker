#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-04-21 16:18:05
@File    :   config.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""


class Config:
    # APScheduler 配置
    SCHEDULER_API_ENABLED = True
    SCHEDULER_JOBSTORES = {"default": {"type": "sqlalchemy", "url": "sqlite:///jobs.db"}}
    SCHEDULER_EXECUTORS = {
        "default": {
            # 使用 ThreadPoolExecutor
            "class": "apscheduler.executors.pool:ThreadPoolExecutor",
            "max_workers": 10,
        }
    }
    SCHEDULER_JOB_DEFAULTS = {"coalesce": False, "max_instances": 1}
    # 数据库配置（Flask-SQLAlchemy）
    SQLALCHEMY_DATABASE_URI = "sqlite:///jobs.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
