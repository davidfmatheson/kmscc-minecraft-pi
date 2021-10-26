from mcpi.minecraft import Minecraft
from time import sleep

mc = Minecraft.create()

pos = mc.player.getPos()
mc.player.setPos(pos.x, pos.y + 100, pos.z)

# while True:
#     x, y, z = mc.player.getPos()
#     sleep(0.1)