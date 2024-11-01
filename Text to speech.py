from gtts import gTTS
import os
mytext = 'Hello Everyone. My name is Shreya. I am going to tell you about nature.Nature is the connection between the physical world surrounding us and the life inside us. Nature is God’s most precious and valuable gift to humans. It is the principal source of all essential nutrients for all living things on the planet.Thankyou.'
language ='en'
my_work = gTTS(text=mytext,lang=language,slow=False)
my_work.save("Introduction.mp3")
os.system("start Introduction.mp3")
