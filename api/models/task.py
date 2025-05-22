#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 15:54:20
@File    :   task.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from libs.utils import now
from extensions.ext_database import db
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, JSON, event


class Task(db.Model):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    task_type = Column(String(20))  # script or request
    task_args = Column(JSON)
    trigger_type = Column(String(20))  # cron/date/interval
    trigger_args = Column(JSON)
    enabled = Column(Boolean, default=True)
    created_at = Column(DateTime, default=now())
    updated_at = Column(DateTime, default=now(), onupdate=now())
    created_by = Column(String(100))
    updated_by = Column(String(100))
    logs = db.relationship("TaskLog", backref="task", lazy=True)


class TaskLog(db.Model):
    __tablename__ = "task_log"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer, ForeignKey("task.id"), nullable=False)
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    status = Column(String(20))  # success/failure/running
    message = Column(JSON)


@event.listens_for(Task, "before_update")
def update_updated_at(mapper, connection, target):
    target.updated_at = now()
