from nltk import word_tokenize

nltk.download('punkt')

def run(fpath, ofpath):
    sentence = []
    string = []
    with open(fpath, 'r') as inf, open(ofpath, 'w') as of :
        for line in inf:
            line = line.strip()
            if line != '':
                sentence = word_tokenize(line)
                d = ' '.join([w for w in sentence])
                d = d.replace("``","''")
                d = d.replace("​","")
                #for german, add this line:
                d = d.replace("'S-MISC","' S-MISC")
                #for spanish, add this line:
                d = d.replace(".B-PER",". B-PER")
                #for italian, add this line:
                d = d.replace("'S-ORG","' S-ORG")
                print(d)
                of.write(d + '\n')
                sentence = []

tl = 'nl'
fpath = tl+'.train.new.link.txt'
ofpath = tl+'.full.txt'
run(fpath,ofpath)
tl = 'de'
fpath = tl+'.train.new.link.txt'
ofpath = tl+'.full.txt'
run(fpath,ofpath)
tl = 'es'
fpath = tl+'.train.new.link.txt'
ofpath = tl+'.full.txt'
run(fpath,ofpath)
