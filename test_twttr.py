import twttr

name = input("Name: ")
s = twttr.shorten(name)
print("Test Result:",s)