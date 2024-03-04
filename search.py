import json
import redis
import requests

"""Connect to Redis"""
redis_host = 'redis-12901.c326.us-east-1-3.ec2.cloud.redislabs.com'
redis_port = 12901
redis_password = 'YBQHNZO0OTYhEW1W1Cu37EGalDgymWRS'
redis_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password)

"""Redis key to store the data"""
redis_key = 'cat_data'

"""Check if the data is already in Redis, if not, fetch from the API and store in Redis"""
if not redis_client.exists(redis_key):
    url = 'https://catfact.ninja/breeds'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Store the data in Redis with a 1-hour expiration time (you can adjust as needed)
        redis_client.setex(redis_key, 3600, json.dumps(data))
    else:
        print(f"Error: Unable to fetch data from the API. Status code: {response.status_code}")
        exit()

"""Fetch data from Redis"""
data_from_redis = redis_client.get(redis_key)
data = json.loads(data_from_redis)

num_records = 20
search_key = 'breed'
search_value = 'Aegean'

"""Extract the 'data' key and then take 20 records (or less if there are fewer available)"""
records = data.get('data', [])[:num_records]

"""Search for the record with the specified key-value pair"""
found_record = next((record for record in records if record.get(search_key) == search_value), None)

"""If a record is found, print it"""
if found_record:
    print("Record Found:")
    print(found_record)
else:
    print(f"No record found with '{search_key}' equal to '{search_value}'.")
