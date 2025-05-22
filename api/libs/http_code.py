#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 10:41:06
@File    :   http_code.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from enum import Enum


class HttpCode(str, Enum):

    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not_found"
    VALIDATE_ERROR = "validate_error"
