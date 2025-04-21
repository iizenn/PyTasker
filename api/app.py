#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-04-20 10:55:23
@File    :   app.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

import logging
from logging.handlers import RotatingFileHandler

# --- 日志配置：移除控制台输出，将所有 APScheduler 日志写入文件 ---
# 1. 创建一个文件日志 handler（5MB 自动轮转，最多保留 3 个备份）
file_handler = RotatingFileHandler(
    filename="apscheduler.log", maxBytes=5 * 1024 * 1024, backupCount=3, encoding="utf-8"
)
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s in %(name)s: %(message)s"))

# 2. 删除根 logger 上的所有 StreamHandler（控制台输出）
root_logger = logging.getLogger()
for handler in list(root_logger.handlers):
    if isinstance(handler, logging.StreamHandler):
        root_logger.removeHandler(handler)

# 3. 添加文件 handler
root_logger.addHandler(file_handler)

# 4. 可选：单独调整 APScheduler 相关 logger 的级别
for name in ("apscheduler.scheduler", "apscheduler.executors.default", "apscheduler.jobstores", "apscheduler.triggers"):
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
# ----------------------------------------------------------------------

from flask import Flask, request, jsonify
from flask_apscheduler import APScheduler
from waitress import serve
from apscheduler.triggers.cron import CronTrigger

# 引入数据库模型和调度器配置
from app.models import db
from app.scheduler import task_funcs
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# 初始化数据库与调度器
db.init_app(app)
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


@app.route("/tasks", methods=["GET"])
def list_tasks():
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append(
            {
                "id": job.id,
                "func": job.func_ref,
                "next_run_time": job.next_run_time.isoformat() if job.next_run_time else None,
            }
        )
    return jsonify(jobs)


@app.route("/tasks", methods=["POST"])
def add_task():
    data = request.get_json(force=True)
    job_id = data.get("id")
    func_name = data.get("func")
    args = data.get("args", [])
    cron_params = data.get("cron", {})

    if not job_id or not func_name or not cron_params:
        return jsonify({"error": "Missing 'id', 'func', or 'cron' field"}), 400

    func = task_funcs.get(func_name)
    if not func:
        return jsonify({"error": "func not found"}), 400

    trigger = CronTrigger(**cron_params)
    try:
        scheduler.add_job(id=job_id, func=func, trigger=trigger, args=args, replace_existing=True)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    return jsonify({"status": "added", "job_id": job_id})


@app.route("/tasks/<job_id>", methods=["DELETE"])
def remove_task(job_id):
    try:
        scheduler.remove_job(job_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 404
    return jsonify({"status": "removed", "job_id": job_id})


if __name__ == "__main__":
    # 首次运行时创建表
    with app.app_context():
        db.create_all()
    # 使用 waitress 部署
    serve(app, host="0.0.0.0", port=5000, threads=4)
