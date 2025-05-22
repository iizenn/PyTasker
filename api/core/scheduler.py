#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 15:26:50
@File    :   scheduler.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""


from extensions.ext_apscheduler import scheduler
from extensions.ext_database import db
from models import Task
from core.task_runner import run_task
import json
import pytz
from flask import current_app


def load_tasks():
    # 清除原有任务
    scheduler.remove_all_jobs()
    timezone = pytz.timezone(current_app.config["TIMEZONE"])

    tasks = Task.query.filter_by(enabled=True).all()
    for t in tasks:
        trigger_args = json.loads(t.trigger_args)
        scheduler.add_job(
            id=str(t.id),
            func=run_task,
            args=[t.id],
            trigger=t.trigger_type,
            replace_existing=True,
            timezone=timezone,
            **trigger_args
        )


# @scheduler.task("interval", id="reload_tasks", seconds=60)
def reload_tasks():
    # with scheduler.app.app_context():
    #     load_tasks()
    load_tasks()