from __future__ import absolute_import
from ogame.constants import *
from bs4 import BeautifulSoup
from ogame.ogame import OGame
from ogame.message import Message
from ogame.espionage import Espionage
from ogame.fleet import Fleet


ogame = OGame( 	's120-us.ogame.gameforge.com', 
				'Thaunatos', 
				'ogadrepr7cHubra' )
				
coords = {
        'galaxy': 1,
        'system': 149,
        'position': 4
    }

fleet = Fleet(espionage=ogame.fetch_espionage(coords))

print(fleet.mission)
print(fleet.where)