#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 15:14:19
@File    :   task_runner.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""


import subprocess
import requests
from extensions.ext_database import db
from models import TaskLog
from libs.utils import now
import json


def run_task(task_id: int):
    log = TaskLog(task_id=task_id, start_time=now(), status="running")
    db.session.add(log)
    db.session.commit()

    task = db.session.query(TaskLog).get(log.id)
    try:
        # 根据 Task.task_type 决定执行逻辑
        from models import Task

        t = Task.query.get(task_id)
        if t.task_type == "script":
            subprocess.run(["python", t.task_args], check=True)
        else:  # request
            cfg = json.loads(t.task_args)
            requests.request(**cfg)
        log.status = "success"
        log.message = "执行成功"
    except Exception as e:
        log.status = "failure"
        log.message = str(e)
    finally:
        log.end_time = now()
        db.session.commit()
