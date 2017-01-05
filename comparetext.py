
from collections import OrderedDict

from nltk import word_tokenize, RegexpTokenizer, sent_tokenize


def remove_stopcompare(s):
    filtered_sentence=[]
    for i in s:
        filtered_sentence.append(i)

    filtered_sentence=" ".join(filtered_sentence)
    #print(filtered_sentence)
    return filtered_sentence

text1lines={}
text2lines={}
linecount1=1
linecount2=1


def make_sentencecompare(f):
    global text1lines
    global linecount1
    tokenizer = RegexpTokenizer(r'\w+')
    sent = sent_tokenize(f)
    new = open("2.txt", "w", encoding="utf-8")
    ctr=1
    for s in sent:
        s = tokenizer.tokenize(s)
        text1lines[ctr] = s
        s = remove_stopcompare(s)
        new.write(s + "." + "\n")
        linecount1+=1
        ctr+=1

    new.close()


def make_sentencecompare2(f):
    global text2lines
    global linecount2
    tokenizer = RegexpTokenizer(r'\w+')
    sent = sent_tokenize(f)
    new = open("4.txt", "w", encoding="utf-8")
    ctr=1
    for s in sent:
        s = tokenizer.tokenize(s)
        text2lines[ctr] = s
        s = remove_stopcompare(s)
        new.write(s + "." + "\n")
        linecount2+=1
        ctr += 1

    new.close()

dicttext1={}
dicttext2={}


def make_dicttext1(wordlist):
    temp=[]
    ctr=1
    global dicttext1
    for i in range(0,len(wordlist)):     #i is an integer
        if str(wordlist[i]) !=".":            #in a sentence
            #temp.append(wordlist[i])
            if dicttext1.get(str(wordlist[i]),"None")=="None":

                temp2=[]
                for w in wordlist[i:len(wordlist)]:     # w is a word
                    if w !='.':
                        temp2.append(w)

                    else:
                        temp2.append(ctr)         #adding the line no. at the end
                        break
                dicttext1[str(wordlist[i])]=[]
                dicttext1[str(wordlist[i])].append(temp2)
                temp2=[]
                '''f1=open("3n.txt","w")
                f1.write(dict)
                f1.close()'''


            else:

                temp2=[]
                for w in wordlist[i:len(wordlist)]:
                    if w!=".":
                        temp2.append(w)
                    else:
                        temp2.append(ctr)
                        break
                dicttext1[str(wordlist[i])].append(temp2)
                '''
                f2=open("3n.txt","w+")
                f2.write(dict)
                f2.close()'''
        else:
            ctr+=1
    #print(dicttext1)


def make_dicttext2(wordlistuser):
    temp=[]
    ctr2=1
    global dicttext2
    for i in range(0,len(wordlistuser)):
        if str(wordlistuser[i]) !=".":
            #temp.append(wordlist[i])
            if dicttext2.get(str(wordlistuser[i]),"None")=="None":

                temp2=[]
                for w in wordlistuser[i:len(wordlistuser)]:     # w is a word
                    if w !='.':
                        temp2.append(w)

                    else:
                        temp2.append(ctr2)
                        break
                dicttext2[str(wordlistuser[i])]=[]
                dicttext2[str(wordlistuser[i])].append(temp2)
                temp2=[]
                '''f1=open("3n.txt","w")
                f1.write(dict)
                f1.close()'''


            else:

                temp2=[]
                for w in wordlistuser[i:len(wordlistuser)]:
                    if w!=".":
                        temp2.append(w)
                    else:
                        temp2.append(ctr2)
                        break
                dicttext2[str(wordlistuser[i])].append(temp2)
                '''
                f2=open("3n.txt","w+")
                f2.write(dict)
                f2.close()'''
        else:
            ctr2+=1

finalcopiedt1={}
finalcopiedt2={}


