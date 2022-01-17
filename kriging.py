import pyKriging
from pyKriging.krige import kriging
from pyKriging.samplingplan import samplingplan
import numpy as np

# The Kriging model starts by defining a sampling plan, we use an optimal Latin Hypercube here
#sp = samplingplan(2)
#X = sp.optimallhc(20)

# Next, we define the problem we would like to solve

#y = testfun(X)
#print(X)

#reading in text files
groundwaterObservationsLocation = 'C:\GitHub\FUSE\Data_forNotebooks\WaterTable\\'

import xlrd

wb = xlrd.open_workbook(groundwaterObservationsLocation+'UB_GW_Data.xls')
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

X=[]
y=[]

for i in range(1, 40): #sheet.nrows):
    X.append([sheet.cell_value(i, 4), sheet.cell_value(i, 3)])
    y.append(sheet.cell_value(i, 5) - sheet.cell_value(i, 8))

X = np.array(X)
y = np.array(y)

testfun = pyKriging.testfunctions().linear

print(X)
print(y)

# Now that we have our initial data, we can create an instance of a Kriging model
k = kriging(X, y, testfunction=testfun, name='simple')
k.train()

# Now, five infill points are added. Note that the model is re-trained after each point is added
numiter = 10
for i in range(numiter):
    print ('Infill iteration {0} of {1}....'.format(i + 1, numiter))
    newpoints = k.infill(1)
    for point in newpoints:
        k.addPoint(point, testfun(point)[0])
    k.train()

# And plot the results
k.plot()