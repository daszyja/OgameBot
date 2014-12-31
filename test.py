from errors import BAD_UNIVERSE_NAME, BAD_DEFENSE_ID, NOT_LOGGED
import constants
from bs4 import BeautifulSoup
from ogame import OGame
import re

ogame = OGame(  's120-us.ogame.gameforge.com',
                'thaunatos',
                'ogadrepr7cHubra' )
                

payload = {
        'displayCategory': '10',
        'displayPage': 1,
        'siteType': '101',
        'ajax': '1'
}

res = ogame.session.post( ogame.get_url( 'messages' ), data=payload).content
soup = BeautifulSoup(res)


with open( 'data.html', 'w' ) as f:
    for line in res:
        f.write( line )


parent = soup.find( 'tr', {'id': 'TR3228375'})
url = parent.find( 'a', {'class': 'overlay'})['href']

print(url)

res = ogame.session.get(url).content




