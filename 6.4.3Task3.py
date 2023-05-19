import pandas as pd
df1=pd.read_csv('book.csv')
df2=pd.read_csv('sale.csv')
data=df1.groupby('publisher')['price'].sum()
newdata=df2[df2['sale_date']>'2021-30-12']
book_merge=df1.merge(newdata,on ="book_id")
data=book_merge.groupby('publisher')['price'].sum()
print(data)
# data.to_csv("puplisher")
data.to_csv('out.csv', index=True )
# print(data.sort_value())

