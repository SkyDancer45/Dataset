import pandas as pd

# Read the CSV data into a DataFrame
df = pd.read_csv('D:\Projects\AI1\Dataset\data.csv')
df2 = pd.read_csv("D:\Projects\AI1\Dataset\pants.csv")
df3 = pd.read_csv("D:\Projects\AI1\Dataset\jackets.csv")
df4 = pd.read_csv("D:\Projects\AI1\Dataset\shoes.csv")

# Convert the DataFrame to a list of dictionaries (object arrays)
object_arrays = df.to_dict(orient='records')
object_arrays2 = df2.to_dict(orient='records')
object_arrays3 = df3.to_dict(orient='records')
object_arrays4 = df4.to_dict(orient='records')

# Now, 'object_arrays' is a list where each element is a dictionary representing a row in the dataset
# You can access individual items like object_arrays[0]['Column1']

# Example: Printing the first few rows of the dataset
print(object_arrays[145])
print(object_arrays2[145])
print(object_arrays3[145])
print(object_arrays4[145])