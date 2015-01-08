import constants
import re

class Espionage(object):
    def __init__(self, body):
        self.body = body
        
        self.set_resources()
        
    def set_resources(self):
        resource_re = ':\s* '