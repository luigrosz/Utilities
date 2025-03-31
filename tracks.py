import json
from re import L
import requests

#  Script para baixar musicas do deezer via streamrip (necessario json da playlist manualmente colocado no diretorio)

tracks_urls = []
notfound_urls = []

with open('playlist.json', encoding = 'utf-8') as f:
  file = f.read()
dataJson = json.loads(file)


# ////////
for item in dataJson['tracks']['data']:
  tracks_urls.append(item['link'])

print("escrevendo no 'tracks.txt' a url das musicas da playlist e no arquivos 'notfound_tracks.txt' as urls quebradas... \n\n")
for i in range(len(tracks_urls)):
  with open('tracks.txt', "w") as outfile:
    outfile.write("\n".join(tracks_urls))
  response = requests.get(tracks_urls[i])

  if response.status_code != 200:
    notfound_urls.append(tracks_urls[i])

  with open('notfound_tracks.txt', "w") as outfile:
    outfile.write("\n".join(notfound_urls))


tracks_urls = []
notfound_urls = []

# //////
with open('notfound_tracks.txt', "r") as f:
  notfound_urls = f.readlines()

notfound_urls = [line.strip() for line in notfound_urls]

for item in dataJson['tracks']['data']:
  if(item['link'] in notfound_urls):
    tracks_urls.append(item['title_short'])

print("escrevendo os titulos de todas as musicas com url quebradas no arquivos 'notfound_tracks_names.txt'...\n\n")
with open('notfound_tracks_names.txt', "w") as outfile:
  outfile.write("\n".join(tracks_urls))


tracks_urls = []
notfound_urls = []

# /////
with open('notfound_tracks_names.txt', "r") as f:
  notfound_urls = f.readlines()

notfound_urls = [line.strip() for line in notfound_urls]

print("requisitando a url correta de todas as musicas quebradas... \n\n")
for i in range(len(notfound_urls)):
  response = requests.get(f"https://api.deezer.com/search?q={notfound_urls[i]}")
  response = response.json()
  tracks_urls.append(response['data'][0]['link'])

print("escrevendo-as no arquivo 'notfound_tracks_urls_RIPTHIS.txt'... \n\n")
with open('notfound_tracks_urls_RIPTHIS.txt', "w") as outfile:
  outfile.write(" ".join(tracks_urls))

tracks_urls = []
notfound_urls = []

with open('notfound_tracks.txt', "r") as f:
  notfound_urls = f.readlines()

notfound_urls = [line.strip() for line in notfound_urls]

with open('tracks.txt', "r") as f:
  tracks_urls = f.readlines()

tracks_urls = [line.strip() for line in tracks_urls]

new_tracks = []
for item in tracks_urls:
  if(item in notfound_urls):
    continue
  new_tracks.append(item)

print("escrevendo urls das musicas com url nao quebradas no arquivo 'found_tracks_urls_RIPTHIS.txt'...\n\n")
with open('found_tracks_urls_RIPTHIS.txt', "w") as outfile:
  outfile.write(" ".join(new_tracks))
