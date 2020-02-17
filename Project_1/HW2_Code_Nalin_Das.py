import numpy as np
import matplotlib.pyplot as plt
import time

from neupy import algorithms, utils

print ('Header files loaded!')

utils.reproducible()
plt.style.use('ggplot')

x = np.linspace(0, 10, num = 100)
i = np.random.permutation(100)

train_input = np.reshape(np.linspace(0, 2 * np.pi, 70), (70, 1))
print ('The training Data is: ', train_input)
print (' ')

test_input = np.reshape(np.sort(2 * np.pi * np.random.random(30)), (30, 1))
print ('The testing Data is: ', test_input)
print (' ')

train_output = np.cos(train_input)
print ('The target 1-D function is tan(x): ', train_output)
print (' ')
test_output = np.cos(test_input)

#cmac.train(train_input, train_output, epochs=100)
#approx_output = cmac.predict(test_input)
window = []
accuracy = []
converge = []
# ****************  Discrete CMAC  *********************************

for i in range(2, 35):
	discrete_cmac = algorithms.CMAC(
	    quantization=100,               
	    associative_unit_size=i,
	    step=0.4,
	    verbose=True,
	    show_epoch=50,
	)
	
	overlap = 35/i
	window.append(overlap)
	start_time = time.clock()
	discrete_cmac.train(train_input, train_output, epochs=100)
	time_taken = time.clock() - start_time
	converge.append(time_taken)	
	approx_output = discrete_cmac.predict(test_input)
	acc = discrete_cmac.score(test_output, approx_output)
	accuracy.append(acc)	
	print ('Accuracy is:', accuracy)
	print ('Overlap is:', overlap)
	if overlap == 1.0 or overlap == 7.0 or overlap == 5.0:
		plt.figure(1)		
		plt.plot(train_input, train_output, label='Training')
		plt.plot(test_input, approx_output, label='Testing')
		plt.title('Overlap = %d' %overlap)
		plt.ylabel('Output')
		plt.xlabel('Input')
		plt.show()

plt.figure(2)
plt.plot(window, accuracy)
plt.title('Accuracy vs Window size')
plt.ylabel('Accuracy')
plt.xlabel('Window Size')
plt.show()

plt.figure(3)
plt.plot(window, converge)
plt.title('Time of convergence vs Window size')
plt.ylabel('Time of Convergence')
plt.xlabel('Window Size')
plt.show()

plt.figure(3)
plt.plot(train_input, train_output, label='Training')
plt.plot(test_input, approx_output, label='Testing')
plt.title('Overlap = %d' %overlap)
plt.ylabel('Output')
plt.xlabel('Input')
plt.show()
#*******************************************************************

# ****************  Continuous CMAC  *********************************
print ('Starting with Continuous CMAC!! ...... ')
for i in range(2, 35):
	continuous_cmac = algorithms.CMAC(
	    quantization=100,               
	    associative_unit_size=i,
	    step=0.6,
	    verbose=True,
	    show_epoch=50,
	)
	
	overlap = 35/i
	window.append(overlap)
	start_time = time.clock()
	continuous_cmac.train(train_input, train_output, epochs=70)
	time_taken = time.clock() - start_time
	converge.append(time_taken)	
	approx_output = continuous_cmac.predict(test_input)
	acc = continuous_cmac.score(test_output, approx_output)
	accuracy.append(acc)	
	print ('Accuracy is:', accuracy)
	print ('Overlap is:', overlap)
	if overlap == 1.0 or overlap == 7.0 or overlap == 5.0:
		plt.figure(1)		
		plt.plot(train_input, train_output, label='Training')
		plt.plot(test_input, approx_output, label='Testing')
		plt.title('Overlap = %d' %overlap)
		plt.ylabel('Output')
		plt.xlabel('Input')
		plt.show()

plt.figure(4)
plt.plot(window, accuracy)
plt.title('Accuracy vs Window size')
plt.ylabel('Accuracy')
plt.xlabel('Window Size')
plt.show()

plt.figure(5)
plt.plot(window, converge)
plt.title('Time of convergence vs Window size')
plt.ylabel('Time of Convergence')
plt.xlabel('Window Size')
plt.show()

plt.figure(6)
plt.plot(train_input, train_output, label='Training')
plt.plot(test_input, approx_output, label='Testing')
plt.title('Overlap = %d' %overlap)
plt.ylabel('Output')
plt.xlabel('Input')
plt.show()


#*******************************************************************



