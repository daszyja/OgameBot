from errors import BAD_UNIVERSE_NAME, BAD_DEFENSE_ID, NOT_LOGGED
import constants
from bs4 import BeautifulSoup
from ogame import OGame
import re

ogame = OGame(  's120-us.ogame.gameforge.com',
                'thaunatos',
                'ogadrepr7cHubra' )
                

print ogame.num_missions()
