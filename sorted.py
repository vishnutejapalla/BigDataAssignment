import requests

url = 'https://catfact.ninja/breeds'
num_records = 20

"""Make a GET request to the URL"""
response = requests.get(url)

"""Check if the request was successful (status code 200)"""
if response.status_code == 200:
    """Parse the JSON response"""
    data = response.json()

    """Extract the 'data' key and then take 20 records (or less if there are fewer available)"""
    records = data.get('data', [])[:num_records]

    """Sort the records alphabetically based on the 'name' key"""
    sorted_records = sorted(records, key=lambda x: x.get('name', '').lower())

    """Print the sorted records"""
    for record in sorted_records:
        print(record)

else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
