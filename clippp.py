import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon as ply
india=gpd.read_file(r"E:\downloads1\IND_rds\IND_roads.shp")
#northmh=gpd.read_file(r"E:\aster\northmaharastra.shp")
polygonn=ply([(68,25),(75,25),(75,20),(70,20),(68,25)])
clipped=gpd.clip(india,polygonn)
clipped.plot()
#india.plot()
#clipped2=gpd.clip(india,northmh)
#clipped2.plot()
print(clipped)
plt.show()

