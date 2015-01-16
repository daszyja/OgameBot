import constants

class Fleet(object):
    def __init__(self, planet=None, ships=None, speed=None, 
                    where=None, mission = None, resources=None,
                    espionage=None):
        
        # default parameters
        self.planet = planet
        self.ships = {}
        self.where = {}
        self.speed = constants.Speed['100%']
        if speed:
            self.speed = constants.Speed[speed]
        
        self.mission = ''
        if mission:
            self.mission = constants.Missions(mission)
        
        self.resources = {'metal': 0, 'crystal': 0, 'deuterium': 0}
        if resources:
            self.resources.update(resources)
            
        if espionage:
            self.spy(espionage)
        
        

    
    def spy( self, espionage ):
        self.mission = constants.Missions['Attack']
        self.ships['SmallCargo'] = espionage.cargos_needed()
        self.where = espionage.coords