import pandas
import folium
from folium.plugins import HeatMap

df = pandas.read_csv('planelog.txt')

groupedf = df.groupby('id')

hmap = folium.Map(location=[47.4660, 8.3266], zoom_start=10, tiles = 'cartodbpositron')


for name, group in groupedf:
    points = group[['lat', 'lon', 'alt']]
    #points = points[(points['alt'] > 33000)]
    signalAverage = group['sig'].mean()
    points = points.values.tolist()
    folium.vector_layers.PolyLine(points, weight=1, opacity=signalAverage/250).add_to(hmap)

"""
maxes = df.sort_values('sig', ascending=False).drop_duplicates('id')
#maxes = maxes[(maxes['alt'] > 33000)]

heats = maxes[['lat','lon','sig']].values.tolist()


hm = HeatMap( heats,
                   min_opacity=0.1,
                   max_val= 50,
                   radius=10, blur=4, 
                   max_zoom=12, 
                   control=True,
                   show=True,
                   name='filtered',
                 )

hmap.add_child(hm)

layercontrol = folium.map.LayerControl()
hmap.add_child(layercontrol)
"""
hmap.save('location.html')

