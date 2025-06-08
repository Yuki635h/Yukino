"""
📘 Yukino Protocol · Example Call

Minimal example: how to execute one protocol (Yuqi.Protocol.JunZiNonHuman)
from the main semantic definition file (yukino_protocol.json).

This is designed for AI interpreters, copilots, and language behavior simulation tools.
"""

import json

# 加载协议集（从本地 JSON 文件）
with open("yukino_protocol.json", "r", encoding="utf-8") as f:
    protocols = json.load(f)

# 指定协议名与输入
protocol_name = "Yuqi.Protocol.JunZiNonHuman"
input_data = {
    "agent_trait": "noble_like",
    "action_trigger": "external_stimulus"
}

# 执行模拟匹配
for proto in protocols:
    if proto["name"] == protocol_name:
        if input_data == proto["input"]:
            print("✅ Output:", proto["output"])
        else:
            print("⚠️ Input mismatch.")
        break
else:
    print("❌ Protocol not found.")
