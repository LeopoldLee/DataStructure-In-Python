a = [26, 5, 37, 1, 61, 11, 59, 15, 48, 19]
left = 0
right = len(a)-1
def quicksort(lef, rig):
    if lef==right:
        print(a, "left :",lef+1,"right :",rig+1)
        print(a)
    elif lef<rig:
        print(a, "left :",lef+1,"right :",rig+1)
        i = lef
        j = rig+1
        piv = a[lef]
        while True:
            while True:
                i += 1
                if a[i]>=piv:
                    break
            while True:
                j -= 1
                if a[j]<=piv:
                    break
            if i<j:
                tmp = a[i]
                a[i] = a[j]
                a[j] = tmp
            if i>=j:
                break
        tmp = a[lef]
        a[lef] = a[j]
        a[j] = tmp
        quicksort(lef, j-1)
        quicksort(j+1, rig)
quicksort(left, right)
