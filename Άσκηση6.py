import calendar
calendar.setfirstweekday(calendar.SUNDAY)
xronia=int(input())
mhnas=int(input())
i=1
a=""
if mhnas==1:
	a="January"
if mhnas==2:
	a="February"
if mhnas==3:
	a="March"
if mhnas==4:
	a="April"
if mhnas==5:
	a="May"
if mhnas==6:
	a="June"
if mhnas==7:
	a="July"
if mhnas==8:
	a="August"
if mhnas==9:
	a="September"
if mhnas==10:
	a="October"
if mhnas==11:
	a="November"
if mhnas==12:
	a="December"
print(a,xronia)
print('S''\t','M''\t','T''\t','W''\t','T''\t','F''\t','S''\t')
for x in calendar.Calendar(firstweekday=6).itermonthdays(xronia,mhnas):
	calendar.setfirstweekday(calendar.SUNDAY)
	if x==0 or x=="":
		print('--','\t',end='')
	else:
		print("%02d"%x,'\t',end='')
	i+=1
	if i==8:
		print("")
		i=1