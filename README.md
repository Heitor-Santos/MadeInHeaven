# Criatividade - Grupo 08 - OpenAI
Criatividade - Grupo 08 - OpenAI

[Colab](https://colab.research.google.com/drive/1rbxMwH6MJCl7dwnCjejW3VwUQaVGKXGb?usp=sharing) 

# Sinopse
Utilizamos o Jukebox da OPEN AI + Versão Alternativa do Jukebox da OPEN AI para gerar músicas utilizando amostras de aúdio, artista, gênero e respeitando uma letra. 

# Desenvolvimento

Além do Notebook que fizemos e modificamos de acordo com a cadeira, para fazer a ferramente que vai otimizar a experiência do usuário para a geração de músicas. Tivemos alguns trabalhos em tratar os dados de [Artistas](https://github.com/openai/jukebox/blob/master/jukebox/data/ids/v3_artist_ids.txt)  e [Generos](https://github.com/openai/jukebox/blob/master/jukebox/data/ids/v3_genre_ids.txt)  que são disponibilizados pela Jukebox, os scripts que utilizamos para tratar eles e também para gerar as fotos que utilizamos, estão na pasta de `pre-processing`.

* `download_artist.py`: Dado a Lista de Artistas utilizando a biblioteca `simple_image_download`, vamos baixar as fotos dos artistas
* `chose-photos.py`: Arquivo responsável por mover as imagens para a pasta de destino.
* `genre_artist_fix.py`: Arquivo responsável por tratar a lista de gêneros e artistas para gerar um array em formato de string para usar no colab para ser transformado em um dropdown.
* `pre-procs.py`: Arquivo responsável por tratar as imagens, removendo os arquivos que não são fotos, muito pequenas ou corrumpidas.

# Amostra de trabalhos anteriores

[Galeria JukeBox Soundcloud](https://soundcloud.com/antonio-barros-da-silva-netto/sets/galeria-jukebox) 



