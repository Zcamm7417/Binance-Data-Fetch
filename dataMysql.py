import json
import mysql.connector
import time

if response.status_code == 200:
    data = response.json()
    current_price = data['price']

    # Load data from the JSON file
    with open('btc_price.json', 'r') as json_file:
        existing_data = json.load(json_file)

    # Append new data to the existing data
    existing_data.append({'timestamp': int(time.strftime("%H:%M")), 'price': current_price})

    # Create a MySQL connection
    connection = mysql.connector.connect(
        host='127.0.0.1:3306',
        user='root',
        password='Rajimrak741777',
        database='data_pipeline'
    )

    cursor = connection.cursor()

    # Define your SQL query to insert data into a table
    insert_query = "INSERT INTO btc-price (btc-price, time) VALUES (%s, %s)"

    # Insert the new data into the MySQL table
    for entry in existing_data:
        cursor.execute(insert_query, (entry['btc-price'], entry['time']))

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and the connection
    cursor.close()
    connection.close()

    # Save the updated data to the JSON file
    with open('btc_price.json', 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)

    print("Data inserted into MySQL and updated in JSON file")

