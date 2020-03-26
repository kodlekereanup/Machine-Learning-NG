import matplotlib.pyplot as plt

def mc(tdx, tdy):

    mean_x = sum(tdx) / len(tdx)
    mean_y = sum(tdy) / len(tdy)

    ss_x = sum([(i - mean_x)**2 for i in tdx])
    sp   = sum([(i - mean_x)*(j - mean_y) for i, j in zip(tdx, tdy)])

    m = sp/ ss_x
    c = mean_y - m * mean_x

    return (m, c)

# x : Size in square feet
# y : Price in 1000s

tdx = []
tdy = []
words = []

# obviously it would be a better choice to import csv here but I just wanted
# to do it this way
with open('dataset.csv', 'r') as training_data:
    lines = [line.rstrip() for line in training_data]

for line in lines:
    words.append(line.split(','))
    #lint = map(int, words)

for i in range(1, len(words)):
    tdx.append(int(words[i][0]))
    tdy.append(int(words[i][1]))

# another way -- simpler
# training_data = [[1,2],[3,4]]
# tdx = [x[0] for x in training_data]
# tdy = [x[1] for x in training_data]

# find the best fit line
#m, c = np.polyfit(tdx, tdy, 1)

m, c = mc(tdx, tdy)

# TODO: Learn polynomial curve fitting
#print(np.polyfit(tdx, tdy, 2))

#tdx2 = np.array(tdx)
tdx2 = []
for i in tdx:
    tdx2.append(m * i + c)

plt.plot(tdx, tdy, 'bo')
plt.plot(tdx2, tdx2)

# enables multiple plotting windows
#plt.figure()

# plot this data using matplotlib
plt.xlabel('Size')
plt.ylabel('Price')
#plt.scatter(extracted_tdx, extracted_tdy)
plt.show()

print('Prediction Function: {}x + {}'.format(m, c))

def predict(m, c):
    x = int(input('Enter Size of House: '))
    print('Value of House is:{}'.format(m * x + c))

predict(m, c)
