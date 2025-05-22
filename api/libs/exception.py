#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 10:41:01
@File    :   exception.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""


from dataclasses import field
from typing import Any
from .http_code import HttpCode


class CustomException(Exception):
    code: HttpCode = HttpCode.FAIL
    message: str = ""
    data: Any = field(default_factory=dict)

    def __init__(self, message: str = None, data: Any = None):
        super().__init__()
        self.message = message
        self.data = data


class FailException(CustomException):
    pass


class NotFoundException(CustomException):
    code = HttpCode.NOT_FOUND


class ValidateErrorException(CustomException):
    code = HttpCode.VALIDATE_ERROR
