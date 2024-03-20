# Mesoscale classifications
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10641821.svg)](https://doi.org/10.5281/zenodo.10641821)

## Description

This repository contains a collection of post-processed mesoscale cloud classifications.

## Installation of dependencies
The dependencies are listed in `environment.yml` and can be installed e.g. with conda or mamba:
```
mamba env create -f environment.yml
```
or directly into an existing python environment with
```
mamba install python intake-xarray xarray s3fs "intake<3.0.0"
```
mamba can be downloaded at https://github.com/conda-forge/miniforge/releases/

## Usage

To access the mesoscale cloud morphology datasets, the following lines are sufficient (after installing any dependencies):

```python
import intake
cat = intake.open_catalog("https://raw.githubusercontent.com/ISSI-CONSTRAIN/meso-morphs/main/catalog/catalog.yaml")
ds = cat.SGFF.to_dask()
```

## Non-python usage
In case the dataset will be handled in a software environment different to python, it might be easiest to store a local copy of the dataset by running the above mentioned python instructions and save the datasets as netCDF files with:

```python
ds.to_netCDF("SGFF_classifications.nc")
```

## Reproducability / Updating of datasets

1. To reproduce the workflow, access to the UW olympus cluster is needed
2. Please set your olympus username as environment variable `export SSH_USERNAME=myname`
3. `dvc repro` downloads the original files and updates the output files
4. To push files to remote, please `export AWS_ACCESS_KEY_ID=${API Key}` and `export AWS_SECRET_ACCESS_KEY='mysecret'`
5. Only files in the output directory should be pushed with `dvc push --remote aws data/output/Daily*`
