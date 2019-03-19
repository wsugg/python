#"mary had a little lamb reversed"
revStr = ""

str = [' ','m','a','r','y',' ','h','a','d',' ','a',' ','l','i','t','t','l','e',' ','l','a','m','b']

print("Mary had a little lamb, reversed Rev4.0" + "\n")
print ("This is the Original String str= {}" .format(str) + "\n\n")

cnt = len(str)
print ("The array item count is:\t {}" .format(cnt) + "\n")

for s in str:
    print(str[cnt-1])
    revStr += str[cnt-1]
    cnt = cnt-1

print("This is the reversed string: {}" .format(revStr) +"\n")

# correct spelling but leave words in reversed order. 

revStr = list(revStr) # make the string a list array. 
print ("This is the string before correcting for spelling:\t {}" .format(revStr))
cntRevStr = len(revStr)      
startCount = 0     #start of a word
endCount = 0       #the space after a word, used as the end.  
c = ""             #char to pop off the array.


for s in revStr:
    endCount +=1
    if (s == ' ') or (endCount == len(revStr)):
        #need to keep track of start of word and end   
        #print ("space", endCount) #for debugging
        space = endCount - 1
        for i in range(((space - startCount) - 1)):
            c = revStr.pop(space - 1)
            revStr.insert((startCount + i), c )
            #print c for debugging
        startCount = endCount
print("\nString with spelling corrected: {}" .format(revStr))


#end