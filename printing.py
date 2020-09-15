str="ASHIL"
print_A=[[" " for i in range(4)] for j in range(4)]
print_S=[[" " for i in range(4)] for j in range(4)]
print_H=[[" " for i in range(4)] for j in range(4)]
print_I=[[" " for i in range(4)] for j in range(4)]
print_L=[[" " for i in range(4)] for j in range(4)]

for row in range(4):
    for col in range(4):
        if((row==0 or row==2 or row==4) and (col>0 and col<4)) or ((row==1 or row==4) and col==8) or ((row==8 or row==3) and col==4):
            print_A[row][col]="*"

    for row in range(4):
        for col in range(4):
            if ((row==0 or row==2) and (col>0 and col<4)) or (col==4 and (row!=0 and row!=2)):
                print_S[row][col]="*"

    for row in range(4):
        for col in range(4):
            if ((col==0 or col==4) and (row!=4)) or (row==4 and (col>0 and col<4)):
                print_H[row][col]="*"

    for row in range(4):
        for col in range(4):
            if row==0 or (col==2 and row!=0):
                print_I[row][col]="*"

    for row in range(4):
        for col in range(4):
            if (col==0 or col==4) or (row==2 and (col>0 and col<4)):
                print_L[row][col]="*"

    for i in range(4):
        for j in range(4):
            print(print_A[i][j],end="")
        print(end=" ")
        for j in range(4):
            print(print_S[i][j],end="")
        print(end=" ")
        for j in range(4):
            print(print_H[i][j],end="")
        print(end=" ")
        for j in range(4):
            print(print_I[i][j],end="")
        print(end=" ")
        for j in range(4):
            print(print_L[i][j],end="")
        print()

