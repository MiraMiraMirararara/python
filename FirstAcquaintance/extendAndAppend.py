li = ['a', 'b', 'c']  
li.extend(['d', 'e', 'f'])   
print(li) #['a', 'b', 'c', 'd', 'e', 'f']
print(len(li))    #6       
li = ['a', 'b', 'c']  
li.append(['d', 'e', 'f'])   
print(li)#['a', 'b', 'c', ['d', 'e', 'f']]
['a', 'b', 'c', ['d', 'e', 'f']]  
print(len(li))   #4                    
