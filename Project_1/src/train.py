"""
Training Script to train the CMAC
"""

import time

def train(r, gf):
	print('Training with generalization factor of:', gf, 'and learning rate:', r)
	# Starting time for training ...
	print('Training started ...')
	start_time = time.time()

	
	
	print('Training ended! Time it took to train: ', time.time() - start_time)
	print('')
