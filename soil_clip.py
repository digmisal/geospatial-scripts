import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Polygon
india=gpd.read_file("D:\sig data\india shp\India_District_Shapefile\India_District_Shapefile\India_Districts.shp")
fire=gpd.read_file("D:\sig data\DSMW\DSMW.shp")
print(fire.crs)
india=india.to_crs("epsg:4326",inplace=False)
print(india.crs)
print(india)
mh=india[india["State_Name"]=="MAHARASHTRA"]

fire_clip=gpd.clip(fire,mh)
fig,ax=plt.subplots()
fire_clip.plot(ax=ax,cmap="Reds")
mh.boundary.plot(ax=ax)
fire_clip.to_file("D:\sig data\DSMW\soil1.shp",driver="ESRI Shapefile")
plt.show()
