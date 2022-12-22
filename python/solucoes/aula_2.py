f=open("files/clubes_pts.txt", "r+")

lista = f.read().strip().split("\n")
nova_lista = []

for auxiliar in lista:
    time = auxiliar.split(" - ")
    nova_lista.append(time)

nova_lista.sort(key= lambda x: x[1], reverse= True)
for index , time in enumerate(nova_lista):
    string ="{} - TIME:{} {} pts".format((index+1),time[0],time[1])
    print(string)
    f.write(string)
    f.write("\n")

