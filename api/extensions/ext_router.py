#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 10:43:29
@File    :   ext_router.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from injector import Injector
from flask_cors import CORS

from pytasker import PyTasker
from routers import Router


def init_app(app: PyTasker):

    injector = Injector()
    router = injector.get(Router)
    router.register_router(app)

    CORS(
        app,
        resources={
            r"/*": {
                "origins": "*",
                "supports_credentials": True,
                # "methods": ["GET", "POST"],
                # "allow_headers": ["Content-Type"],
            }
        },
    )
