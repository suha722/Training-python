import pandas as pd
data=pd.read_csv('reviews.csv')
data["avarage_rating"]=data.groupby('product_id')['rating'].mean()
# print(data)
selecting=data[data['rating']>3]
select_product = selecting['rating']
data['percent']=(select_product/select_product.sum())*100
# print(data['percent'])
print(data.groupby('product_id')['percent'])
print("Average ratings by product:\n",data['avarage_rating'])
print("Top 10 products by average rating:\n",data['avarage_rating'].nlargest(n=10))
print("Percentage of positive reviews by product:\n",data['percent'])
print("Top 10 products by percentage of positive reviews:\n",data['percent'].nlargest(n=10))

# # print(data[data['rating']>3])
# positive=data.query('rating>4').groupby('product_id')['rating'].count()
# allpos=data.query('rating>4').groupby('product_id')['percent']
# print(allpos)
# # poss=(positive['rating']/allpos['rating'])*100
# # print(poss)