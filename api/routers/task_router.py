#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 10:48:26
@File    :   task_router.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from flask import Blueprint


def test():
    return 200


from injector import inject
from dataclasses import dataclass
from libs.utils import get_project_route
from handlers import TaskHandler


@inject
@dataclass
class TaskRouter:

    task_handler: TaskHandler

    def __post_init__(self):
        self.bp = Blueprint("task", __name__, url_prefix=get_project_route() + "/task")

        self.bp.add_url_rule("/", "list_task", self.task_handler.list_task)
        self.bp.add_url_rule("/", "create_task", self.task_handler.create_task, methods=["POST"])

        self.bp.add_url_rule("/<int:id>", "get_task", test)
        self.bp.add_url_rule("/<int:id>", "update_task", test, methods=["POST"])

        self.bp.add_url_rule("/<int:id>/delete", "delete_task", test, methods=["POST"])

        self.bp.add_url_rule("/<int:id>/enable", "enable_task", test, methods=["POST"])
        self.bp.add_url_rule("/<int:id>/disable", "disable_task", test, methods=["POST"])

        self.bp.add_url_rule("/<int:id>/run", "run_task_once", test, methods=["POST"])

        self.bp.add_url_rule("/<int:id>/log", "get_task_log", test)
