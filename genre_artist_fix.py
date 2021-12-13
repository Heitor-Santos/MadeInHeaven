a = "["

with open('genre_ids.txt') as f:
    lines = f.readlines()
    for line in lines:
      aux = line.split(";")[0]
      aux = aux.split("‎")[0]
      aux = aux.replace("/", " ")
      a += '"'+aux+'"'+ ", "

a = a[:-2] + "]"
print(a)

a = ""

with open('artists_ids.txt') as f:
    lines = f.readlines()
    for line in lines:
      if (line.find('"') == -1):
        aux = line.split(";")[0]
        aux = aux.split("‎")[0]
        aux = aux.replace("/", " ")
        a += aux+", "

a = a[:-2]

a = sorted(a.split(", "))

b = ''.join('"'+str(e) + '"' + ", " for e in a)

a_file = open("artist.txt", "w")
a_file.write(b)
a_file.close()

