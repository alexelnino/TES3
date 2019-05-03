def balikPosisi(x):
    lenX=len(x)
    list=[]
    for i in range(lenX):
	    list.append(x[lenX-1-i])
    return list

print(balikPosisi([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(balikPosisi(['A', 'B', 'C', 'D', 'E', 'F', 'G']))
print(balikPosisi(['Messi', 'Suarez', 'Coutinho', 'Dembele', 'Rakitic']))