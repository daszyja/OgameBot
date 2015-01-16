import constants
import re

class Espionage(object):
    def __init__(self, body):
        # stripping out periods makes parsing the numbers easier
        self.body = body.replace('.', '')
        
        self.set_resources()
        self.set_defense()
        self.set_meta()
        
        
    def get_count(self, name):
        regex = re.compile(name + '\s*(\d+)', re.IGNORECASE)
        m = regex.search(self.body)
        return int(m.group(1))
    
    def set_resources(self):
        self.resources = {}
        self.total_resources = 0
        
        for material in ['metal', 'crystal', 'deuterium']:
            self.resources[material] = self.get_count(material + ':')
            self.total_resources += self.resources[material]
       
    def set_buildings(self):
        pass
    
    def set_defense(self):
        pass
    
    def set_fleet(self):
        pass
    
    def set_meta(self):
        # target name, location, time?
        name_regex = re.compile( r'Player: (.*)\)', re.IGNORECASE)
        self.target_name = name_regex.search(self.body).group(1)
        
        coords_regex = re.compile( r'\[(\d+):(\d+):(\d+)\]', re.IGNORECASE)
        match = coords_regex.search(self.body)
        self.coords = {}
        self.coords['galaxy'] = int(match.group(1))
        self.coords['system'] = int(match.group(2))
        self.coords['position'] = int(match.group(3))

    def cargos_needed(self, large=False, percentage=0.5):
        res_possible = self.total_resources * percentage
        if large:
            return int(round(res_possible/25000)) + 1
        else:
            return int(round(res_possible/5000)) + 1