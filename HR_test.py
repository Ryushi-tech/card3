lis = [input() for _ in range(2)]
for i in lis:
    if i[0]=="4" or i[0]=="5" or i[0]=="6" and i[4]=="-" and i[9]=="-" and i[14]=="-":
            i2 = i[:4]+i[5:9]+i[10:14]+i[15:]
            state = 0
            for j in range(len(i2)-3):
                if i2[j]==i2[j+1]==i2[j+2]==i2[j+3]:
                    print("Invalid")
                    state = 1
                    break
                else:
                    j += 1
            if state == 0:
                print("Valid")
    else:
        print("Invalid b")