import geopandas as gpd
import matplotlib.pyplot as plt
fire=gpd.read_file(r"E:\downloads1\MODIS_C6_1_South_Asia_24h\MODIS_C6_1_South_Asia_24h.shp")
#fire.plot()
print(fire)
dissolved=fire.dissolve(by="DAYNIGHT",aggfunc={'BRIGHTNESS':'mean','BRIGHT_T31':'mean'})
dissolved.plot(cmap="copper")
print(dissolved)
dissolved.to_file(r"E:\downloads1\MODIS_C6_1_South_Asia_24h\dissolved.shp",driver="ESRI Shapefile")
dissolved.to_file(r"E:\downloads1\MODIS_C6_1_South_Asia_24h\dissolved.geojson",driver="GeoJSON")
plt.show()
