import json
import random

# Number of JSON objects to generate
num_objects = 600  # You can change this to the desired number

# List to store the generated JSON objects
json_objects = []
word_options = ["Good", "Bad"]

# Loop to generate JSON objects
for i in range(num_objects):
    data = {
        "resource": f"LT-{i+1}",  # Example: LT-1, LT-2, ...
        "value": round(random.uniform(20.0, 90.0),3),
        "quality": random.choice(word_options)
    }
    json_objects.append(data)

# Convert the list of dictionaries to a JSON array
json_data = json.dumps(json_objects, indent=2)

# Print or save the generated JSON
print(json_data)

# If you want to save it to a file, you can use the following:
with open('output.json', 'w') as json_file:
    json_file.write(json_data)
