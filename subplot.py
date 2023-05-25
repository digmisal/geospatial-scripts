import geopandas as gpd
import matplotlib.pyplot as plt
india=gpd.read_file(r"E:\downloads1\IND_wat\IND_water_areas_dcw.shp")
fire=gpd.read_file(r"E:\downloads1\MODIS_C6_1_South_Asia_24h\MODIS_C6_1_South_Asia_24h.shp")
roads=gpd.read_file(r"E:\downloads1\IND_rds\IND_roads.shp")
northmh=gpd.read_file(r"E:\aster\northmaharastra.shp")

ax1=plt.subplot(221)
india.plot(ax=ax1,figsize=(5,5))


ax2=plt.subplot(222)
fire.plot(ax=ax2)


ax3=plt.subplot(223)
roads.plot(ax=ax3)


ax4=plt.subplot(224)
northmh.plot(ax=ax4)


ax1.set_axis_off()
plt.show()
