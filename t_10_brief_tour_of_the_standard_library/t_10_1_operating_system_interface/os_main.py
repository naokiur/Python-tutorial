import os
print(os.getcwd())
first_dir = os.getcwd()

os.chdir('../')
print(os.getcwd())

os.chdir(first_dir)
print(os.getcwd())

dir_name = "today"
os.system('mkdir ' + dir_name)
os.chdir(dir_name)
print(os.getcwd())

os.chdir(first_dir)
os.rmdir(dir_name)

dir(os)
help(os)
