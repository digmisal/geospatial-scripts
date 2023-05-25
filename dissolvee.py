import geopandas as gpd
import matplotlib.pyplot as plt
india=gpd.read_file(r"D:\sig data\india shp\India_District_Shapefile\India_District_Shapefile\India_Districts.shp")
india.plot()
print(india.head())
state=india.dissolve(by="State_Name")
state.plot(cmap="tab20")
                     
plt.show()
