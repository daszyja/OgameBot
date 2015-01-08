import constants
import re
from datetime import datetime
from bs4 import BeautifulSoup, SoupStrainer 

class Message(object):
    def __init__( self, tag ):
        self.soup = tag
        
        self.set_id()
        self.set_time()
        self.set_sender()
        self.set_subject()
        self.set_url()
        self.set_type()
        self.set_location()

    
    def set_id(self):
        id_reg = re.compile('TR(\d+)')
        match = id_reg.match(self.soup['id'])
        self.message_id = match.group(1)
    
    def set_time(self):
        tag = self.soup.find('td', {'class':re.compile('date')})
        raw_time = tag.text.strip()
        
        time_converter = '%d.%m.%Y %H:%M:%S'
        self.time = datetime.strptime( raw_time, time_converter )
            
    def set_sender(self):
        self.sender = self.soup.find('td', {'class':'from'}).text.strip()
        
    def set_subject(self):
        self.subject = self.soup.find('td', {'class':'subject'}).text.strip()
        
    def set_location(self):
        self.location = None
        location_reg = re.compile( '''
                \[(\d):     # galaxy
                (\d{1,3}):  # system
                (\d{1,2})]  # position
            ''', re.VERBOSE)
        match = location_reg.match(self.subject)
        if match:
            self.location = {
                'galaxy': match.group(1),
                'system': match.group(2),
                'position': match.group(3)
            }
        
        
    def set_url(self):
        self.url = self.soup.find('a', {'class':'overlay'})['href']

    def set_type(self):
        if self.sender == 'Fleet Command':
            if self.subject.startswith('Espionage report'):
                self.message_type = 'espionage'
            elif self.subject.startswith('Battle Report'):
                self.message_type = 'battle'
            elif self.subject.startswith('Return of a'):
                self.message_type = 'return'
        else:
            self.message_type = 'personal'
            
    def get_body(self, body_html):
        strainer = SoupStrainer('div', {'class':'note'})
        soup = BeautifulSoup(body_html, parse_only=strainer)
        self.body = soup.text.strip()
        
            
    def __str__(self):
        return str(self.time) + ' ' + self.subject