#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 10:40:11
@File    :   ext_error_handler.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""


import os
from flask import Flask

from libs.exception import CustomException
from libs.response import Response, json_response
from libs.http_code import HttpCode


def init_app(app: Flask):
    def _register_error_handler(error: Exception):
        if isinstance(error, CustomException):
            return json_response(
                Response(
                    code=error.code,
                    message=error.message,
                    data=error.data if error.data is not None else [],
                )
            )

        if app.debug or os.getenv("FLASK_ENV") == "development":
            raise error
        else:
            return json_response(
                Response(
                    code=HttpCode.FAIL,
                    message=str(error),
                    data=[],
                )
            )

    app.register_error_handler(Exception, _register_error_handler)
