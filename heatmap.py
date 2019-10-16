import folium
from folium.plugins import HeatMap
from folium.plugins import HeatMapWithTime
import csv


heat_lats_U10 = []
heat_lons_U10 = []
signal_U10 = []

heat_lats_1020 = []
heat_lons_1020 = []
signal_1020 = []

heat_lats_2030 = []
heat_lons_2030 = []
signal_2030 = []

heat_lats_A30 = []
heat_lons_A30 = []
signal_A30 = []

with open('planelog.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if (float(row[3]) < 10000):
            heat_lats_U10.append(float(row[4]))
            heat_lons_U10.append(float(row[5]))
            signal_U10.append(float(row[6]))
        if (float(row[3]) >= 10000 and float(row[3]) < 20000):
            heat_lats_1020.append(float(row[4]))
            heat_lons_1020.append(float(row[5]))
            signal_1020.append(float(row[6]))
        if (float(row[3]) >= 20000 and float(row[3]) < 30000):
            heat_lats_2030.append(float(row[4]))
            heat_lons_2030.append(float(row[5]))
            signal_2030.append(float(row[6]))
        if (float(row[3]) >= 30000):
            heat_lats_A30.append(float(row[4]))
            heat_lons_A30.append(float(row[5]))
            signal_A30.append(float(row[6]))

hmap = folium.Map(location=[47.4660, 8.3266], zoom_start=10)

hmU10 = HeatMap( list(zip(heat_lats_U10, heat_lons_U10, signal_U10)),
                   min_opacity=0.1,
                   max_val= 150,
                   radius=4, blur=4, 
                   max_zoom=12, 
                   control=True,
                   show=True,
                   name='-10000',
                 )
hm1020 = HeatMap( list(zip(heat_lats_1020, heat_lons_1020, signal_1020)),
                   min_opacity=0.1,
                   max_val= 150,
                   radius=4, blur=4, 
                   max_zoom=12, 
                   control=True,
                   show=False,
                   name='10000-20000',
                 )
hm2030 = HeatMap( list(zip(heat_lats_2030, heat_lons_2030, signal_2030)),
                   min_opacity=0.1,
                   max_val= 150,
                   radius=4, blur=4, 
                   max_zoom=12, 
                   control=True,
                   show=False,
                   name='20000-30000',
                 )
hmA30 = HeatMap( list(zip(heat_lats_A30, heat_lons_A30, signal_A30)),
                   min_opacity=0.1,
                   max_val= 150,
                   radius=4, blur=4, 
                   max_zoom=12, 
                   control=True,
                   show=False,
                   name='30000+',
                 )

layercontrol = folium.map.LayerControl()
"""
hm = HeatMapWithTime( list(zip(heat_lats, heat_lons)),
                 )
"""
hmap.add_child(hmU10)
hmap.add_child(hm1020)
hmap.add_child(hm2030)
hmap.add_child(hmA30)
hmap.add_child(layercontrol)
hmap.save('planeheatmap.html')