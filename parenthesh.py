def matchedparenthesis(s):
try:
list=[]
for i in s:
if i =="(":
list.append(i)
elif i ==")":
list.remove("(")
if list == []
return (TRUE)
else:
return(FALSE)
except ValueError :
return ("FALSE")


string=input("ENTER YOUR TEXT(ONLY PARENTHESES WILL BE COUNTED):")
print(matchedparenthesis(string))