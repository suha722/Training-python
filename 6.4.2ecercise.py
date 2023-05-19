# Data Frame
"""
Description: Load a CSV file into a DataFrame, handle missing values, and remove duplicates.

Example Run: Load a CSV file containing information about cars and perform data cleaning operations on it

"""
'''import pandas as pd
df=pd.read_csv('data.csv')
missing_value=df.dropna(inplace=True)
duplicated_df=df.drop_duplicates(inplace=True)
print(df)
# print(duplicated_df,"\n",missing_value)
# for value in df.values:
#     print(value)

'''
"""
Exercise 2: Data Aggregation

Description: Load a CSV file into a DataFrame, group the data by a certain column, and compute aggregate
 statistics. Example Run: Load a CSV file containing information about movies and 
compute the average rating for each genre.
"""
'''import pandas as pd
df=pd.read_csv("data1.csv")
newdata=df.groupby('genre')['rating'].mean()

print(newdata)

'''


"""
Exercise 3: Data Visualization

Description: Load a CSV file into a DataFrame and create a scatter plot using Matplotlib.
 Example Run: Load a CSV file containing information about
 cars and create a scatter plot of horsepower vs. weight.

"""
'''import pandas as pd

df=pd.read_csv('data.csv')
# df.plot('model')
df.plot.scatter(x="horsepower",y='weight')
'''
"""
Exercise 4: Data Reshaping

Description: Load a CSV file into a DataFrame and reshape it from wide to long format using pandas melt function.
 Example Run: Load a CSV file containing information 
about stocks and reshape the data from wide to long format.
"""
# import pandas as pd
#
# df=pd.read_csv('data.csv')


"""
Exercise 5: Data Manipulation

Description: Load two CSV files into DataFrames and perform an inner join on a common column. 
Example Run: Load two CSV files containing information about 
sales and products and perform an inner join on the product ID
"""
# import pandas as pd
# product=pd.read_csv('product.csv')
# sales=pd.read_csv('sales.csv')
# output1 = pd.merge(product, sales,
#                    on='product_id',
#                    how='inner')
# print(output1)

"""
Exercise 6:Data Merging

Description: You have two datasets of customer orders and items. You want to merge them into a 
single dataset that includes the customer name, email, item name, and item price for each order.

"""
import pandas as pd
customer=pd.read_csv('customer.csv')
order=pd.read_csv('order.csv')
items=pd.read_csv('items.csv')
# print(order['order_id'])
# newcustomer=customer._append(order['order_id'])
# print(newcustomer)
# print(customer)
# result=pd.merge(customer,order,on='order_id',how='inner')
# result=pd.merge(customer,items,on='item_name''price',how='inner')
# print(result)

#
# customer['order_id']=order['order_id']
# customer['item_name']=items['item_name']
# customer['price']=items['price']
# print(customer)

"""
Exercise 7: Data Joining

Description: You have two datasets, one with customer information and another with purchase information.
 You want to join the two datasets based on the customer ID 
to create a single dataset with both types of information.
"""
# import pandas as pd
# df=pd.read_csv('customers.csv')
# df2=pd.read_csv('purchases.csv')
# result=pd.merge(df2,df,on='customer_id',how='outer')
# print(result)
import pandas as pd
df=pd.read_csv('orders.csv')
