import numpy as np
import matplotlib.pyplot as plt
import time
from discrete_train_test import des_train, window_pointer, window_weights, test
from continuous_train_test import cont_train, window_pointer, window_weights, test

# Generating 100 sampling points
samples = np.linspace(0, 2*np.pi, num = 100)
num_samples = len(samples)
# No of Weights
num_weights = 35

learning_rate = 0.1

# Defining the 1-D Target Function to be trained on
func = np.cos(samples)

plt.plot(samples,func)
plt.title('1-D function to be trained')
plt.ylabel('F(x)')
plt.xlabel('100 Sampling points')
plt.show()

# Generate random indexes from 1-100
i = np.random.permutation(100)

train_data = (samples[i[0:70]], func[i[0:70]])

plt.plot(samples[i[0:70]],func[i[0:70]])
plt.title('Training Data')
plt.ylabel('Training Outputs')
plt.xlabel('Training Inputs')
plt.show()

test_data = (samples[i[71:100]], func[i[71:100]])

plt.plot(samples[i[71:100]],func[i[71:100]])
plt.title('Test Data')
plt.ylabel('Test Outputs')
plt.xlabel('Test Inputs')
plt.show()

#-------------Discrete----------------#

# Training for generalization factor gen from 1-->34

for gen in range(1,35):
	print('For discrete overlap = ', gen)
	des_train(learning_rate, gen, train_data, test_data, samples)

for gen in range(1,35):
	print('For continuous overlap = ', gen)
	cont_train(learning_rate, gen, train_data, test_data, samples)



	

	
			
			
			
	
	

	
	


