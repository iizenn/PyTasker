#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 15:59:10
@File    :   ext_apscheduler.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = APScheduler(scheduler=BackgroundScheduler(daemon=True))
