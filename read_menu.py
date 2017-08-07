import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import urllib2
import jsonlines

print 'reading image'
image = 'menu.jpg'
im = Image.open(image) # the second one 
text = pytesseract.image_to_string(Image.open(image))

#fuzzy find
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

#read in json
print 'reading json'
data = []
choices = []
import json
with jsonlines.open('output.json') as reader:
    for line in reader:
        data.append(line)
        choices.append(line['title'] + ' ' +  line['location'])
        choices.append(line['title'])

print 'defining text'
for each in text.split('\n'):
    t = True
    if len(each) > 15 and len(each) < 35:
        guess = process.extract(each, choices, limit=3, scorer=fuzz.token_sort_ratio) 
        for every in guess:
            if every[1] > 50:
                if t == True:
                    print
                    print each
                    t = False
                print every[0]

