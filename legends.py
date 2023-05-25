import geopandas as gpd
import matplotlib.pyplot as plt
india=gpd.read_file(r"D:\sig data\india shp\INDIA_states.shp")
print(india)
india.plot(column="ST_NAME",legend=True,cmap="viridis",legend_kwds={loc:'upper right', bbox_to_anchor:(0.5, 0.5)})
plt.show()
