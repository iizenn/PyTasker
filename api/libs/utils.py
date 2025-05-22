#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 15:56:35
@File    :   utils.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""
import os
from dateutil import tz
from datetime import datetime


def get_project_route():
    return os.getenv("PROJECT_NAME", "/gpp-pytasker")

def now():
    return datetime.now(tz.gettz(os.getenv("TIMEZONE", "Asia/Shanghai")))
