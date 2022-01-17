"""
Ordinary Kriging Example
========================
First we will create a 2D dataset together with the associated x, y grids.
"""

import numpy as np
import pykrige.kriging_tools as kt
from pykrige.ok import OrdinaryKriging
import matplotlib.pyplot as plt

groundwaterObservationsLocation = 'C:\GitHub\FUSE\Data_forNotebooks\WaterTable\\'

import xlrd

wb = xlrd.open_workbook(groundwaterObservationsLocation+'UB_GW_Data.xls')
sheet = wb.sheet_by_index(0)
sheet.cell_value(0, 0)

X=[]
Y=[]
Z=[]

for i in range(1, sheet.nrows):
    X.append(sheet.cell_value(i, 4))
    Y.append(sheet.cell_value(i, 3))
    Z.append(sheet.cell_value(i, 5) - sheet.cell_value(i, 8))


print(X)
print(max(X))

X = np.array(X)
Y = np.array(Y)
Z = np.array(Z)

gridx = np.arange(73.1708, 76.24583+0.0083, 0.0083333333333333333333)
gridy = np.arange(19.49583, 16.83750-0.0083, -0.0083333333333333333333)
print(min(gridy))

# gridx = np.arange(min(X), max(X), 0.01)
# gridy = np.arange(max(Y), min(Y), -0.01)
# gridy = np.arange(min(Y), max(Y), 0.00)

###############################################################################
# Create the ordinary kriging object. Required inputs are the X-coordinates of
# the data points, the Y-coordinates of the data points, and the Z-values of the
# data points. If no variogram model is specified, defaults to a linear variogram
# model. If no variogram model parameters are specified, then the code automatically
# calculates the parameters by fitting the variogram model to the binned
# experimental semivariogram. The verbose kwarg controls code talk-back, and
# the enable_plotting kwarg controls the display of the semivariogram.

OK = OrdinaryKriging(
    X, #data[:, 0],
    Y, #data[:, 1],
    Z, #data[:, 2],
    variogram_model="linear",
    verbose=False,
    enable_plotting=False,
    #coordinates_type="geographic",
)

###############################################################################
# Creates the kriged grid and the variance grid. Allows for kriging on a rectangular
# grid of points, on a masked rectangular grid of points, or with arbitrary points.
# (See OrdinaryKriging.__doc__ for more information.)

z, ss = OK.execute("grid", gridx, gridy)

###############################################################################
# Writes the kriged grid to an ASCII grid file and plot it.

print(len(z[0])) #xaxis 370
print(len(z)) #yaxis 320
kt.write_asc_grid(gridx, gridy, z, filename="output.asc")
plt.imshow(z)
plt.show()