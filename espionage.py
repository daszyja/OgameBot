from ogame import OGame
from constants import *
import time
from collections import deque


def espionage( target_txt, wait_time, verbose =True ):
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
	vprint( 'read target file\n' )

	j = 0
	done = False
	ogame = OGame( 	's120-us.ogame.gameforge.com', 
					'Thaunatos', 
					'ogadrepr7cHubra' )

	potential_slots = ogame.get_research('Computer Technology') + 1	
	
	num_probes = ogame.get_preferred_probes()
	home = ogame.get_planet_by_name(home)
	while targets:
		current_fleets = ogame.num_missions()
		num_fleets = potential_slots - current_fleets
		
		j += 1
		vprint( 'Beginning Round %d' %(j))
		for i in range(num_fleets):
			if not ogame.is_logged():
				ogame.login()
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

		vprint( 'Round %d complete\n' %(j))
		if done:
			break

		time.sleep(wait_time)
	ogame.logout()
	vprint('Waiting for last wave...')
	time.sleep(wait_time/2)

	print("Spying complete")

if __name__ == '__main__':
	# txt, probes, fleet, wait, verbose
	espionage( 'esp_targets/alpha1.txt', 90 )

