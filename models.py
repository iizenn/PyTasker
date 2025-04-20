#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-04-20 10:55:28
@File    :   models.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class JobRecord(Base):
    __tablename__ = "apscheduler_jobs"
    id = Column(String, primary_key=True)
    next_run_time = Column(Integer)
    job_state = Column(Text)
