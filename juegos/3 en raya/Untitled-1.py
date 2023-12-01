# 1. Pintar tablero

'''
| 0 | 1 | 2 |
| 3 | 4 | 5 |
| 6 | 7 | 8 |

tablero = [0,1,2,3,4]

| X |  |  |
| O |  |  |
|   | X |  |
            0   1   2   3   4   5   6   7   8
tablero = ["X"," "," ","O"," "," "," ","X"," "]

tablero[3] == "O"

tablero[7] = "X"

'''
    #       0   1   2   3   4   5   6   7   8
tablero = [" "," "," "," "," "," "," "," "," "]

print("|",tablero[0],"|")