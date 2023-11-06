def alergy_list(a, b):
    for i in range(a,b):
        i_arr = str(i).slice() 
        if i_arr[len(i_arr)] != 5:
            print(i, end=" ")

alergy_list(3, 27)
alergy_list(1, 7)