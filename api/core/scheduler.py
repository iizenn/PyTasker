#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-05-22 15:58:06
@File    :   scheduler.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""


import requests


# 通用任务：执行脚本文件
def run_script(script_path):
    with open(script_path, encoding="utf-8") as f:
        code = compile(f.read(), script_path, "exec")
        exec(code, {})


# 通用任务：发送 HTTP 请求
def send_request(url, method="GET", **kwargs):
    resp = requests.request(method, url, **kwargs)
    print(f"[{resp.status_code}] {url}")


# 将函数名映射到实际函数
task_funcs = {
    "script": run_script,
    "request": send_request,
}
