from __future__ import absolute_import
from ogame.constants import *
from bs4 import BeautifulSoup
from ogame.ogame import OGame
from ogame.message import Message
import re


ogame = OGame(  's120-us.ogame.gameforge.com',
                'thaunatos',
                'ogadrepr7cHubra' )

for message in ogame.messages():
    print(message)