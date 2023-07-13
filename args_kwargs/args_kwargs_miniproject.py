tables = {
    'table_1' : {
        'customer_name' : '',
        'phone_number' : '',
        'order' : {
            'appetizer' : '',
            'main_meal' : '',
            'dessert' : ''
        },
        'total_price' : 0.0
    },
    'table_2' : {
        'customer_name' : '',
        'phone_number' : '',
        'order' : {
            'appetizer' : '',
            'main_meal' : '',
            'dessert' : ''
        },
        'total_price' : 0.0
    }, 
    'table_3' : {
        'customer_name' : '',
        'phone_number' : '',
        'order' : {
            'appetizer' : '',
            'main_meal' : '',
            'dessert' : ''
        },
        'total_price' : 0.0
    },
    'table_4' : {
        'customer_name' : '',
        'phone_number' : '',
        'order' : {
            'appetizer' : '',
            'main_meal' : '',
            'dessert' : ''
        },
        'total_price' : 0.0
    }
}

def table_control(table_number, *customer_information, **order_and_prices):
    if tables[table_number]['customer_name'] == '':
        tables[table_number]['customer_name'] = customer_information[0]
        tables[table_number]['phone_number'] = customer_information[1]
        tables[table_number]['order']['appetizer'] = order_and_prices['appetizer']
        tables[table_number]['order']['main_meal'] = order_and_prices['main_meal']
        tables[table_number]['order']['dessert'] = order_and_prices['dessert']
        tables[table_number]['total_price'] = order_and_prices['dessert_price'] + order_and_prices['appetizer_price'] + order_and_prices['main_meal_price']
    else:
        print('Table already occupied!')

table_control('table_1', 'Lucas Vilar', '12345678', appetizer='Green Salad', main_meal='Steak', dessert='Ice cream', appetizer_price = 11.80, main_meal_price=28.90, dessert_price=19.9)

for table_key, table_value in tables.items():
    print(f"{table_key} - {table_value}")

table_control('table_1', 'Julia Bruno', '12345678', appetizer='Green Salad', main_meal='Steak', dessert='Ice cream', appetizer_price = 11.80, main_meal_price=28.90, dessert_price=19.9)