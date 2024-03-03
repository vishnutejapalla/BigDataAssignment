import requests

url = 'https://catfact.ninja/breeds'
num_records = 20
search_key = 'breed'  # Key to search for
search_value = 'Aegean'  # Value to search for

"""Make a GET request to the URL"""
response = requests.get(url)

"""Check if the request was successful (status code 200)"""
if response.status_code == 200:
    """Parse the JSON response"""
    data = response.json()

    """Extract the 'data' key and then take 20 records (or less if there are fewer available)"""
    records = data.get('data', [])[:num_records]

    """Search for the record with the specified key-value pair"""
    found_record = None
    for record in records:
        if record.get(search_key) == search_value:
            found_record = record
            break

    # If a record is found, print it
    if found_record:
        print("Record Found:")
        print(found_record)
    else:
        print(f"No record found with '{search_key}' equal to '{search_value}'.")

else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")