import pandas as pd
df=pd.read_csv('employee.csv')
count=0
avarege=df['salary'].mean()
maxsalary=df['salary'].max()
print("The average salary for the company is:",avarege)
print("The highest salary at the company is: ",maxsalary)
maxx=df.loc[df['salary'].idxmax()]
print("The employee with the highest salary is:\n",maxx)
for c in df.values[df['salary']<avarege]:
    count+=1
print("The number of employees who make less than the average salary is:",count)
print(df.groupby('department')['salary'].agg(("min","max")))
employee_new = df.groupby('department',as_index=False).apply(lambda x:x.sort_values('first_name'))\
    .reset_index(drop=True)
print(employee_new)