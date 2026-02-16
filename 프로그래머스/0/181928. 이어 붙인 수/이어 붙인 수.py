def solution(num_list):
    oddL=[]
    evenL=[]
    for x in num_list:
        if x%2==1:
            oddL.append(str(x))
        else:
            evenL.append(str(x))
    odd=''
    even=''
    for x in oddL:
        odd+=x
    for x in evenL:
        even+=x
    return int(odd)+int(even)