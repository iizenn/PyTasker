#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 16:06:55
@File    :   task_service.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""


from injector import inject
from dataclasses import dataclass

from extensions.ext_apscheduler import scheduler


@inject
@dataclass
class TaskService:

    def list_task(self):
        jobs = []
        for job in scheduler.get_jobs():
            jobs.append(
                {
                    "id": job.id,
                    "func": job.func_ref,
                    "next_run_time": job.next_run_time.isoformat() if job.next_run_time else None,
                }
            )
        return jobs
