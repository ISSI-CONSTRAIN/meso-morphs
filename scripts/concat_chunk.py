import xarray as xr
import datetime as dt
import argparse

fnames = 'data/input/SGFF/yearly/Daily*.nc'

def preprocess(ds):
    fn = ds.encoding['source']
    year = fn.split('_')[-1][:4]
    ds['time'] = xr.DataArray([dt.datetime(int(year), 1, 1)+ dt.timedelta(days=int(d)) for d in ds.days.values], dims='time')
    del ds['days']
    return ds
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Combining yearly mesoscale classification files.")

    parser.add_argument('-i', '--fnames', type=str, required=True, help='The file names to process')
    parser.add_argument('-o', '--output_filename', type=str, required=True, help='The zarr output file name')

    args = parser.parse_args()

    ds = xr.open_mfdataset(args.fnames, preprocess=preprocess, combine='by_coords')
    ds.chunk({"time":10,"class":1,"latitude":150,"longitude":360}).to_zarr(args.output_filename)