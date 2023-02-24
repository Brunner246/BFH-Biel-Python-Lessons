myList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

def print_elements(myList):
    for element in myList:
        print(element)

if __name__ == '__main__':
    for zahl in myList:
        if ist_gerade(zahl):
            print(zahl)


    # counter = 0
    # while counter < len(myList):
    #     if ist_gerade(myList[counter]):
    #         print(myList[counter])
    #         counter += 1
    #     else:
    #         counter += 1
