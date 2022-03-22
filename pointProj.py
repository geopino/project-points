from pyproj import CRS
from pyproj import Transformer
import pandas as pd

def projectCSV( origCSV, projCSV, origCoord, projCoord):

    ###Define 'from' CRS
    crs_from = CRS.from_epsg(origCoord)
    
    ###Define a 'to' CRS
    crs_to = CRS.from_epsg(projCoord)

    ###Define a transformer
    transformer = Transformer.from_crs(crs_from, crs_to)

    ###Use pandas to read Northing and Easting from CSV and derive Latitiude Longitude
    df = pd.read_csv(origCSV, header=0)
    a = df['x'].values
    b = df['y'].values
    df["projY"] = transformer.transform(a, b)[0]
    df["projX"] = transformer.transform(a, b)[1]

    ###Write dataframe to CSV
    df.to_csv(projCSV)

if __name__ == "__main__":
    projectCSV()