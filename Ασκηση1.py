import re
string=input("enter:")
string = re.sub('\!(?!$)', '', string)
print(string)