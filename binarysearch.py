
def binary_search(array, number):
    lower = 0
    upper = len(array)
    while lower < upper:
        middle = lower + (upper - lower) // 2
        
        val = array[middle]
        if number == val:
            return middle
        elif number > val:
            if lower == middle:
                break       
            lower = middle
        elif number < val:
            upper = middle


def sort_array(array):
    swapped = True
    while (swapped):
        swapped = False
        for i in range(len(array)-1):
            if(array[i] > array[i+1] ):
                array[i] , array[i+1] = array[i+1], array[i]
                swapped = True

    return array


def main():
    size = input("Enter the Size of the array: ")
    arr = []
    for i in range(size):
        value = input(str(i+1) + ": ")
        arr.append(value)
    arr = sort_array(arr)
    #arr.sort()
    print(arr)
    number = input("Enter a number you want to find: ")
    print("Number Found at " + str(binary_search(arr, number)) + " index")
if __name__ == '__main__':
    main()