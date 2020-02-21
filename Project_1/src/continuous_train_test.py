"""
Training Script to train and test the continous CMAC
"""

import numpy as np
import matplotlib.pyplot as plt
import time
 

#***************** Functions ***************#

def test(AU1, W1):
	pred_output = []
	for x in range(0, len(AU1)):
		sums = 0
		for y in AU1[x]:
			sums = sums + W1[y[0]]
		pred_output.append(sums)
	return pred_output
 
# Function to find the association window mid index pointer
def window_pointer(gf, nw, nx, i):
	i = int(i)
	index = gf//2 + ((nw-2*(gf//2))*i)//nx
	return index

# Function to choose association window weights
def window_weights(gf, i):
	ww = []
	for k in range(i-(gf//2), i+(gf//2)+1):
		ww.append([k,1])
	#print('The window weights are:', weights)
	return ww
#*******************************************#

def cont_train(learning_rate, gen, train_data, test_data, samples):
	num_samples = len(samples)
	#Weights for each Association Unit
	AU_weights = []
	AU_weights1 = []
	# No of Weights
	num_weights = 35

	old_error = 0
	new_error = 5
	itr = 0
	t = 0
	error_diff = new_error - old_error
	weights = np.ones((num_weights,1))

	print('Training with generalization factor of:', gen, 'and learning rate:', learning_rate)
	# Starting time for training ...
	print('Training started ...')
	start_time = time.time()
	
	for i in train_data[0]:
		#print('Length of train data inputs:', t)
		#print('')
		#print('Lenght of AU weights:', len(AU_weights))
		index_pointer = window_pointer(gen, num_weights, num_samples, i)
		wgts = window_weights(gen, index_pointer)
		AU_weights.append(wgts)
		#print ('AU_weights train is:', AU_weights)
	
	#Update the weights till the no of iterations has completed or error drops below threshold
	while error_diff > 0.000001 and itr < 1000:
		#print('Training iteration no.:', itr)
		#print('')
		#print('Error difference:', error_diff)
		#print('')
		mse = 0
		old_error = new_error
		#print('AU_weghts is:', AU_weights)
		for i in range(0, len(AU_weights)):
			weight_sum = 0
			#print('AU wiegths train i:', AU_weights[i])
			# Summing up all the weights for the overlap window to get predicted o/p
			for j in AU_weights[i]:
				#print('weights are: ', weights)
				weight_sum = weight_sum + weights[j[0]]
				#print('train au:', weights[j[0]])
			# Error calculated
			err = weight_sum - train_data[1][i]
			# Correction Factor calculated
			CF = err/gen
			# Updating the weights by subtracting the product of the Learning rate & Correction factor
			for j in AU_weights[i]:
				weights[j[0]] = weights[j[0]] - learning_rate*CF
			# New error will be the mean square error
			mse = mse + err**2
			new_error = mse
			error_diff = abs(new_error - old_error)
			itr = itr+1
	print('Training ended!')
	
	
	print('Training ended! Time it took to train: ', time.time() - start_time)
	print('')

	#-------------Test----------#

	for i1 in test_data[0]:
		#print('Length of train data inputs:', t)
		#print('')
		#print('Lenght of AU weights:', len(AU_weights))
		index_pointer1 = window_pointer(gen, num_weights, num_samples, i1)
		wgts1 = window_weights(gen, index_pointer1)
		AU_weights1.append(wgts1)
	

	op = test(AU_weights1, weights)
	if gen == 5:
		plt.plot(test_data[0], op)
		print('Predicted Output for Overlap =', gen)
		plt.title('Predicted Function')
		plt.ylabel('Predicted Output')
		plt.xlabel('Testing Input')
		plt.show()
		plt.plot(test_data[0], test_data[1])
		print('Actual Output for Overlap =', gen)
		plt.title('Actual Function')
		plt.ylabel('Actual Output')
		plt.xlabel('Testing Input')
		plt.show()
	if gen == 10:
		plt.plot(test_data[0], op)
		print('Predicted Output for Overlap =', gen)
		plt.title('Predicted Function')
		plt.ylabel('Predicted Output')
		plt.xlabel('Testing Input')
		plt.show()
		plt.plot(test_data[0], test_data[1])
		print('Actual Output for Overlap =', gen)
		plt.title('Actual Function')
		plt.ylabel('Actual Output')
		plt.xlabel('Testing Input')
		plt.show()
	
	return mse
	


