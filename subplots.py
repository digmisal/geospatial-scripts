import geopandas as gpd
import matplotlib.pyplot as plt
fire= gpd.read_file(r"E:\downloads1\MODIS_C6_1_South_Asia_24h\dissolved.shp")
india=gpd.read_file(r"D:\sig data\india shp\INDIA_states.shp")
roads=gpd.read_file(r"E:\downloads1\IND_rds\IND_roads.shp")
northmh=gpd.read_file(r"E:\aster\northmaharastra.shp")
#print(india.head())
#print(roads.head())
#print(northmh.head())
fig, ax = plt.subplots(2,2,facecolor="lightgrey",figsize=(12,12))
fire.plot(cmap='viridis',ax=ax[1,1],column="DAYNIGHT",legend=True)
india.plot(cmap="magma",ax=ax[0,1],column="ST_NAME",legend=True,legend_kwds={"loc":"lower right","bbox_to_anchor":(.5, 0, .5, 0),"fontsize":3})
roads.plot(cmap='plasma',ax=ax[0,0],column="RTT_DESCRI",legend=True)
northmh.plot(cmap='viridis',ax=ax[1,0],column="Dist_Name",legend=True,legend_kwds={"loc":"lower right","bbox_to_anchor":(0.5, 0., 0.5, 0.5)})
plt.tight_layout()

plt.show()
