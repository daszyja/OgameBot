from ogame.ogame import OGame
from ogame.constants import *
import time
from collections import deque


def spy( target_txt, wait_time, verbose =True ):
	if verbose:
		def vprint(text):
			print(text)
	else:
		vprint = lambda x: None


	with open( target_txt, 'r' ) as f:
		lines = f.readlines()

	targets = deque([])
	home = lines[0].strip()
	for line in lines[1:]:
		nums = line.split(':')
		targets.append ({ 
			'galaxy': int(nums[0]),
			'system': int(nums[1]),
			'position': int(nums[2])
		} )
	copy = list( targets )
	vprint( 'read target file\n' )

	j = 0
	done = False
	ogame = OGame( 	's120-us.ogame.gameforge.com', 
					'Thaunatos', 
					'ogadrepr7cHubra' )

	potential_slots = ogame.get_research('Computer Technology') + 1	
	
	num_probes = ogame.get_preferred_probes()
	home = ogame.get_planet_by_name(home
	while targets:
		ogame.login()
		current_fleets = ogame.num_missions()
		open_fleets = potential_slots - current_fleets
		
		total_probes = ogame.get_ships( home )['EspionageProbe']
		num_fleets = min( open_fleets, total_probes/num_probes )
		
		j += 1
		vprint( 'Beginning Round %d' %(j))
		for i in range(num_fleets):
			
			ships = [(Ships['EspionageProbe'], num_probes)]
			speed = Speed['100%']
			where = targets.popleft()
			mission = Missions['Spy']
			resources = {'metal': 0, 'crystal': 0, 'deuterium': 0}
			ogame.send_fleet( home, ships, speed, where, mission, resources)
			vprint('%d:%d:%d' % 
				(where['galaxy'], where['system'], where['position']))

			if not targets:
				done = True
				break
		ogame.logout()

		vprint( 'Round %d complete\n' %(j))
		if done:
			break

		time.sleep(wait_time)
	ogame.logout()
	vprint('Waiting for last wave...')
	time.sleep(wait_time/2)
	 
	print("Espionage complete")
	
	return copy

if __name__ == '__main__':
	spy( 'esp_targets/alpha.txt', 90 )
