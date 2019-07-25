def reverseWordSentence(a): 
    words = a.split(" ") 
    newWords = [word[::-1] for word in words] 
    newSentence = " ".join(newWords) 
    return newSentence   
a=str(input())
print(reverseWordSentence(a))                                                                              
