#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-04-21 16:10:15
@File    :   models.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from flask_sqlalchemy import SQLAlchemy

# ORM 实例
db = SQLAlchemy()


class JobRecord(db.Model):
    __tablename__ = "apscheduler_jobs"
    id = db.Column(db.String, primary_key=True)
    next_run_time = db.Column(db.Integer)
    job_state = db.Column(db.Text)
