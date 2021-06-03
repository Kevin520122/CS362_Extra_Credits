#O(n) method via hashmap
def target_sum(arr, sum):
    checkDic = {}
    for i in range(0, len(arr)):
        diff = sum - arr[i]
        #if the complement number already in the dictionary,
        #return the result
        if diff in checkDic.keys():
            return[diff, arr[i]]
        #Put the dictionary with current value and index
        checkDic[arr[i]] = i

    print("No these 2 numbers!")

print(target_sum([2,7,11,15], 9))



