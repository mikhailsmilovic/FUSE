IMD_WFDEI
--------

PB 21/11/19

Precipitation Data from:
India Meteorological Department (IMD)

http://www.imdpune.gov.in/Clim_Pred_LRF_New/Grided_Data_Download.html
http://www.imdpune.gov.in/Clim_Pred_LRF_New/Research%20paper.pdf
http://www.imdpune.gov.in/Clim_Pred_LRF_New/rainfall.php


Rainfall:
IMD New High Spatial Resolution (0.25X0.25 degree) Long Period (1901-2018) Daily Gridded Rainfall Data Set Over India. 
This data product is a very high spatial resolution daily gridded rainfall data (0.25 x 0.25 degree). 
The unit of rainfall is in millimeter (mm). Data available for 118 years, 1901 to 2018. Data is arranged in 135x129 grid points. 
The first data in the record is at 6.5N & 66.5E, the second is at 6.5N & 66.75E, and so on. The last data record corresponds to 38.5N & 100.0E.
The yearly data file consists of 365/366 records corresponding to non leap/ leap years.

CITATION (for Rainfall):
Should you refer to our product in your paper/presentation, please cite
Pai et al. (2014). Pai D.S., Latha Sridhar, Rajeevan M., Sreejith O.P., Satbhai N.S. and Mukhopadhyay B., 2014:
Development of a new high spatial resolution (0.25° X 0.25°)Long period (1901-2010) daily gridded rainfall data set over
India and its comparison with existing data sets over the region; MAUSAM, 65, 1(January 2014), pp1-18.



WFDEI
-----

Daily-resolution observed climate data on a global (land only) 0.5°x0.5° lat-lon grid, 
based on the reanalysis data set ERA-Interim and using the bias target GPCC. 
The data set covers the period 1901-2018, where the data for 1901-1978 are taken from WFD, and from 1979 onwards from WFDEI.GPCC


Data Type: Daily observed atmospheric climate
Variables: 
tasmax: Max Temperature [K]
tas: Avg. Temperature [K]
tasmin: Max Temperature [K]
rlds: Long wave radiation flux downward [W m-2]
rsds: Short wave radiation flux downward [W m-2]
wind: wind [m s-1]
rhs: Relative humidity [%]
ps: Surface pressure [Pa]


HERE: a dataset from 1/1/1961- 31/12/2018 with each parameter in a single netcdf file.


Weedon, G.P., S.S. Gomes, P.P. Viterbo, W.J. Shuttleworth, E.E. Blyth, H.H. Österle, J.C. Adam, N.N. Bellouin, O.O. Boucher, 
and M.M. Best, 2011:
Creation of the WATCH Forcing Data and Its Use to Assess Global and Regional Reference Crop Evaporation over Land during the
Twentieth Century. J. Hydrometeor., 12, 823–848, doi: 10.1175/2011JHM1369.1



Average with cdo
================
cdo timavg pr_IMD_bhima_025.nc pr_avg.nc

