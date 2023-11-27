def cross(n):
    for i in range(n):
        row = " " * (2 * i - 1) + "#" + " " * (2 * (n - i - 1))
        mirrored_row = row[::-1]  # Reverse the row
        print(row + mirrored_row)

    for i in range(n - 2, -1, -1):
        row = " " * (2 * i - 1) + "#" + " " * (2 * (n - i - 1))
        mirrored_row = row[::-1]  # Reverse the row
        print(row + mirrored_row)

# Example usage to draw a symmetric cross pattern with arms of length 5
cross(5)

## A bit dfucked run and see
#                #
 #            #
   #        #
     #    #
       ##
     #    #
   #        #
 #            #
#                #