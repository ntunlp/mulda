from google.cloud import translate_v2 as translate
import sys
import os
import time
from nltk import word_tokenize

translator = translate.Client.from_service_account_json('google_translate.json')

#define source language and target language
sl = 'en'
tl = 'de'

fix_placehoders = {
"MISC ": "MISC",
"PER ": "PER",
"ORG ": "ORG",
"LOC ": "LOC",
"POR ": "PER",
"(POR ": "PER",
"PRO ": "PER",
"MUSC ": "MISC",
"HISC": "MISC",
"LISC": "MISC",
"MOCC": "MISC",
"LIS": "LOC",
"Misc": "MISC",
"Org": "ORG",
"Per": "PER",
"Loc": "LOC",
"loc": "LOC",
"per": "PER",
"misc": "MISC",
"org": "ORG",
"Misc ": "MISC",
"Org ": "ORG",
"Per ": "PER",
"Loc ": "LOC",
"loc ": "LOC",
"per ": "PER",
"misc ": "MISC",
"org ": "ORG",
}

def postprocess(t, dict1):
    t = t.replace("-"," ")
    t = t.replace("&quot;","\"")
    t = t.replace("&#39;","'")
    t = t.replace(" DOCSTART ","-DOCSTART-")
    for i in range(10):
        for key in fix_placehoders:
            t = t.replace(key + str(i), fix_placehoders[key]+ str(i))
    for i in range(10):
        i = "t"+str(i)
        for key in fix_placehoders:
            t = t.replace(key + str(i), fix_placehoders[key]+ str(i))
    if tl == 'nl':
        t = t.replace("PERO","PER0")
    for a, b in dict1.items():
        t = t.replace(a, b)
    t = t.replace("​","")
    return t


def preprocess(sentence):
    original = ''
    tmp = []
    string = []
    dict1 = {}
    n = 0
    s=""
    v=""
    for w in sentence:
        original = ' '.join([w[0] for w in sentence])
    print("original: ",original)
    if original == '':
        return None, dict1
    for w in sentence:
        if w[1][:1]=="S":
            s=w[0]
        elif w[1][:1]=="B":
            string.append(w[0])
        elif w[1][:1]=="I":
            string.append(w[0])
        elif w[1][:1]=="E":
            string.append(w[0])
            s = ' '.join([w for w in string])
        else:
            tmp.append(w[0])
        if s !="":
            ner = w[1][2:]
            s1 = "["+s+"]"
            new = original.replace(s,s1)
            results2 = translator.translate(new, source_language=sl, target_language=tl)
            t2 = results2['translatedText']
            t2 = t2.replace("&quot;","\"")
            t2 = t2.replace("&#39;","'")
            t2 = t2.replace("&amp;","&")
            if tl == 'nl':
                pass
            else:
                t2 = t2.replace('-',' ')
            t2 = word_tokenize(t2)
            t2 = ' '.join([w for w in t2])
            w1 = t2.split()
            l = len(w1)
            t3 = ""
            for i in range(l):
                if w1[i][:1] =="[" and w1[i][-1:] =="]":
                    t3 = w1[i]
                    break
                elif w1[i][:1] =="[" and w1[i][-1:] !="]":
                    t3 = w1[i]
                elif w1[i][:1] !="[" and w1[i][-1:] =="]":
                    t3 = t3+" "+w1[i]
                    break
                else:
                    t3 = t3+" "+w1[i]
            if "[" not in t3:
                if ner == "LOC":
                    s1 = "[Location] "+s
                elif ner == "PER":
                    s1 = "[Name] "+s
                elif ner == "ORG":
                    s1 = "[Organization] "+s
                elif ner == "MISC":
                    s1 = "[Miscellaneous] "+s
                results2 = translator.translate(s1, source_language=sl, target_language=tl)
                t2 = results2['translatedText']
                t2 = t2.replace("&quot;","\"")
                t2 = t2.replace("&#39;","'")
                t2 = t2.replace("&amp;","&")
                if tl == 'nl':
                    pass
                else:
                    t2 = t2.replace('-',' ')
                w2 = t2.split()
                l = len(w2)
                t3 = ""
                for i in range(l):
                    if w2[i][:1] !="[":
                        if i == 0:
                            t3 = w2[i]
                        else:
                            t3 = t3 +" "+w2[i]
            t3 = t3.replace("[","")
            t3 = t3.replace("]","")
            if n > 9:
                g2 =ner+"t"+str(n)
            else:
                g2 =ner+str(n)
            n=n+1
            tmp.append(g2)
            keys = []
            keys.append(g2)
            w2 = t3.split()
            l = len(w2)
            if l == 1:
                v = "S-"+ner+" "+w2[0]
            elif l > 1:
                for i in range(l):
                    if i == 0:
                        v = "B-"+ner+" "+w2[i]
                    elif i == l-1:
                        v = v+" "+"E-"+ner+" "+w2[i]
                    else:
                        v = v+" "+"I-"+ner+" "+w2[i]
            values = []
            values.append(v)
            d1 = dict(zip(keys,values))
            if dict1 == {}:
                dict1.update(d1)
            elif g2 not in dict1:
                dict1.update(d1)
            s=""
            string=[]
            ner=""
            t3=""

    return ' '.join([w for w in tmp]), dict1


def run(fpath, ofpath):
    sentence = []
    print("Start the process.")
    with open(fpath, 'r') as inf, open(ofpath, 'w') as of:
        for line in inf:
            line = line.strip()
            if line != '':
                line = line.split()
                if len(line) == 2:
                    sentence.append(line)
            else:
                sentence_preprocessed, dict1 = preprocess(sentence)
                if sentence_preprocessed is None:
                    continue
                results = translator.translate(sentence_preprocessed, source_language=sl, target_language=tl)
                t = postprocess(results['translatedText'], dict1)
                print("translated sentence: ", t)
                of.write(t + '\n')
                time.sleep(1.2)
                sentence = []

#tl = 'de'
#tl = 'es'
tl = 'nl'
fpath ='eng.train.iobes.txt'
ofpath = tl+'.train.new.link.txt'
run(fpath, ofpath)
