# 配置文件说明

```
[bot]
chat_id = 123456 # 你的chat_id
bot_token = 1223456:abcdefg # 你的bot_token
api_id = 123456 # 你的api_id
api_hash = abc # 你的api_hash

[jd]
cookies = pt_key=xxxx;pt_pin=zzzz;&pt_key=aaaa;pt_pin=bbbb; # 京东cookie，多个cookie请用&隔开

[enable]
proxy = True # 代理开关，True代表代理，False代表直连
proxy_user = True # 代理验证，True代表开启代理验证，False代表关闭代理验证
notify = True # 通知开关

[proxy]
proxy_type = socks5 # 代理类型
addr = 0.0.0.0 # 代理ip
port = 1234 # 代理端口
username = username # 用户名，用于验证，没有不用填
password = password # 密码，用于验证，没有不用填

[loggers]
keys = root,rain,JD_PY # 日志，别动

[handlers]
keys = fileHandler,consoleHandler # 日志，别动

[formatters]
keys = simpleFormatter # 日志，别动

[logger_root]
level = ERROR # root日志等级，一般不用动
handlers = consoleHandler,fileHandler # 日志，别动

[logger_rain]
level = INFO # rain日志等级，一般不用动
handlers = consoleHandler,fileHandler # 日志，别动
qualname = rain # 日志，别动
propagate = 0 # 日志，别动

[logger_JD_PY]
level = INFO # JD_PY日志等级，一般不用动
handlers = consoleHandler,fileHandler # 日志，别动
qualname = JD_PY # 日志，别动
propagate = 0 # 日志，别动

[handler_consoleHandler]
class = StreamHandler # 日志，别动
args = (sys.stdout,) # 日志，别动
level = DEBUG # 日志等级，一般不用动
formatter = simpleFormatter # 日志，别动

[handler_fileHandler]
class = FileHandler # 日志，别动
args = # 日志路径以及编码和写入方式，自动生成
level = DEBUG # 日志等级，一般不用动
formatter = simpleFormatter # 日志，别动

[formatter_simpleFormatter]
format = %(asctime)s | %(levelname)-8s | %(filename)s[:%(lineno)-3d]  |  %(message)s # 日志格式，可按需要自定义
```
