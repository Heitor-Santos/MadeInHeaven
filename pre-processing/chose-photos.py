import os
import shutil

for pasta_music in os.listdir('./'):
    if(pasta_music != 'pre-procs.py' and  pasta_music != 'chose-photos.py' and pasta_music != 'photos'):
        for artist in os.listdir('./'+pasta_music):
            if len(os.listdir('./'+pasta_music+'/'+artist))> 0:
              image = os.listdir('./'+pasta_music+'/'+artist)[0]
              extens = image[-3:]
              if not os.path.isfile('./photos/'+artist+'.'+extens):
                os.rename('./'+pasta_music+'/'+artist+'/'+image, './photos/'+artist+'.'+extens)

