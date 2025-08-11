# host.py
import json, subprocess, sys, time

p = subprocess.Popen(
    [sys.executable, "server.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    text=True,
    bufsize=1,
)

def send(obj):
    p.stdin.write(json.dumps(obj) + "\n")
    p.stdin.flush()

def recv():
    line = p.stdout.readline()
    return json.loads(line) if line else None

# 0) initialize（必須：clientInfo を含める）
send({
    "jsonrpc": "2.0",
    "id": "init-1",
    "method": "initialize",
    "params": {
        "protocolVersion": "2024-11-05",
        "clientInfo": {"name": "demo-host", "version": "0.1.0"},
        "capabilities": {}
    }
})
print(">> initialize")
print(recv())  # ここで serverInfo / capabilities が返る

# 1) initialized 通知（id なし）
send({
    "jsonrpc": "2.0",
    "method": "notifications/initialized",
    "params": {}
})
print(">> notifications/initialized (sent)")

# 2) ツール一覧
send({"jsonrpc": "2.0", "id": "1", "method": "tools/list", "params": {}})
print(">> tools/list")
print(recv())

# 3) add(2,3)
send({
    "jsonrpc": "2.0", "id": "2", "method": "tools/call",
    "params": {"name": "add", "arguments": {"a": 2, "b": 3}}
})
print(">> add")
print(recv())

# 4) echo("hello")
send({
    "jsonrpc": "2.0", "id": "3", "method": "tools/call",
    "params": {"name": "echo", "arguments": {"text": "hello"}}
})
print(">> echo")
print(recv())

time.sleep(0.2)
p.terminate()
