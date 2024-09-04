f_read=open("C:\\Users\\ABI\\Desktop\\PythonJuneWorks\\FILE PROGRAMS\\news.txt","r")
 
word_list=[]    
for line in f_read:

    word=line.rstrip("\n").split(" ")

    for w in word:

        word_list.append(w)
        wc={w:word_list.count(w) for w in word_list}
      
print(word_list)
print(wc)
def get_value(key):

    return wc.get(key)
    
srt=sorted(wc,key=get_value,reverse=True)
print(srt)



