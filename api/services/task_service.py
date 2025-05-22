#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 14:42:13
@File    :   task_service.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""


from injector import inject
from dataclasses import dataclass
from .base_service import BaseService
from extensions.ext_database import db
from libs.utils import now
from models import Task, TaskLog


from extensions.ext_apscheduler import scheduler
import json
from core.scheduler import load_tasks


@inject
@dataclass
class TaskService(BaseService):

    def list_task(self):
        print(Task.query.all())
        return []

    def create_task(self, data: dict) -> dict:
        data["trigger_args"] = json.dumps(data.get("trigger_args"))
        data["task_args"] = json.dumps(data.get("task_args"))
        t = Task(**data)
        db.session.add(t)
        db.session.commit()
        load_tasks()
        return t.__dict__
