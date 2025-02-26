num= int(input("write the number of raws you want"))
the_range= int(input("enter your range"))

for line_no in range(1, num+1):
    for inner_line in range(1, line_no+1):
     
        print(inner_line, end="")
    print()


print("end of script")    

star= int(input("write the number of raws you want"))
the_range= input("enter your pattern")

for line_no in range(1, star +1):
    for inner_line in range(1, line_no+1):
     
        print(the_range, end="")
    print()


print("end of script") 