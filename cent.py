
import geopandas as gpd
import matplotlib.pyplot as plt
gdf=gpd.read_file("D:\sig data\india shp\INDIA_states.shp")
#print(gdf)
gdf=gdf.set_index("ST_NAME")
gdf["area1"]=gdf.area
gdf["boundary1"]=gdf.boundary
gdf["centroid1"]=gdf.centroid
gdf=gdf.set_geometry("boundary1")
gdf.plot("area1")
plt.show()
