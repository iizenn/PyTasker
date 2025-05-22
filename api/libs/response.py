#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   Zhifeng Lin
@Contact :   332886770@qq.com
@Time    :   2025-02-25 09:26:55
@File    :   response.py
@Desc    :

Copyright (c) 2025 by Zhifeng_Lin, All Rights Reserved.
"""

from dataclasses import field, dataclass
from typing import Any
from flask import jsonify, Response as FlaskResponse

from .http_code import HttpCode


@dataclass
class Response:
    code: HttpCode = HttpCode.SUCCESS
    message: str = ""
    data: Any = field(default_factory=dict)


def json_response(body: Response = None) -> FlaskResponse:
    return jsonify(body), 200


def success_json(data: Any = None):
    return json_response(Response(code=HttpCode.SUCCESS, message="", data=data))


def fail_json(data: Any = None):
    return json_response(Response(code=HttpCode.FAIL, message="", data=data))


def not_found_json(data: Any = None):
    return json_response(Response(code=HttpCode.NOT_FOUND, message="", data=data))


def validate_error_json(errors: dict = None):
    first_key = next(iter(errors))
    if first_key is not None:
        msg = errors.get(first_key)[0]
    else:
        msg = ""
    return json_response(Response(code=HttpCode.VALIDATE_ERROR, message=msg, data=[]))


def message(code: HttpCode = None, msg: str = ""):
    return json_response(Response(code=code, message=msg, data={}))


def success_message(msg: str = ""):
    return message(code=HttpCode.SUCCESS, msg=msg)


def fail_message(msg: str = ""):
    return message(code=HttpCode.FAIL, msg=msg)


def not_found_message(msg: str = ""):
    return message(code=HttpCode.NOT_FOUND, msg=msg)
