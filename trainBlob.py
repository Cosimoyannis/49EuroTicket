from textblob_de.classifiers import NaiveBayesClassifier
from textblob_de import TextBlobDE as TextBlob
import pandas as pd
import numpy as np
import random
import re


# ------------ textblob model wird trainiert

train = [
    #pos
    ('Ja gut, man kann es ohnehin Niemanden Recht machen mit dieser Lösung.In wenigen individuellen Fällen ist das 49 Euroticket halt teuer. Wer die etwas weitere Lösung also nicht braucht, muss dieses ja auch nicht kaufen. Der Mehrheit aller Pendler und übrigen Menschen bringt dieses Ticket auf jeden Fall etwas.', 'pos'),
    ('@S. H.  Finde ich aber echt gut, dass er endlich die Freiheit bekommen zu machen was wir wollen Ohne den Tarifdschungel.', 'pos'),
    ('49€ ist voll ok würde auch mehr zahle ja für meine Monatskarte in einer Kleinstadt fast so viel', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    #neg
    ('Achhh kommm hör mir auf 50 Euro ticket viel zu teuer das können sich teilweise Leute immer noch nicht leisten. Diese Politik ist am arsch', 'neg'),
    ('@Juliz 49 ist aber vielen trotzdem zu viel', 'neg'),
    ('Das Ticket umfasst sämtlichen Regional Verkehr egal ob bus, bahn, ubahn, ...Nur keinen Fernverkehr und wahrscheinlich auch keine Sonderzüge also ich mein die Firmen die Historische Schmalspurstrecken mit Dampflok betreiben.', 'neg'),
    ('49€ Ticket ist einfach lose lose, zu teuer als das es eine Mehrheit einfach kauft weil es ja so günstig ist und die Verkehrsbetriebe haben massive Einnahmeeinbußen durch den Wegfall der teureren Abotickets.', 'neg'),
    ('Nicht gut. Nur digital, nur im Abo, und zu teuer. Hat nicht wirklich viel mit dem 9 Euro Ticket gemeinsam. Und so wundert es nicht, dass Experten sagen, dass es die Inflation kaum beeinflussen wird', 'neg'),

    #pos
    ('@Soren_Meyer14 Ja das stimmt. Das #9EuroTicket war ein Traum. Aber das #49EuroTicket/#Deutschlandticket ist ein erster Schritt in die richtige Richtung. Klar ist: Mehr Geld in den ÖPNV und Zugverkehr.', 'pos'),
    ('Das 49€ Ticket ist super. Es ist unkompliziert, billiger und bringt frischen Wind in den ÖPNV. Aber wie nennt ihr das Ticket? #49EuroTicket oder #Deutschlandticket?', 'pos'),
    ('Herr @Wissing die Menschen haben das #9euroticket geliebt, und nicht die @fdp! 😉 #Maischberger', 'pos'),
    ('Good News zum #HVV-Jobticket: Mit Einführung des #49EuroTicket werden alle Tickets auf max. 49€ gesenkt und darauf kommt der volle Arbeitgeberzuschuss. Wer so eine Karte hat, zahlt also nur ca. 34€ für die Deutschland-Flat. Details hier: https://t.co/mvLpUbhRRP #hamburg #bahn https://t.co/KS9zsqB2jG', 'pos'),
    ('Erfolgsprojekt 9-Euro-Ticket: DVB mit Rekorden im vergangenen Sommer. #Dresden #DVB #Rekord #9EuroTicket #Fahrgastzahlen #Stadtbahn #Bus #ÖPNV https://t.co/FRjTZUPedG', 'pos'),
    #neg
    ('Alles scheiß Betrüger', 'neg'),
    ('Das Ticket ist super unnötig', 'neg'),
    ('Wisst Ihr noch, diese Idee vom deutschlandweit gültigen #49EuroTicket? Schäm mich bisschen, dass ich ‘ne Weile echt dran geglaubt habe.', 'neg'),
    ('Bevor das #49EuroTicket eingeführt wird, erhöht der Augsburger Verkehrs- und Tarifverbund erstmal das Monats-Abo von 104 € auf 114,50 € pro Monat.', 'neg'),
    ('Ihr könnt mir hier erzählen was ihr wollt, aber der Nachfolger des #9euroticket wird ein Reinfall. #Deutschlandticket #Maischberger @Wissing https://t.co/uql89Gkg8k', 'neg'),
    ('grausame Idee', 'neg'),
    ('Mir gefällt das 49 ticket übertrieben gut', 'pos'),
    ('Natürlich verarschen die #Politiker und die #Bahn-Vorstände die #Kunden, die #Bürger... Nach dem Beschwichtigungs-#9euroticket sollte das #49EuroTicket kommen. Dann wurde es in #DeutschlandTicket umgetauft... Logisch, dass es stets teurer werden wird. https://t.co/wikSvFbGlF', 'neg')


]
test = [
    ('Nicht gut. Nur digital, nur im Abo, und zu teuer. Hat nicht wirklich viel mit dem 9 Euro Ticket gemeinsam. Und so wundert es nicht, dass Experten sagen, dass es die Inflation kaum beeinflussen wird', 'pos'),
    ('49 Euro ist ein Witz und einfach nur ein Schlag ins Gesicht. Was ist mit all den Menschen die sich so einen Preis schon vor dem 9 Euro Ticket nicht leisten konnten ? Kein Brot im Schrank, Heizung aus, Auto abgemeldet. Alle Gutverdiener müssenb ETWAS sparen und werden trotz höhrem Einkommen nicht solidarisch zur KAsse gebeten. FDP: Toll gemacht.Toll, daß Menschen die jetzt gerade mehr bezahlen sich freuen. Aber es gibt Menschen, die erst durch den günstigen Preis von 9 Euro überhaupt mobil wurden. Was ist dann mit den sonst vergünstigten Monatskarten wie Ticket 2000, Sozialticket etc. werden die dann abgeschafft ? oder muß zum Bsp. ein Sozialempfänger sich das 35€ Ticket kaufen, weil es kein 9 Euro Ticket mehr gibt und er sich 49 nicht leisten kann ? Und ist das dann auch deutschlandweit gültig ? Der Preis von 49 Euro ist in Zeiten von 100erten MILLIARDEN Sondervermögen für dies und das , sowie der Scheinheiligkeit des Finanzministers eine Lachnummer und ein Schlag ins Gesicht. Autos und KFZ Infrastruktur werden mit einem zig-fachen mehr subventioniert, als das 9Euro Ticket Kosten würde. E-Fuel Abkommen für die Porsche AG (Lindner bekommt bestimmt nicht nur die Wartungseinen 911ers gratis..), Milliarden für die Stromerzeuger, aber eine im Vergleich lächerliche Summe für eine komplette Fortführung des 9 Euro Tickets nicht erwünscht. Dabei würde daß Mal wirklich bei der ganzen Scheis..e die unsere Regierung verzapft, mal für ein gutes Gefühl sorgen. Aber daß ist wohl offensichtlich nicht erwünscht, angesicht der Einfachen Rechnungen mit den Kosten ein solchen Tickets vs KFZ Subventionen vs Militärausgabe vs Milliarden Stuergeschenke füür die Strom und Ölmultis vs Steuerverschwendungen. Das kann jedes Kleinkind besser, als unsere Regierung. Wohin soll das führen ??49 € ffühlt sich jetzt ´günstig´´  an ? Dafür ist ja auch die 3 Monatige Wartezeit da. Man hätte schon vor Beginn des 9 Eurotickets einen NAchfolger beschließen können. Aber besser den MEnschen nach dem Ticket erstmal wieder zeigen, wie super teuer alles ist, damit man sich dann über ein 49 Euro Ticket ,Almosen´´ freut. Einfach nur manipulativ. Alle Bürger werden für dumm verkauft, Einfachheit ist nun daß Zauberwort. Nur nocht über die vielen Milliarden reden, die sich die Multimiliardäre in die Tasche stecken. Tankrabbatm Sondervermögen, keine Übergewinnsteuer. Was will diese Regierung machen ? Denkt malö drüber nach. So was habe ich nicht gewählt.Was für eine Verarsche', 'neg'),
    ("49€Euro Ticket ist eine reine Provokoation hätte da lieber 58 bezahlt", 'neg'),
    ("Klingt gut - allein als Student in Raum Erlangen/Nürnberg wäre es zu gebrauchen da das Semesterticket absolut zu nichts zu gebrauchen ist", 'pos'),
    ('49 € sind top', 'pos'),
    ("Für mich sind 49 € auch keine Option. So oft fahre ich nicht mit dem ÖPNV. Meist bin ich doch eher auf das Auto angewiesen.", 'neg'),
    ('Das Ticket ist einer absoluter Erfolg', 'pos'),
    ('Man stelle sich vor 50 Leute, die im teuren Auto im Stau stehen, würden stattdessen für 9 € mtl im Bus sitzen und zügig voran kommen Wäre möglich, wenn der ÖPNV ausgebaut, das erfolgreiche #9euroticket eingeführt und die Leute ihre Autos abschaffen würden https://t.co/hbG2pB9Qcs', 'pos'),
    ('na dann, zack zack, da wäre der 1.2.2023 locker schaffbar #49EuroTicket #Deutschlandticket #9EuroTicket https://t.co/BJlrDhUfE9', 'pos'),
    ('Für mich nicht finanzierbar. #49euroticket #Deutschlandticket', 'neg'),
    ('Bringt gar nichts!', 'neg'),
    ('Ich kann gar nicht sagen, an wie vielen Dingen die #FDPmachtkrankundarm (teils seit Jahrzehnten) festklebt, obwohl diese nachweislich Unfug sind…', 'neg')
]

cl = NaiveBayesClassifier(train)

# Test - Classify some text
# print(cl.classify("Mir gefällt das 49 ticket übertrieben gut"))  # "pos"
# print(cl.classify("Das Ticket ist super unnötig"))   # "neg"






# ------------ CSV wird mit sentiment analysiert

data = pd.read_csv('YoutubeComments.csv', on_bad_lines='skip')

count = 0

while (count < 5):

    text = (data.values[random.randint(0, 1000)])

    textString = " ".join(str(x) for x in text)

    textStringRegex = re.sub('[^ ]*http[^ ]*', '', textString)

    textStringRegexTwo = re.sub('[@#]', '', textStringRegex)    

    blob = TextBlob(textStringRegexTwo, classifier=cl)
    sentiment = blob.sentiment.polarity 

    print(" ") 
    print("----------------")
    print(" ") 
    print(textStringRegexTwo)
    # print(sentiment)

    # print(blob)
    print(blob.classify())

    # for sentence in blob.sentences:
       # print(sentence)
       # print(sentence.classify())

    # Compute accuracy
       # print("Accuracy: {0}".format(cl.accuracy(test)))

    # Show 5 most informative features
    #cl.show_informative_features(5)
   
    count = count + 1

else: 
    print(" ") 
    print("----------------")
    print(" ") 

