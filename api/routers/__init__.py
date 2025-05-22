#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 16:02:46
@File    :   __init__.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from injector import inject
from dataclasses import dataclass
from pytasker import PyTasker
from .task_router import TaskRouter


@inject
@dataclass
class Router:
    task_router: TaskRouter

    def register_router(self, app: PyTasker):
        app.register_blueprint(self.task_router.bp)
