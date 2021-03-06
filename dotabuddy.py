# Dota2 Rosh Buddy 1.0
# Author:   Kean Jafari
# Project:  Dota2Buddy

import sys
import pyperclip

def usage():
    print('Usage: py dotabuddy.py')

def getRoshTime(timeOfDeath):
    roshRespawnLow = convertToTime(str(int(timeOfDeath) + 800))
    roshRespawnHigh = convertToTime(str(int(timeOfDeath) + 1100))
    ageisExpire = convertToTime(str(int(timeOfDeath) + 500))
    
    ret = 'Aegis expires {} | Rosh respawns between {} and {}'.format(ageisExpire, roshRespawnLow, roshRespawnHigh)
    return ret

def convertToTime(time):
    if len(time) == 3:
        ret = '{}:{}'.format(time[0:1], time[1:3])
    elif len(time) == 4:
        ret = '{}:{}'.format(time[0:2], time[2:4])
    return ret

pyperclip.copy(getRoshTime(pyperclip.paste()))