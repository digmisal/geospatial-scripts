
import pandas as pd
import geopandas
import matplotlib.pyplot as plt
df= pd.DataFrame({'City': ["mumbai", "aurangabad", "pune", "nagpur", "nashik"],
                  'Longitude': [72, 75, 74, 77,73],
                  'Latitude': [19,20,18, 20, 20]})
print(df)
gdf= geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.Longitude, df.Latitude))
print(gdf.head())
gdf.plot()
plt.show()
