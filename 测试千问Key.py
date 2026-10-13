# -*- coding: utf-8 -*-
"""
测试你的阿里云百炼(通义千问)API Key 是否可用。
运行方式：把此文件放在客户跟进工作台.html 同目录，双击运行即可。
"""
import json
import urllib.request
import urllib.error

KEY = input("请粘贴你的千问 API Key（sk-开头）: ").strip()
URL = "https://dashscope.aliyuncs.com/compatible-mode/v1/chat/completions"
BODY = {
    "model": "qwen-plus",
    "messages": [{"role": "user", "content": "hi，请回复一句简短的话"}]
}

req = urllib.request.Request(
    URL,
    data=json.dumps(BODY, ensure_ascii=False).encode("utf-8"),
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + KEY
    },
    method="POST"
)

print("\n正在请求千问接口...")
try:
    with urllib.request.urlopen(req, timeout=30) as resp:
        print("HTTP 状态:", resp.status, "(Key 可用)")
        data = json.loads(resp.read().decode("utf-8"))
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        print("模型回复:", content)
except urllib.error.HTTPError as e:
    print("HTTP 错误:", e.code)
    print("详情:", e.read().decode("utf-8"))
except Exception as e:
    print("请求失败:", e)

input("\n按回车键退出...")
