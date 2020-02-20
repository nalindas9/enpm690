import numpy as np
import matplotlib.pyplot as plt
import time
from train import train 


#***************** Functions ***************#

# Function to find the association window mid index pointer
def window_pointer(gf, nw, nx, i):
	i = int(i)
	index = gf//2 + ((nw-2*(gf//2))*i)//nx
	return index

# Function to choose association window weights
def window_weights(gf, i):
	weights = []
	for k in range(i-(gf//2), i+(gf//2)+1):
		weights.append([k,1])
	print('The window weights are:', weights)
	return weights
#*******************************************#

# Generating 100 sampling points
samples = np.linspace(0, 2*np.pi, num = 100)
num_samples = len(samples)
# Association Units Info
AU = {}
# No of Weights
num_weights = 35

#Weights for each Association Unit
AU_weights = []
# Defining the 1-D Target Function to be trained on
func = np.cos(samples)

plt.plot(samples,func)
plt.title('1-D function to be trained')
plt.ylabel('F(x)')
plt.xlabel('100 Sampling points')
plt.show()

# Generate random indexes from 1-100
i = np.random.permutation(100)

train_data = (samples[i[0:69]], func[i[0:69]])

plt.plot(samples[i[0:69]],func[i[0:69]])
plt.title('Training Data')
plt.ylabel('Training Outputs')
plt.xlabel('Training Inputs')
plt.show()

test_data = (samples[i[70:99]], func[i[70:99]])

plt.plot(samples[i[70:99]],func[i[70:99]])
plt.title('Test Data')
plt.ylabel('Test Outputs')
plt.xlabel('Test Inputs')
plt.show()

#-------------Discrete----------------#

# Training for generalization factor gen from 1-->34

for gen in range(1,35):
	
	weights = np.ones((num_weights,1))
	for i in train_data[0]:
		index_pointer = window_pointer(gen, num_weights, num_samples, i)
		AU_weights.append(window_weights(gen, index_pointer))
	
	print('The AU weights are:', AU_weights)
	train(0.1, gen)
	
	#Update the weights till the no of iterations has completed or error drops below threshold
	while 
	
	

	
	


