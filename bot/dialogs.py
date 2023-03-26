import pymongo
import requests
import config

# Connect to MongoDB
client = pymongo.MongoClient(config.mongodb_uri)
print(client)
db = client["chatgpt_telegram_bot"]

user_collection = db["user"]
dialog_collection = db["dialog"]

# Define the query
query = {
  'user_id': { '$ne': 132433743 },
  'start_time': { '$gte': '2023-03-23T00:00:00.000Z' }
}

# Execute the query and get the results
results = list(dialog_collection.find(query))

print(results)

# Define the webhook URL
url = 'https://hook.eu1.make.com/7ysg5cqwzf1n9j4280km32lntocz3ioo'

# Send the data to the webhook
response = requests.post(url, json=results)

if response.status_code == 200:
    print('Data sent successfully!')
else:
    print('Error sending data:', response.status_code)
