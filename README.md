# Mesoscale classifications

## Description

This repository contains a collection of post-processed mesoscale cloud classifications.

## Usage

To access the mesoscale cloud morphology datasets, the following lines are sufficient (after installing any dependencies):

```
import intake
cat = intake.open_catalog("https://raw.githubusercontent.com/ISSI-CONSTRAIN/meso-morphs/main/catalog/catalog.yaml")
ds = cat.SGFF.to_dask()
```

## Reproducability / Updating of datasets

1. To reproduce the workflow, access to the UW olympus cluster is needed
2. Please set your olympus username as environment variable `export SSH_USERNAME=myname`
3. `dvc repro` downloads the original files and updates the output files
4. To push files to remote, please `export AWS_ACCESS_KEY_ID=${API Key}` and `export AWS_SECRET_ACCESS_KEY='mysecret'`
5. Only files in the output directory should be pushed with `dvc push --remote aws data/output/Daily*`
