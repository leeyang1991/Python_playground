import matplotlib.pyplot as plt
from lytools import *
import pprint
import os
T = Tools()

def plot_NDVI_time_series():
    fdir = 'data/NDVI/'
    date_list = []
    mean_list = []
    for f in os.listdir(fdir):
        if not f.endswith('.tif'):
            continue
        date = f.split('.')[0]
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        date_obj = datetime.datetime(year, month, day)
        if year <= 2015:
            continue
        fpath = join(fdir, f)
        arr = ToRaster().raster2array(fpath)[0]
        arr = np.array(arr,dtype=float) / 10000.
        arr[arr>1] = np.nan
        arr[arr<0] = np.nan
        arr_mean = np.nanmean(arr)

        date_list.append(date_obj)
        mean_list.append(arr_mean)

        # plt.imshow(arr,'PRGn',vmin=0,vmax=8000,interpolation='nearest')
        # plt.imshow(arr,'YlGn',vmin=0,vmax=.8,interpolation='nearest')
        # plt.colorbar()
        # plt.title(f.replace('.tif',''))
        # plt.show()
    date_list = np.array(date_list)
    plt.plot(date_list,mean_list)
    plt.show()

    pass


def plot_NDVI_average_spatial_map():
    fdir = 'data/NDVI/'
    date_list = []
    arr_list = []
    for f in os.listdir(fdir):
        if not f.endswith('.tif'):
            continue
        date = f.split('.')[0]
        year = int(date[:4])
        month = int(date[4:6])
        day = int(date[6:])
        date_obj = datetime.datetime(year, month, day)
        if year <= 2015:
            continue
        fpath = join(fdir, f)
        arr = ToRaster().raster2array(fpath)[0]
        arr = np.array(arr,dtype=float) / 10000.

        # arr[arr>1] = np.nan
        # arr[arr<0] = np.nan
        arr_list.append(arr)
    # pprint.pprint(arr_list);exit()

    arr_list = np.array(arr_list)
    arr_mean = np.nanmean(arr_list,axis=0)
    plt.imshow(arr_mean,'YlGn',vmin=0,vmax=.8,interpolation='nearest')
    plt.colorbar()
    plt.title('NDVI average spatial map')
    plt.show()

    pass


# T.color_map_choice()
# plot_NDVI_time_series()
plot_NDVI_average_spatial_map()