import os
os.chdir(os.getcwd()+'/book')
a=str(os.listdir("../book"))

file= open("book_list.txt","w")
file.write(a)
file.close()


