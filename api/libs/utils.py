#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 10:41:20
@File    :   utils.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""


import os
from marshmallow import ValidationError
from dateutil import tz
from datetime import datetime


def get_project_route():
    return os.getenv("PROJECT_NAME", "/gpp-api-mlmgt")


def not_empty_string(value: str, field_name="field_name"):
    if not isinstance(value, str) or not value.strip():
        raise ValidationError(f"{field_name} can not be blank")


def now():
    return datetime.now(tz.gettz(os.getenv("TIMEZONE", "Asia/Shanghai")))
