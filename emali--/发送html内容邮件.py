#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/1/4 0004  17:37
#Author:chao
import smtplib, time, os
from email.mime.text import MIMEText
from email.header import Header

def send_email_html(file):
    # 1-配置邮箱属性
    # 2-发送邮箱
