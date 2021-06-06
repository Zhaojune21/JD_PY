#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-06-02 21:57
# @Author  : 178
import re, datetime
from telethon import TelegramClient, events
from crontab import CronTab
from JD_PY_config import *


client = TelegramClient(session, api_id, api_hash, proxy=proxy).start(bot_token=bot_token)


def get_time(t):
    logger_rain.debug(t)
    cron_time = []
    for i in t:
        time = re.findall(r'[\d]+', i)
        logger_rain.debug(time)
        cron_time.append(datetime.datetime(int(time[0]), int(time[1]), int(time[2]), int(time[3]), int(time[4])))
    return cron_time


def add_cron(cron, RRAs):
    with CronTab(user=True) as my_cron:
        for i in range(len(RRAs)):
            job = my_cron.new(command=f'echo {RRAs[i]}', comment=RRAs[i])
            job.setall(cron[i])


@client.on(events.NewMessage(chats=[-1001159808620]))
async def monitoringbot(event):
    text = event.message.text
    logger_rain.debug(text)
    if '京豆雨' in text and '开始时间' in text:
        RRAs = re.findall(r'RRA.*', text)
        time = re.findall(r'开始时间.*', text)
        add_cron(get_time(time), RRAs)


if __name__ == '__main__':
    with client:
        client.loop.run_forever()
