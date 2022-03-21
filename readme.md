pointProj adds projected coordinates as to columns at the end of a CSV document.



Call pointProj from the terminal, or import from another scrpt like this:

from pointProj import projectCSV

origCSV = r"Path\to\original.csv"

projCSV = r""Path\to\projected.csv""

origCoord = EPSG of 'from' CRS e.g., 4326

projCoord = EPSG of 'to' CRS e.g., 3857

def projectCSV(origCSV, projCSV, origCoord, projCoord)

***The original CSV must include coordinate fields ("x", "y").

******See requirements.txt for dependencies.