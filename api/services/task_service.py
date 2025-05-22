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
from extensions.ext_database import SQLAlchemy


from models import Task, TaskLog


@inject
@dataclass
class TaskService(BaseService):
    db: SQLAlchemy

    def list_task(self):
        return self.db.session.query(Task).all()
