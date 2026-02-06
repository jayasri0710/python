arr=[1,2,3,4]
for i in arr:
    print(i)
-------------

arr=[1,2,3]
for i in range(len(arr)):
    print(arr[i])

#append ---- add at last

arr=[10,20,30] 
arr.append(50)
print(arr)

#insert ----- insert at index

arr=[1,2,3,4]
arr.insert(2, 25)
print(arr)

#deletion of index

arr=[1,2,3,4]
arr.pop(1)
print(arr)

#deletion of value 

arr=[1,2,3,4]
arr.remove(4)
print(arr)