#"mary had a little lamb reversed"
revStr = ""
str2 = ""
str3 = ""

str = ['m','a','r','y',' ','h','a','d',' ','a',' ','l','i','t','t','l','e',' ','l','a','m','b']

print("Mary had a little lamb, reversed Rev3.0 \n")

cnt = len(str)
print ("The array item count is:\t", cnt, "\n")

for s in str:
    print(str[cnt-1])
    revStr += str[cnt-1]
    cnt = cnt-1

print("This is the reversed string:", revStr)

#started 2:40 pm 3/15/19 
revStr = list(revStr)
print ("This is the string before correcting for spelling:\t", revStr)
cntRevStr = len(revStr) 
scnt = 0

for s in revStr:
	scnt +=1
	if s == ' ':
		print ("scnt=", scnt)
		#for c in word:  
		 
		 #print (word)





#end 
""" This works, but hacky. 
cntRevStr = len(revStr)

for s in revStr: #the words are spelled backwards and we want them spelled correctly and readable, but maintain the reveresed order "lamb little a had mary". 
 	str2 += s
 	cntRevStr -= 1
 	if (s.isspace()) or (cntRevStr == 0): #get the first word when we see a space we know its the end of a word. 
 		print(str2) #for debugging

 		str2 += " " #add the space back into the sentance. 
 		cnt2 = len(str2) #get array len of the word.
 		
 		for char in str2:
 	  		str3 += str2[cnt2-1] #reverse order of letters into a new array str3. 
 	  		cnt2 = cnt2-1
 		str2 = ""   # make str2 null now since we will start a new word. 
 		print(str3)      
print("str3\t", str3,"\n") """