def checking():
    global finalcopiedt1
    global finalcopiedt2
    global dicttext2
    global dicttext1
    global text1lines
    global text2lines
    copiedt1={}
    copiedt2={}
    for w in dicttext2.keys():
        if w in dicttext1.keys():
            t=dicttext1[w]
            t2=dicttext2[w]
            #print(t)
            #print(t2)
            temp=[]
            for i in t2:
                for j in t:
                    for k in range(0,min(len(i),len(j))):

                        if i[k]==j[k]:
                            temp.append(i[k])

                        else:
                            break
                    #print("this is a copied list")
                    if copiedt1.get(j[-1], "None") == "None":
                        copiedt1[j[-1]]=[]
                        copiedt1[j[-1]].append(temp)
                    else:
                        copiedt1[j[-1]].append(temp)
                    if copiedt2.get(i[-1], "None") == "None":
                        copiedt2[i[-1]]=[]
                        copiedt2[i[-1]].append(temp)
                    else:
                        copiedt2[i[-1]].append(temp)

                    #print(temp)
                    temp=[]
    #print("copied t1")
    #print(copiedt1)
    #print(copiedt2)
    for i in copiedt1.keys():
        c=max(copiedt1[i],key=len)
        finalcopiedt1[i]=c
    for i in copiedt2.keys():
        c=max(copiedt2[i],key=len)
        finalcopiedt2[i]=c
    #print("this is copied t1")
    #print(finalcopiedt1)
    #print(finalcopiedt2)
    #print(text1lines)
    #print(text2lines)

comparetxtdict1=OrderedDict()
comparetxtdict2=OrderedDict()
ttime=None
plagrate1=0
plagrate2=0


def comparetext(text1,text2):
    global ttime
    global dicttext1
    global dicttext2
    global finalcopiedt1
    global finalcopiedt2
    global text1lines
    global text2lines
    global linecount2
    global linecount1
    global comparetxtdict1
    global comparetxtdict2
    global plagrate1
    global plagrate2
    dicttext1={}
    dicttext2={}
    finalcopiedt1={}
    finalcopiedt2={}
    text1lines={}
    text2lines={}
    linecount2=1
    linecount1=1
    comparetxtdict2=OrderedDict()
    comparetxtdict1=OrderedDict()
    #text1=comparetxt.cleaned_data['text1']
    #text2=comparetxt.cleaned_data['text2']
    text1=text1.strip()
    text1=text1.lower()
    text2 = text2.strip()
    text2 = text2.lower()
    make_sentencecompare(text1) # list of sentences of text1
    make_sentencecompare2(text2)# list of sentences of text2
    f = open("2.txt", "r")
    fr = f.read()
    wordlisttext1 = word_tokenize(fr)
    #print(wordlisttext1)
    # word.remove("." )
    make_dicttext1(wordlisttext1)
    f.close()
    f = open("4.txt", "r")
    fr = f.read()
    wordlisttext2 = word_tokenize(fr)
    # print(wordlist)
    # word.remove("." )
    make_dicttext2(wordlisttext2)
    f.close()
    checking()
    #print(linecount1)
    #print(linecount2)
    counter=1
    counter2=2
    for i in range(1, linecount1):
        t1 = text1lines[i]
        if finalcopiedt1.get(i, "none") != "none":
            t2 = finalcopiedt1[i]
            for word in t1:
                if word not in t2:
                    comparetxtdict1[counter] = word
                    counter += 2
                else:
                    comparetxtdict1[counter2] = word
                    counter2 += 2
        else:
            for word in t1:
                comparetxtdict1[counter] = word
                counter += 2
                # comparetxtdict1["period"] =". "
    counter = 1
    counter2 = 2

    for i in range(1, linecount2):
        t1 = text2lines[i]
        if finalcopiedt2.get(i, "none") != "none":
            t2 = finalcopiedt2[i]
            for word in t1:
                if word not in t2:
                    comparetxtdict2[counter] = word
                    counter += 2
                else:
                    comparetxtdict2[counter2] = word
                    counter2 += 2
        else:
            for word in t1:
                comparetxtdict2[counter] = word
                counter += 2
                # comparetxtdict1["period"] =". "

    #print(comparetxtdict1)
    copied = 0
    notcopied = 0
    for i in comparetxtdict1.keys():
        if i % 2 == 0:
            copied += 1
        else:
            notcopied += 1
    plagrate1 = (copied / (copied + notcopied)) * 100
    copied = 0
    notcopied = 0
    for i in comparetxtdict2.keys():
        if i % 2 == 0:
            copied += 1
        else:
            notcopied += 1
    plagrate2 = (copied / (copied + notcopied)) * 100
    #print("plagrate 1 & plagrate2")
    #print(plagrate1)
    #print(plagrate2)
    #print(comparetxtdict1)
    #print(comparetxtdict2)
    final[1]=[]
    final[2]=[]
    for i in comparetxtdict1.keys():
        if int(i) % 2 == 0:
            final[1].append(comparetxtdict1[i])
    for i in comparetxtdict2.keys():
        if int(i) % 2 == 0:
            final[2].append(comparetxtdict2[i])
    return final
finalt1=[]
finalt2=[]
final={}
#comparetext("ram is going market. shyam eats apple","shyam is going market")
