from simple_image_download import simple_image_download as simp


def downloadPhotos(artist):
  response = simp.simple_image_download

  response().download(artist, 3)

count = 1

with open('artists_ids.txt') as f:
    lines = f.readlines()
    for line in lines:
      aux = line.split(";")[0]
      aux = aux.replace("/", " ")
      print(f'Download Arista: {aux}\nProgessão: {count} de {len(lines)}')
      downloadPhotos(aux)
      count += 1



