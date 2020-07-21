# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from mcpi.minecraft import Minecraft
mc=Minecraft.create()
while True:
    x,y,z=mc.player.getTilePos()
    
    right=mc.getblock(x+1,y-1,z)
    left=mc.getblock(x-1,y-1,z)
    front=mc.getblock(x,y-1,z+1)
    back=mc.getblock(x,y-1,z-1)
    
    if right==8 or left==8 or front==8 or back== 8:
        mc.setblock(x-1,y-1,z-1,x+1,y-1,z+1,79)
    