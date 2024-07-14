import random
temperatures= []
for i in range(7):
	temperatures.append(random.randint(26,40))
weekdays=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"]	
count=0
for i in range(7):
	temperatures[i]
	evendays=weekdays[i]
	if temperatures[i] %2 ==0:
		count+=1 
		print(evendays)
		
for x in range(7):
	print(weekdays[x],":",temperatures[x])



high_tem = 0 
for j in range(7):
	if temperatures[j] > high_tem:
		high_tem = temperatures[j]
		day=weekdays[j]
print("the hottest temperatures was" , high_tem ," on" ,day)


low_tem = temperatures[0]	
for l in range(7):
	if temperatures[l]<low_tem:
		low_tem=temperatures[l]
		day2=weekdays[j]
print("the lowest was" , low_tem, "on" ,day2)		

sum = 0		
for k in range(7):
	sum =sum +temperatures[k]
avg = sum/7
print("the average temperatureswas " , avg)


above_avg=[]
for g in range(7):
	if temperatures[g]>avg :
		above_avg.append(temperatures[g])
		w = weekdays[g]


print("the days with above average temperatures were:" , w)






