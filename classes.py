import constants
import re
from datetime import datetime

class Message():
    def __init__( self, soup):
        self.soup = soup
        self.find_id()
        self.find_sender()
        self.find_recipient()
        self.find_subject()
        self.find_body()
        self.find_time()
        self.set_type()
        
    def find_sender( self ):
        tag = self.soup.find('span', {'class':'playerName'} )
        self.sender = tag.text.strip()
    
    def find_subject( self ):
        child = self.soup.find('th', text= re.compile('Subject'))
        tag = child.parent.find('td')
        self.subject = tag.text.strip()
        
    def find_recipient(self):
        child = self.soup.find('th', text=re.compile('To'))
        tag = child.parent.find('td')
        self.recipient= tag.text.strip()
    
    def find_body(self):
        tag = self.soup.find('div', {'class':'note'})
        self.body = tag.text.strip()
    
    def find_time(self):
        child = self.soup.find('th', text=re.compile('Date'))
        tag = child.parent.find('td')
        self.raw_time = tag.text.strip()
        
        time_converter = '%d.%m.%Y %H:%M:%S'
        self.time = datetime.strptime( self.raw_time, time_converter )
    
    def find_id(self):
        tag = self.soup.find('div', {'class':'showmessage'})
        self.message_id = tag['data-message-id']
        
    def set_type(self):
        if (self.subject.startswith('Espionage report of ') and
                self.sender == 'Fleet Command'):
            self.message_type = 'espionage'
                
                
        
        
        