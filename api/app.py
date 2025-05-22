#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 10:32:47
@File    :   app.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

import os
from pathlib import Path
from pytasker import PyTasker
from configs.config import Config
from models import *


def create_pytasker() -> PyTasker:
    pytasker = PyTasker("PyTasker")
    pytasker.config.from_object(Config)

    return pytasker


def initialize_extensions(app: PyTasker):
    from extensions import ext_router, ext_error_handler

    extensions = [ext_router, ext_error_handler]
    for ext in extensions:
        ext.init_app(app)

    from extensions.ext_apscheduler import scheduler
    from extensions.ext_migrate import migrate
    from extensions.ext_database import db

    scheduler.init_app(app)
    scheduler.start()
    db.init_app(app)
    migrate.init_app(app, db, directory="api/migration")

    with app.app_context():
        try:
            os.makedirs(Path(Config.SQLALCHEMY_DATABASE_URI.split("///")[-1]).parent, exist_ok=True)
        except OSError:
            pass
        db.create_all()


def create_app():
    app = create_pytasker()
    initialize_extensions(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000)
