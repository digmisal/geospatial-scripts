import geopandas as gpd
import pandas
import matplotlib.pyplot as ply
districts=gpd.read_file("D:\sig data\india shp\India_District_Shapefile\India_District_Shapefile\India_Districts.shp")
fire=gpd.read_file("E:\downloads1\MODIS_C6_1_South_Asia_24h\MODIS_C6_1_South_Asia_24h.shp")
print(districts.crs)
districts=districts.to_crs("epsg:32633",inplace=False)
fire=fire.to_crs("epsg:32633",inplace=False)
print(districts.crs)
print(fire.crs)

#print(districts.head())
#print(fire.head())

dist_with_geometry=gpd.sjoin(districts,fire,how="right")
dist_with_geometry.plot()
print(dist_with_geometry)
ply.show()





