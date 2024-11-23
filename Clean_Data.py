import ijson

file_path = r"D:\Research Papers Dataset\dblp-citation-network-v14.json"

# Open the large JSON file
with open(file_path, "r") as file:
    # Parse the JSON incrementally
    objects = ijson.items(file, "item")  # Parse all objects in the file
    first_1000 = [obj for _, obj in zip(range(1000), objects)]

# Print the first 1000 objects
print(first_1000)
