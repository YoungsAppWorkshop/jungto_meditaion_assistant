#!/usr/bin/env python3
import datetime
from dotenv import load_dotenv
import os
import pytz
import subprocess

# Import Environment variables
load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")
is_prod = os.getenv("IS_PROD")
band_key = os.getenv(
    "BAND_KEY") if is_prod == "TRUE" else os.getenv("BAND_KEY_DEV")

# Calculate datetime
day_of_week = ['월', '화', '수', '목', '금', '토', '일']
seoul = pytz.timezone('Asia/Seoul')
dt_now = seoul.localize(datetime.datetime.now())
dt_start = seoul.localize(datetime.datetime(2019, 6, 16, dt_now.hour,
                                            dt_now.minute, dt_now.second))
tdelta = datetime.timedelta(days=(1 if dt_now.hour >= 12 else 0))
dt_target = dt_now + tdelta
days = dt_target - dt_start

# Fill out Payload
uri = "http://openapi.band.us/v2.2/band/post/create"
content = f"""
[불기 {dt_target.year + 544}년 {dt_target.month}월 {dt_target.day}일 {day_of_week[dt_target.weekday()]}요일]
정토행자 만일결사 중
제9-9차 천일결사 {days.days}일째 기도
🌸 나는 행복한 수행자입니다 🌸

천일결사 기도음원
http://m.jungto.org/1000days.php
"""
payload = (
    f'curl -d "access_token={access_token}&band_key={band_key}'
    f'&content={content}" {uri}'
)


# Send API Request
def main():
    print("------------------------------------------------------------------------")
    print("Sending Request at:", dt_now)
    print("Result:")

    subprocess.call(payload, shell=True)


if __name__ == '__main__':
    main()
