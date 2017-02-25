aList=[int(x) for x in input().split()];
aList.sort();
aList=aList[2:len(aList)-2]
mean=sum(aList)/len(aList)

for i in range(len(aList)):
aList[i] = (aList[i]-mean)**2;
variance=sum(aList)/len(aList);
sd=variance**0.5;
print("Η τυπική απόκλιση (χωρίς τους δύο μικρότερους και τους δύο μεγαλύτερους) είναι:" + str(sd));