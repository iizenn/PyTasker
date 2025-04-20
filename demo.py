#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Author  :   iizenn
@Contact :   332886770@qq.com
@Time    :   2025-04-20 11:06:04
@File    :   demo.py
@Desc    :

Copyright (c) 2025 by iizenn, All Rights Reserved.
"""

# myscript.py - 示例任务脚本
import datetime
import os

# 获取当前时间并记录到文件
log_path = "./task_logs/demo.log"
os.makedirs(os.path.dirname(log_path), exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
with open(log_path, "a") as f:
    f.write(f"[{timestamp}] Task executed successfully!\n")


print("Script executed! Check demo.log")  # 控制台输出（仅开发调试可见）
