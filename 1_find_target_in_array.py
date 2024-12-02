def locate_card(cards,query):
    lo,hi=0, len(cards)

#if the array is empty return -1
    if(hi==0):
        return -1
    
    while lo<=hi:
        #locating the mid value
        mid=(lo+hi)//2

        mid_num=cards[mid]

        print('lo: ',lo,  ' hi: ',hi, ' mid: ', mid)

        if(mid_num==query):
            print("query found at: ",mid)
            return mid
        elif (mid_num>query):
            lo=mid+1
        elif (mid_num<query):
            hi=mid-1
    
    return -1
        
test_cases=[{input:{'cards':[1,2,3,4,5,7,9],'query':7},'output':5},{input:{'cards':[], 'query':-1}, 'output':5}]


locate_card([9,6,4,2,0,-1],-1)