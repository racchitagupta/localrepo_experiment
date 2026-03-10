## List named products
products = ['apple','pepsi','santro','plate','brinjal','notebook']

## Tuple
sample_product = ('Banana',60,'fruits')

# 2nd and last item from the list - print
print("2nd item from the list : ",products[1])
print("Last item from the list : ",products[-1])

# append 2 new products to 'products', then print 'products'
products.append('pen')
products.append('cups')
print("printing 'products' list : ", products)

#Extra
print("Tuple :",sample_product)
convert_sample=list(sample_product)
convert_sample[1]=40
sample_product=tuple(convert_sample)
print("Tuple post changes :",sample_product)

####### Task 2 #########

# Create a new list
categories = ['fruit','vegetable','toy car','utensil','stationary','beverage']

# Convert list to set
convert_categories=set(categories)
print("Set : ",convert_categories)

# Add new category to set
convert_categories.add("stationary")
print("Set post add() : ",convert_categories)

# Check if category exist in a set
print("To check if Electronics is present in a set : ","Electronics" in convert_categories)
print("To check if fruit is present in a set : ","fruit" in convert_categories)

# Print length of the set
print("Length of the set : " , len(convert_categories))

####### Task 3 #########

# Create dict
price_dict = {'apple':30,'pepsi':20,'santro':51,'plate':20.5,
              'brinjal':40,'notebook':67.8}
print(price_dict)

# Add new product to dict
price_dict['scrub'] = 45
print('After updating dictionary : ',price_dict)

#Update price of existing product
price_dict['apple']=34.5
print('updating value of a key in dict : ',price_dict)

#Remove item that does not exist in dict
price_dict.pop('coke',None)
print('After deleting coke from dictionary : ',price_dict)

#Find Average of prices in dict
total=sum(price_dict.values())
count=len(price_dict)
print(f'Average of prices in the dict is {round((total/count),3)}')

#Find min and max price and its corresponding key - Extra(optional)
print(f'Max price and product in dict is {max(price_dict.values())} and {max(price_dict, key=price_dict.get)}')
print(f'Min price and product in dict is {min(price_dict.values())} and {min(price_dict, key=price_dict.get)}')


####### Task 4 #########

#products = ['apple', 'pepsi', 'santro', 'plate', 'brinjal', 'notebook', 
#            'pen', 'cups']
# price_dict = {'apple': 34.5, 'pepsi': 20, 'santro': 51, 'plate': 20.5, 
#               'brinjal': 40, 'notebook': 67.8, 'scrub': 45}
#convert_categories = {'toy car', 'beverage', 'stationary', 
#                      'vegetable', 'fruit', 'utensil'}

categories = ['fruit', 'beverage', 'toy car', 'utensil', 
              'vegetable', 'stationery', 'cleaning']
catalog = list(zip(price_dict.keys(),price_dict.values(),categories))
print(catalog)
category_to_products = {}