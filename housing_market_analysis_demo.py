# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 19:32:46 2024

@author: mcall
"""
# The Mean Squared Error (MSE) is a measure used to evaluate the accuracy of a regression model by comparing the predicted values to the actual values. Here's what the MSE value of approximately 62,560,070.32 means:
#Interpretation of MSE:

#    Scale of the Error: The MSE value represents the average squared difference between the predicted values and the actual values in the units of the squared outcome variable (in this case, squared monetary units, if dealing with financial data).

#    Magnitude: A larger MSE indicates that the model's predictions are, on average, further away from the actual values compared to a smaller MSE.

#    Evaluation: While the absolute value of MSE might not directly indicate model performance, it is commonly used to compare different models. Lower MSE values generally indicate better model performance, but the interpretation depends on the specific context and scale of the data.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

def load_data():
    """
    Hardcoded data for demonstration.
    
    Returns:
    - pd.DataFrame: DataFrame containing hardcoded housing data.
    """
    data = {
        'Housing_Price': [300000, 320000, 340000, 310000, 330000, 350000, 370000, 360000, 380000, 400000],
        'GDP_Growth_Rate': [2.5, 2.8, 3.0, 2.7, 2.9, 3.1, 3.2, 3.0, 3.3, 3.5],
        'Interest_Rates': [4.5, 4.3, 4.0, 4.2, 4.1, 4.0, 3.8, 3.9, 3.7, 3.5],
        'Population_Growth': [1.2, 1.1, 1.3, 1.0, 1.2, 1.4, 1.5, 1.3, 1.6, 1.8],
        'Building_Permits': [100, 110, 120, 105, 115, 125, 130, 120, 135, 140],
        'Location_Urban_Suburban': [1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
        'Consumer_Confidence_Index': [85, 88, 90, 87, 89, 92, 93, 91, 94, 95],
        'Green_Building_Adoption': [0.2, 0.3, 0.4, 0.3, 0.5, 0.6, 0.7, 0.5, 0.8, 0.9],
        'Tax_Policies': [1, 1, 2, 1, 2, 2, 3, 2, 3, 3]
    }
    
    return pd.DataFrame(data)

def preprocess_data(data):
    """
    Preprocess hardcoded housing data for modeling.
    
    Parameters:
    - data (pd.DataFrame): DataFrame containing hardcoded housing data.
    
    Returns:
    - pd.DataFrame: Processed DataFrame with selected features and target variable.
    """
    # Select relevant features (adjust based on your dataset)
    selected_features = [
        'GDP_Growth_Rate', 'Interest_Rates', 'Population_Growth', 
        'Building_Permits', 'Location_Urban_Suburban', 'Consumer_Confidence_Index', 
        'Green_Building_Adoption', 'Tax_Policies'
    ]
    
    # Separate features (X) and target variable (y)
    X = data[selected_features]
    y = data['Housing_Price']
    
    return X, y

def train_model(X_train, y_train):
    """
    Train a Linear Regression model.
    
    Parameters:
    - X_train (pd.DataFrame): Features for training.
    - y_train (pd.Series): Target variable for training.
    
    Returns:
    - LinearRegression: Trained Linear Regression model.
    """
    # Initialize the Linear Regression model
    model = LinearRegression()
    
    # Train the model on the training data
    model.fit(X_train, y_train)
    
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluate the trained model on test data.
    
    Parameters:
    - model (LinearRegression): Trained Linear Regression model.
    - X_test (pd.DataFrame): Features for testing.
    - y_test (pd.Series): Target variable for testing.
    """
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Calculate Mean Squared Error (MSE) as a measure of model performance
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error (MSE): {mse}")

def main():
    # Step 1: Load Data (Hardcoded for demo)
    try:
        data = load_data()
    except Exception as e:
        print(f"Error loading data: {e}")
        return
    
    print("Data loaded successfully.")
    
    # Step 2: Preprocess Data
    try:
        X, y = preprocess_data(data)
    except Exception as e:
        print(f"Error preprocessing data: {e}")
        return
    
    print("Data preprocessed successfully.")
    
    # Step 3: Split Data into Training and Testing Sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Step 4: Train the Model
    try:
        model = train_model(X_train, y_train)
    except Exception as e:
        print(f"Error training model: {e}")
        return
    
    print("Model trained successfully.")
    
    # Step 5: Evaluate the Model
    try:
        evaluate_model(model, X_test, y_test)
    except Exception as e:
        print(f"Error evaluating model: {e}")
        return

if __name__ == "__main__":
    main()
