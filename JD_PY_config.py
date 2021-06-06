#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-06-06 16:24
# @Author  : 178
import os, logging, logging.config
from configparser import ConfigParser
from httpx_socks import SyncProxyTransport

# 定义目录
path = os.path.dirname(os.path.realpath(__file__))
conf_path = path + '/config'
log_path = path + '/logs'
log_file = log_path + '/JD_PY.log'
conf_file = conf_path + '/JD_PY_BOT.conf'
session = conf_path + '/JD_PY_BOT'

# 写入日志路径
config = ConfigParser()
config.read(conf_file, encoding='utf-8')
with open(conf_file, 'w', encoding='UTF-8') as f:
    config['handler_fileHandler']['args'] = f'("{log_file}", "a", "utf-8")'
    config.write(f)

# 读取配置
logging.config.fileConfig(conf_file)
logger_rain = logging.getLogger('rain')
logger_JD_PY = logging.getLogger('JD_PY')
cookies = config.get('jd', 'cookies').split('&')
chat_id = int(config.get('bot', 'chat_id'))
bot_token = config.get('bot', 'bot_token')
api_id = int(config.get('bot', 'api_id'))
api_hash = config.get('bot', 'api_hash')
enable_proxy = config.get('enable', 'proxy')
enable_proxy_user = config.get('enable', 'proxy_user')
enable_notify = config.get('enable', 'notify')
if enable_proxy == 'True':
    if enable_proxy_user == 'True':
        proxy = {
            'proxy_type': config.get('proxy', 'proxy_type'),
            'addr': config.get('proxy', 'addr'),
            'port': int(config.get('proxy', 'port')),
            'username': config.get('proxy', 'username'),
            'password': config.get('proxy', 'password'),
        }
        SyncProxy = SyncProxyTransport.from_url(f"{proxy['proxy_type']}://{proxy['username']}:{proxy['password']}@{proxy['addr']}:{proxy['port']}")
    else:
        proxy = {
            'proxy_type': config.get('proxy', 'proxy_type'),
            'addr': config.get('proxy', 'addr'),
            'port': int(config.get('proxy', 'port')),
        }
        SyncProxy = SyncProxyTransport.from_url(f"{proxy['proxy_type']}://{proxy['addr']}:{proxy['port']}")
