#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   Zhifeng Lin
@Contact :   332886770@qq.com
@Time    :   2025-02-25 09:11:05
@File    :   http_code.py
@Desc    :   

Copyright (c) 2025 by Zhifeng_Lin, All Rights Reserved. 
"""

from enum import Enum


class HttpCode(str, Enum):

    SUCCESS = "success"
    FAIL = "fail"
    NOT_FOUND = "not_found"
    VALIDATE_ERROR = "validate_error"
