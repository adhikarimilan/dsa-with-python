def locate_card(cards,query):
    lo,hi=0, len(cards)-1

#if the array is empty return -1
    if(hi<0 or lo>len(cards)-1):
        return -1
    
    while lo<=hi:
        #locating the mid value
        mid=(lo+hi)//2

        mid_num=cards[mid]

        print('lo: ',lo,  ' hi: ',hi, ' mid: ', mid)

        if(mid_num==query):
            #checking if the query element is repeated and is on the left
            #first occurence of the element is returned
            if(mid-1>=0 and cards[mid-1]==query):
                hi=mid-1
            else:
                print("query found at: ",mid)
                return mid#found
        elif (mid_num>query):
            lo=mid+1
        elif (mid_num<query):
            hi=mid-1
    
    return -1
        
test_cases=[{input:{'cards':[1,2,3,4,5,7,9],'query':7},'output':5},{input:{'cards':[], 'query':-1}, 'output':5}]

print("Test case 1")
locate_card([2],2)
print("Test Case 2")
locate_card([5,3,2,1,1],1)
print("Test case 3")
locate_card([5,-1,-1,-1,-1],-1)