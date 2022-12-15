import folium
from desafio.lib_local import Location

file = open("files/lat_lon.txt", "r")
data = file.read().split("\n")
List_Points = []
for value in data:
    List_Points.append(value.split(","))

ObjectList = []
for i in range(0, len(List_Points[0])):
    if List_Points[0][i] != "" and List_Points[1][i] != "" and List_Points[2][i] != "":
        ObjectList.append(Location(lat=List_Points[0][i], lon=List_Points[1][i], name=List_Points[2][i]))


map = folium.Map(location= [ObjectList[0].lat, ObjectList[0].lon], zoom_start=17)
for point in ObjectList:
    point.Plot(map=map)
map.save("index.html")
