# kirana store bill generator
i=1
sum = 0
with open("kirana.txt","w") as f:
    f.write(" ")
    f.writelines("ABC Kirana Store")
while(True):
    item = input(f"Enter the price of the item {i}: ")
    if(item != 'q'):
        sum+=int(item)
        print(f"The sum of items as of now is : {sum}")
        with open("kirana.txt","a") as f:
            f.writelines(f"\nThe price of item {i} is {item}")
            i+=1
            
    else:
        with open("kirana.txt","a") as f:
            f.writelines(f"\nThe total sum of all the items is : {sum}")
            f.writelines("\nThank you for shopping with us have a good day ! \nPlease Visit us Again")
            break
    
        



    
