import requests
import redis

url = 'https://catfact.ninja/breeds'
num_records = 20

"""Make a GET request to the URL"""
response = requests.get(url)

"""heck if the request was successful"""
if response.status_code == 200:
    data = response.json()

    """Extracting the 'data' key and then take 20 records (or less if there are fewer available)"""
    records = data.get('data', [])[:num_records]

    """Connecting to Redis cloud"""


    r = redis.Redis(
        host='redis-12901.c326.us-east-1-3.ec2.cloud.redislabs.com',
        port=12901,
        password='YBQHNZO0OTYhEW1W1Cu37EGalDgymWRS')

    """Insert records into Redis"""
    for index, record in enumerate(records, start=1):
        """Use a key like 'cat_breed_1', 'cat_breed_2', etc."""
        key = f'cat_breed_{index}'

        """Set the value in Redis"""
        r.set(key, str(record))
        print(f"Inserted record {index} into Redis with key {key}")

else:
    print(f"Error: Unable to fetch data. Status code: {response.status_code}")
