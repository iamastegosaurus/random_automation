from tika import parser
from gtts import gTTS
from playsound import playsound

output = 'out.mp3'
filename = 'blink.pdf'

raw = parser.from_file(filename)
text = raw['content']

sp = gTTS(text=text, lang = 'en')
sp.save(output)

