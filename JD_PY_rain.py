#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021-06-06 13:20
# @Author  : 178
import json, httpx, asyncio, sys, time
from JD_PY_config import cookies, logger_rain, chat_id, bot_token, SyncProxy, enable_notify
from crontab import CronTab


msg = []


async def receiveRedRain(i, cookie, RRA, client):
    """
    发起 GET 请求
    """
    global res
    params = {
        "functionId": "noahRedRainLottery",
        "body": json.dumps({"actId": RRA}),
        "client": "wh5",
        "clientVersion": "1.0.0",
        "_": round(time.time() * 1000)
    }
    url = 'https://api.m.jd.com/api'
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-cn",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "api.m.jd.com",
        "Referer": f"https://h5.m.jd.com/active/redrain/index.html?id={RRA}&lng=0.000000&lat=0.000000&sid=&un_area=",
        "Cookie": cookie,
        "User-Agent": "JD4iPhone/9.3.5 CFNetwork/1209 Darwin/20.2.0"
        }
    r = await client.get(url, params=params, headers=headers)
    r = r.json()
    account = f'京东账号{i}\n\t\t└'
    if r['subCode'] == '0':
        res = f"{account}领取成功，获得 {r['lotteryResult']['PeasList'][0]['quantity']}京豆\n"
    elif r['subCode'] == '8':
        res = f"{account}领取失败，本场已领过\n"
    else:
        res = f"{account}异常：{r['msg']}\n"
    msg.append(res)
    logger_rain.info(res)


async def main(cookies, RRA):
    """
    执行任务
    """
    async with httpx.AsyncClient(http2=True) as client:
        task_list = []
        i = 0
        try:
            for cookie in cookies:
                i += 1
                r = receiveRedRain(i, cookie, RRA, client)
                task = asyncio.create_task(r)
                task_list.append(task)
            await asyncio.gather(*task_list)
        except Exception as error:
            logger_rain.error(error)


def push(msg):
    url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    data = {
        'chat_id': chat_id,
        'text': '\n'.join(msg),
    }
    headers = {"ontent-Type": "application/x-www-form-urlencoded"}
    with httpx.Client(transport=SyncProxy) as client:
        res = client.post(url, data=data, headers=headers)
    if res.status_code == httpx.codes.OK:
        logger_rain.info('推送成功' + str(res))
    else:
        logger_rain.error('推送失败！' + str(res))


if __name__ == '__main__':
    RRA = sys.argv[1]
    asyncio.run(main(cookies, RRA))
    with CronTab(user=True) as my_cron:
        my_cron.remove_all(comment=RRA)
    if enable_notify == 'True':
        push(msg)
    else:
        logger_rain.info('不推送通知')