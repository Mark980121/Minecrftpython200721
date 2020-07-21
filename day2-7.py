# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:13:11 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc=Minecraft.create()
username=input("請輸入名字:")
while True:
    messge=input("請輸入訊息:")

    mc.postToChat("["+username+"]"+messge)
