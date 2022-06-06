ammunition = []
weight_per_pack =[]
damage_per_pack=[]
maxweight = 0
weapons  = 0
damage = 0
def merge(arr,arr1,arr2,arr3,l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * (n1)
    R = [0] * (n2)
    L1 = [0] * (n1)
    R1 = [0] * (n2)
    L2 = [0] * (n1)
    R2 = [0] * (n2)
    L3 = [0] * (n1)
    R3 = [0] * (n2)
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i]  = arr[l + i]
        L1[i]  = arr1[l + i]
        L2[i]  = arr2[l + i]
        L3[i]  = arr3[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R1[j] = arr1[m+1+j]
        R2[j] = arr2[m+1+j]
        R3[j] = arr3[m+1+j]
    i = 0    # Initial index of first subarray
    j = 0    # Initial index of second subarray
    k = l    # Initial index of merged subarray
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr1[k] = L1[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            i += 1
        else:
            arr[k] = R[j]
            arr1[k] = R1[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        arr1[k] = L1[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        arr1[k] = R1[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        j += 1
        k += 1
def mergeSort(arr,arr1,arr2,arr3,l, r):
    if l < r:
        m = l+(r-l)//2
        mergeSort(arr,arr1,arr2,arr3,l, m)
        mergeSort(arr,arr1 ,arr2,arr3,m+1, r)
        merge(arr,arr1,arr2,arr3, l, m, r )
def parse_input(input_file):
    global maxweight
    fp = open(input_file, "r")
    i=0
    while True:
        lines = fp.readline()
        if lines == "":
            break
        if i == 0:
            weapons =int(lines.split(":")[1])
            # weapons_count = weapons[1]
        elif i == 1:
            maxweight = int(lines.split(":")[1])
        else:
            temp_array = lines.split("/")
            ammunition.append(temp_array[0])
            weight_per_pack.append(int(temp_array[1]))
            damage_per_pack.append(int(temp_array[2].split("\n")[0]))
        i = i+1 
def ammunition_greedy():
    global ammunition
    global damage_per_pack
    global weight_per_pack
    global maxweight 
    global damage 
    pw =[]
    proportion_taken =[0]*6
    dic_for_ammunition ={}
    parse_input("inputPS4.txt")
    for i in range(0, len(ammunition)):
        pw.append(damage_per_pack[i]/weight_per_pack[i])
    mergeSort(pw,ammunition,damage_per_pack,weight_per_pack,0 ,len(pw)-1)
    pw = pw[::-1]
    ammunition = ammunition[::-1]
    damage_per_pack  = damage_per_pack[::-1]
    weight_per_pack = weight_per_pack[::-1]
    for i in range(0,len(ammunition)):
        if maxweight>0 and weight_per_pack[i]<maxweight:
            maxweight = maxweight - weight_per_pack[i]
            damage = damage + damage_per_pack[i]
            proportion_taken[i] = 1
        elif maxweight > 0 :
            damage = damage + (maxweight/weight_per_pack[i])* damage_per_pack[i]
            proportion_taken[i] = (maxweight/weight_per_pack[i])
        else:
            break
    print(ammunition)
    print(proportion_taken)
    print("The total damge is ", damage)
    # print(pw)
    # print(ammunition)
    # print(damage_per_pack)
    # print(weight_per_pack)
ammunition_greedy()