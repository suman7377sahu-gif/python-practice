# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the different
# files. Place these files in a folder for a 13-year-old.

for i in range (2,21):
    filename = f"Chapter 9/table/{i}.txt"

    with open(filename,"w") as f :
        
        for j in range (1,11):
            f.write(f"{i} X {j} = {i*j}")


print("All multiplication table created successfull." )
            