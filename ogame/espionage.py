import constants
import re

class Espionage(object):
    def __init__(self, body):
        # stripping out periods makes parsing the numbers easier
        self.body = body.replace('.', '')
        
        self.set_resources()
        self.set_defense()
        
        
    def get_count(self, name):
        regex = re.compile(name + '\s*(\d+)', re.IGNORECASE)
        m = regex.search(self.body)
        return int(m.group(1))
    
    def set_resources(self):
        self.resources = {}
        
        for material in ['metal', 'crystal', 'deuterium']:
            self.resources[material] = self.get_count(material + ':')
       
    def set_buildings(self):
        pass
    
    def set_defense(self):
        pass
    
    def set_fleet(self):
        pass
    
    def set_meta(self):
        pass
