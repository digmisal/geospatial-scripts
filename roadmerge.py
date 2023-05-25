import geopandas as gpd
import pandas
import matplotlib.pyplot as ply
districts=gpd.read_file("D:\sig data\india shp\India_District_Shapefile\India_District_Shapefile\India_Districts.shp")
road=gpd.read_file("E:\downloads1\IND_rds\IND_roads.shp")
print(districts.crs)
print(road.crs)
road_with_geometry=gpd.sjoin(road,districts,how="inner")
road_with_geometry.plot()
print(road_with_geometry.head())
ply.show()
