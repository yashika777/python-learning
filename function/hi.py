# nums=[22,5,4,4,6,6,8]
# freq={}
# for i in nums:
#     if i not in freq:
#                 freq[i]=1
#     else:
#                 freq[i]+=1
# highest = 0
# secondhighest = 0
# val = -1
# val2 = -1

# for key, value in freq.items():
#     if value > highest:
#         secondhighest = highest
#         val2 = val
#         highest = value
#         val = key
#     elif value > secondhighest and value != highest:
#         secondhighest = value
#         val2 = key
#     elif value==secondhighest and (val2 is None or key < val2):
#            val2=key
# print(val2)
# arr=[14,9,15,12,6,8,13]
# for i in range(0,len(arr)):
#     j=i
#     while j>0 and arr[j-1]>arr[j]:
#         arr[j-1],arr[j]=arr[j],arr[j-1]
#         j-=1
# print(arr)

    