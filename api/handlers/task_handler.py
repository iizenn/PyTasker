#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 14:31:06
@File    :   task_handler.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from injector import inject
from dataclasses import dataclass
from libs.response import success_json, validate_error_json
from services import TaskService
from flask import request, jsonify, abort


@inject
@dataclass
class TaskHandler:
    task_service: TaskService

    def list_task(self):
        resp = self.task_service.list_task()
        return success_json(resp)

    def create_task(self):
        data = request.get_json(force=True)
        task = self.task_service.create_task(data)
        return jsonify(task), 201
