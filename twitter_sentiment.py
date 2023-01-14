from textblob_de import TextBlobDE as TextBlob
import pandas as pd
import numpy as np
import random
import re

data = pd.read_csv('YoutubeComments.csv', on_bad_lines='skip')

count = 0

while (count < 5):

    text = (data.values[random.randint(0, 1000)])

    textString = " ".join(str(x) for x in text)

    textStringRegex = re.sub('[^ ]*http[^ ]*', '', textString)

    textStringRegexTwo = re.sub('[@#]', '', textStringRegex)    

    blob = TextBlob(textStringRegexTwo)
    sentiment = blob.sentiment.polarity 


    print("----------------")
    print(textStringRegexTwo)
    print(sentiment)
   
    count = count + 1

else: 
    print("----------------")