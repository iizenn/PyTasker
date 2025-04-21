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

from waitress import serve
from flask import Flask, request, jsonify
from scheduler import scheduler, run_script, send_request
from apscheduler.triggers.cron import CronTrigger

app = Flask(__name__)


@app.route("/tasks", methods=["GET"])
def list_tasks():
    jobs = []
    for job in scheduler.get_jobs():
        jobs.append(
            {
                "id": job.id,
                "func": job.func_ref,
                "next_run_time": str(job.next_run_time),
            }
        )
    return jsonify(jobs)


@app.route("/tasks", methods=["POST"])
def add_task():
    """
    JSON 示例：
    {
      "id": "job1",
      "func": "run_script",  # 或 send_request
      "args": ["./myscript.py"],
      "cron": {"minute": "*/5"}
    }
    """
    data = request.json
    job_id = data["id"]
    func_name = data["func"]
    args = data.get("args", [])

    # 构造触发器
    cron_params = data["cron"]
    trigger = CronTrigger(**cron_params)

    # 获取函数引用
    func = globals().get(func_name)
    if not func:
        return jsonify({"error": "func not found"}), 400

    scheduler.add_job(func, trigger, args=args, id=job_id, replace_existing=True)
    return jsonify({"status": "added", "job_id": job_id})


@app.route("/tasks/<job_id>", methods=["DELETE"])
def remove_task(job_id):
    scheduler.remove_job(job_id)
    return jsonify({"status": "removed", "job_id": job_id})


if __name__ == "__main__":
    # Flask 服务和调度器共同运行
    # app.run(host="0.0.0.0", port=5000)
    serve(app, host="0.0.0.0", port=5000, threads=4)
