# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:35:22 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()

height=10
lenght=10
widht=10

mc.setBlocks(x,y,z,x+widht,y+height,z+lenght,46)
mc.setBlocks(x+1,y+1,z+1,x+widht-1,y+height-1,z+lenght-1,0)

