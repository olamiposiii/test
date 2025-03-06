import pandas as pd

#Pandas series
lst=[1,2,3,4,5,6]
series=pd.Series(lst)
print(series)
print(type(series))

#how to create an empty series
empty=pd.Series([])
print(empty)

#defining the x and y series
a=pd.Series(['p','q','r','s','t'], index=[10,11,12,13,14])
print(a)

b=pd.Series(['p','q','r','s','t'], index=[10,11,12,13,14], name='alphabets')
print (b)

#pandas series with python dictionary
dict_series=pd.Series({'p':1, 'q':2, 'r':3, 's':4, 't':5})
print(dict_series)

print(dict_series[0:3])

print(max(dict_series))

dict_series=pd.Series({'p':[1,5,6], 'q':[2,6,7], 'r':[3,9,0], 's':[4,4,5], 't':[5,1,2]})
print(dict_series)


#pandas dataframe and reading csv files
df= pd.DataFrame()
print(df)

#Dataframe using list
lst=[1,2,3,4,5]
df=pd.DataFrame(lst)
print(df)

lst=[[1,2,3,4,5],[11,12,13,14,15]]
df=pd.DataFrame(lst)
print(df)

#using distionaire
a=[ {'a':5, 'b':7, 'c':9, 'd':2},{'a':4, 'b':8, 'c':19, 'd':12} ]
df=pd.DataFrame(a)
print(df)

b= { 'RollNo':pd.Series([1,2,3,4,5]), 'Maths': pd.Series([67,89,23,90,56]), 'Physics': pd.Series([12,98,44,90,78])}
df= pd.DataFrame(b)
print(df)

#Reading CSV (common separated values) as DataFrame



