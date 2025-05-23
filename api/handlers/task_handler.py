#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 16:05:58
@File    :   task_handler.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from injector import inject
from dataclasses import dataclass
from libs.response import success_json, validate_error_json
from services import TaskService

from flask import Flask, request, jsonify
from apscheduler.triggers.cron import CronTrigger
from core.scheduler import task_funcs

from extensions.ext_apscheduler import scheduler


@inject
@dataclass
class TaskHandler:
    task_service: TaskService

    def list_task(self):
        resp = self.task_service.list_task()
        return success_json(resp)

    def create_task(self):
        data = request.get_json(force=True)
        id = data.get("id")
        name = data.get("name")
        task_type = data.get("task_type")
        task_args = data.get("task_args", [])
        trigger_type = data.get("trigger_type")
        trigger_args = data.get("trigger_args", {})

        func = task_funcs.get(task_type)
        if not func:
            return jsonify({"error": "func not found"}), 400

        trigger = CronTrigger(**trigger_args)
        try:
            scheduler.add_job(id=id, func=func, trigger=trigger, args=task_args, replace_existing=True)
        except Exception as e:
            return jsonify({"error": str(e)}), 500

        return jsonify({"status": "added", "job_id": id}), 200

    def delete_task(self, id: int):
        print(id)
        try:
            scheduler.remove_job(id)
        except Exception as e:
            return jsonify({"error": str(e)}), 404
        return jsonify({"status": "removed", "job_id": id})
