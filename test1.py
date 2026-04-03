import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib
matplotlib.use('Agg')  # Essential for Docker: prevents graphical interface errors
import matplotlib.pyplot as plt
import logging

# Configure logging to display information
logging.basicConfig(level=logging.INFO)

# Create a DataFrame with study hours and corresponding scores
data = {'Hours_Studied': [1, 2, 3, 4, 5], 'Scores': [50, 60, 70, 80, 90]}
df = pd.DataFrame(data)

# Define features and target variable
X = df[['Hours_Studied']]
y = df['Scores']

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Plot the actual scores and the predicted scores
plt.scatter(X, y, color='blue', label='Actual Scores')
plt.plot(X, model.predict(X), color='red', label='Predicted Scores')
plt.title('Hours Studied vs Scores')
plt.xlabel('Hours Studied')
plt.ylabel('Scores')
plt.legend()

# Save the plot as an image file
plt.savefig('output.png')
logging.info("--- [SUCCESS] The graph has been generated in output.png ---")
# plt.show()  # REMOVED: Blocks execution in the container
