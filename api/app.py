#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 15:48:16
@File    :   app.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

from pytasker import PyTasker
from configs.config import Config
from extensions.ext_database import db
from extensions.ext_APScheduler import scheduler
from extensions.ext_router import init_app as init_router
from models import *


def create_pytasker() -> PyTasker:
    pytasker = PyTasker("PyTasker")
    pytasker.config.from_object(Config)

    return pytasker


def create_app():
    app = create_pytasker()

    db.init_app(app)

    with app.app_context():
        db.create_all()

    scheduler.init_app(app)
    scheduler.start()
    init_router(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
