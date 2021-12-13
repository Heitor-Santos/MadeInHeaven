import os
from PIL import Image


count = 0
total = 0

for pasta_music in os.listdir('./'):
    if(pasta_music != 'pre-procs.py' and  pasta_music != 'chose-photos.py'):

        for artist in os.listdir('./'+pasta_music):
            
            for image in os.listdir('./'+pasta_music+'/'+artist):
                 total += 1
                 if os.path.getsize('./'+pasta_music+'/'+artist+'/'+image)/1024 < 50:
                    os.remove('./'+pasta_music+'/'+artist+'/'+image)
                    
                 else:
                     if image.endswith('.png') or image.endswith('.jpg'):
                        try:
                            img = Image.open('./'+pasta_music+'/'+artist+'/'+image) 
                            img.verify() 
                        except (IOError, SyntaxError) as e:
                            print('Bad file:', image)
                            os.remove('./'+pasta_music+'/'+artist+'/'+image)
                     else:
                        os.remove('./'+pasta_music+'/'+artist+'/'+image)

            if len(os.listdir('./'+pasta_music+'/'+artist)) == 0:
                os.rmdir('./'+pasta_music+'/'+artist)
                count += 1

print(count)
print(total)

