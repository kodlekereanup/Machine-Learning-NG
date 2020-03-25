import numpy as np
import matplotlib.pyplot as plt

# x : Size in square feet
# y : Price in 1000s
#                 [ x  , y  ]

training_data = np.array(
                [ [2104, 460],
                  [1416, 232],
                  [1534, 315],
                  [ 852, 178],
                  [ 400,  20],
                  [1634, 345],
                  [3452, 500],
                  [2000, 450]
                ])

#extracted_tdx = np.array([])
#extracted_tdy = np.array([])
#for i in training_data:
#    extracted_tdx = np.append(extracted_tdx ,i[0])
#    extracted_tdy = np.append(extracted_tdy, i[1])
#
# another way -- simpler
tdx = [x[0] for x in training_data]
tdy = [x[1] for x in training_data]

# find the best fit line
m, c = np.polyfit(tdx, tdy, 1)

# TODO: Learn polynomial curve fitting
#print(np.polyfit(tdx, tdy, 2))

tdx2 = np.array(tdx)
plt.plot(tdx, tdy, 'bo')
plt.plot(tdx2, m * tdx2 + c)

# enables multiple plotting windows
#plt.figure()

# plot this data using matplotlib
plt.xlabel('Size')
plt.ylabel('Price')
#plt.scatter(extracted_tdx, extracted_tdy)
plt.show()

print('Prediction Function: {}x + {}'.format(m, c))

def predict(m, c):
    x = int(input('Enter Size of House'))
    print('Value of House is:{}'.format(m * x + c))

predict(m, c)
