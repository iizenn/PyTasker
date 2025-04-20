#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-04-20 10:55:32
@File    :   scheduler.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ThreadPoolExecutor
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import models
import importlib

# 初始化调度器，使用 SQLite 持久化
jobstores = {"default": SQLAlchemyJobStore(url="sqlite:///jobs.db")}
executors = {"default": ThreadPoolExecutor(10)}
job_defaults = {"coalesce": False, "max_instances": 1}

scheduler = BackgroundScheduler(
    jobstores=jobstores,
    executors=executors,
    job_defaults=job_defaults,
    timezone="UTC",
)

# 启动时加载数据库中的任务
scheduler.start()


# 通用任务：执行脚本文件
def run_script(script_path):
    with open(script_path, encoding="utf-8") as f:
        code = compile(f.read(), script_path, "exec")
        exec(code, {})


# 通用任务：发送 HTTP 请求
import requests


def send_request(url, method="GET", **kwargs):
    resp = requests.request(method, url, **kwargs)
    # 简单打印，可扩展为存入日志表
    print(f"[{resp.status_code}] {url}")
