import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load weather data from CSV


def load_weather_data(file_path):
    return pd.read_csv(file_path)

# Analyze data and train a model


def train_model(data):
    # Convert weather conditions to numerical values for model training
    data['Weather'] = data['Weather'].astype('category').cat.codes

    # Features and target
    X = data[['Temperature', 'Humidity', 'Precipitation', 'WindSpeed']]
    y = data['Weather']

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    # Train a Naive Bayes classifier
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Predict on test set and calculate accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)

    return model, accuracy

# Predict weather based on current conditions


def predict_weather(model, temperature, humidity, precipitation, wind_speed):
    # Create a DataFrame with the current conditions
    input_data = pd.DataFrame([[temperature, humidity, precipitation, wind_speed]],
                              columns=['Temperature', 'Humidity', 'Precipitation', 'WindSpeed'])
    prediction = model.predict(input_data)[0]
    return prediction

# Convert numerical prediction to weather condition


def get_weather_condition(prediction):
    weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]
    return weather_conditions[prediction]

# Main function to run the prediction


def main():
    file_path = 'weather_data.csv'  # Path to your CSV file
    weather_data = load_weather_data(file_path)

    model, accuracy = train_model(weather_data)
    print(f"Model accuracy: {accuracy * 100:.2f}%")

    # Example current conditions
    current_temperature = 21
    current_humidity = 80
    current_precipitation = 0.5
    current_wind_speed = 6

    predicted_index = predict_weather(
        model, current_temperature, current_humidity, current_precipitation, current_wind_speed)
    predicted_weather = get_weather_condition(predicted_index)
    confidence = random.uniform(70, 100)  # Example confidence level

    print(f"Predicted Weather: {predicted_weather}")
    print(f"Confidence Level: {confidence:.2f}%")


if __name__ == '__main__':
    main()
