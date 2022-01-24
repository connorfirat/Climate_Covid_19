# ============================================================= METHOD For Data Mining Environmental Variables ==================================================================
# URL download cdsapi package instructions: https://confluence.ecmwf.int/display/CKB/How+to+install+and+use+CDS+API+on+Windows
# URL for API token instructions: https://cds.climate.copernicus.eu/api-how-to
# URL forum troubleshooting .cdsapirc file: https://earthscience.stackexchange.com/questions/16962/error-trying-to-download-era5-data-exception-missing-incomplete-configuration
# ===============================================================================================================================================================================

import cdsapi
cds = cdsapi.Client()
cds.retrieve('reanalysis-era5-pressure-levels', {
           "variable": "temperature",
           "pressure_level": "1000",
           "product_type": "reanalysis",
           "date": "2017-12-01/2017-12-31",
           "time": "12:00",
           "format": "grib"
       }, 'download.grib')