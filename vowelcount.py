def getvowel(word):
    print('The vowels in the word ','"', word ,'" ', 'are:-', end=" ")
    word=word.lower()
    lst=list()
    for i in word:
        if(i=='a')or(i=='e')or(i=='i')or(i=='o')or(i=='u'):
            lst.append(i)
    print(lst)
w=input('Enter the word')
getvowel(w)
