import geopandas as gpd
import pandas
import matplotlib.pyplot as ply
fire=gpd.read_file("E:\downloads1\MODIS_C6_1_South_Asia_24h\MODIS_C6_1_South_Asia_24h.shp")
india=gpd.read_file("D:\sig data\india shp\INDIA_states.shp")
print(fire.crs)
india=india.to_crs("epsg:4326",inplace=False)
print(india.crs)

#fire.plot(cmap="Reds")
#india.plot()
joined=india.append(fire)
print(joined)
joined.plot()
ply.show()
