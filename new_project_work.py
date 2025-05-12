
import pandas as pd

# Load the CSV file
data = pd.read_csv("D:\\survey.csv")

# Display the first few rows
print("Survey Data Preview:")
print(data.head())

# Extract columns into separate lists
user_ids = data['User_ID'].tolist()
ages = data['Age'].tolist()
genders = data['Gender'].tolist()
platforms = data['Platform'].tolist()
usage_times = data['Daily Usage Time (in hours)'].tolist()
posts_per_day = data['Posts Per Day'].tolist()
likes_per_day = data['Likes Received Per Day'].tolist()
comments_per_day = data['Comments Received Per Day'].tolist()
messages_per_day = data['Messages Sent Per Day'].tolist()
emotions = data['Dominant Emotion'].tolist()

# Basic statistics
print("\nBasic Statistics:")
print(f"Total Respondents: {len(user_ids)}")
print(f"Average Daily Usage Time: {sum(usage_times)/len(usage_times):.2f} hours")

# Gender distribution
print("\nGender Distribution:")
print(data['Gender'].value_counts())

# Most popular platform
print("\nMost Popular Platform:")
print(data['Platform'].value_counts().idxmax())

# Most common dominant emotion
print("\nMost Common Dominant Emotion:")
print(data['Dominant Emotion'].mode()[0])
