import numpy as np
import matplotlib.pyplot as plt

def cmac_map(samp_pts, nw, na):
	


# Generating 100 sampling points
x = np. linspace(0, 2*np.pi, num = 100)

# Defining the 1-D Target Function to be trained on
y = np.sin(x)

plt.plot(x,y)
plt.title('1-D function to be trained')
plt.ylabel('F(x)')
plt.xlabel('100 Sampling points')
plt.show()

# Generate random indexes from 1-100
i = np.random.permutation(100)

train_data = (x[i[0:69]], y[i[0:69]])

plt.plot(x[i[0:69]],y[i[0:69]])
plt.title('Training Data')
plt.ylabel('Training Outputs')
plt.xlabel('Training Inputs')
plt.show()

test_data = (x[i[70:99]], y[i[70:99]])

plt.plot(x[i[70:99]],y[i[70:99]])
plt.title('Test Data')
plt.ylabel('Test Outputs')
plt.xlabel('Test Inputs')
plt.show()



