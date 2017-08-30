
search_string=input("Please Enter the search string: ")

with open("search_file.txt") as f:
    for index,line in enumerate(f):
        if search_string in line:
             print (str(index+1)+" "+line)