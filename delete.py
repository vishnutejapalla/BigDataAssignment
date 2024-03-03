import redis

"""Connect to Redis"""
r = redis.Redis(
    host='redis-12901.c326.us-east-1-3.ec2.cloud.redislabs.com',
    port=12901,
    password='YBQHNZO0OTYhEW1W1Cu37EGalDgymWRS')

def delete_record(key):
    """Decode the key from bytes to string"""
    key_str = key.decode('utf-8')

    """Check if the key exists before deleting"""
    if r.exists(key):
        r.delete(key)
        print(f"Record with key '{key_str}' deleted successfully.")
    else:
        print(f"No record found with key '{key_str}'.")

"""Example usage: Delete a record with a specific key"""
delete_record(b'cat_breed_18')
