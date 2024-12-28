#Unordered datatype

#you cannot define empty set using literals
emptySet=set()
sampleSet={1,'dayche',123,'abc',3.86}
for i in range(10):

    print(sampleSet)
print('='*40)
odd=set(range(1,50,2))
power={1,4,9,16,25,36,49}
print(len(odd))
print(odd.intersection(power))
print(odd.union(power))
