import streamlit as st
import pandas as pd
import joblib

@st.cache_resource
def load_assets():
    """
    Loads the saved machine learning model and scaler from disk.
    This function is cached to ensure it's only run once per session.
    """
   
    scaler = joblib.load('scaler.joblib')
    model = joblib.load('final_model.joblib')

    return scaler, model

scaler, model = load_assets()

st.title('🏡 California Real Estate Price Predictor')

# st.sidebar.header() places a header in the sidebar panel on the left.
# This is the ideal place to organize all the user input widgets.
st.sidebar.header('User Input Features')

def user_input_features():
    """
    Creates sidebar widgets to get input from the user.
    Returns a dictionary of the user's selected feature values.
    """
    # For each feature, we create a widget. The value from the widget is stored in a variable.
    # We use st.sidebar to place these widgets in the sidebar.

    # Arguments: label, min_value, max_value, default_value
    house_age = st.sidebar.slider('House Age (years)', 1, 52, 25)

    # Arguments: label, min_value, max_value, default_value, step
    med_inc = st.sidebar.number_input('Median Income (in tens of thousands of $)', 1.0, 15.0, 3.5, 0.1)
    
    # We create widgets for all 8 base features the model needs.
    avg_rooms = st.sidebar.number_input('Average Number of Rooms', 2.0, 10.0, 5.0, 0.5)
    avg_bedrms = st.sidebar.number_input('Average Number of Bedrooms', 1.0, 5.0, 1.0, 0.5)
    population = st.sidebar.number_input('Block Population', 500, 5000, 1500, 100)
    avg_occup = st.sidebar.number_input('Average House Occupancy', 1.0, 10.0, 2.5, 0.25)
    latitude = st.sidebar.number_input('Latitude', 32.0, 42.0, 35.6, 0.1)
    longitude = st.sidebar.number_input('Longitude', -124.0, -114.0, -119.5, 0.1)
    
    data = {
        'HouseAge': house_age,
        'MedInc': med_inc,
        'AveRooms': avg_rooms,
        'AveBedrms': avg_bedrms,
        'Population': population,
        'AveOccup': avg_occup,
        'Latitude': latitude,
        'Longitude': longitude
    }
    
    return data

# Call the function to get the user's input.
user_inputs = user_input_features()


# Convert the user's input dictionary into a pandas DataFrame.
# The `index=[0]` argument is crucial; it tells pandas to create a DataFrame with a single row.
input_df = pd.DataFrame(user_inputs, index=[0])

# Create the 'rooms_per_person' feature.
# We add a small check to avoid division by zero, a good robust practice.
if input_df['Population'][0] > 0:
    input_df['rooms_per_person'] = input_df['AveRooms'][0] / input_df['Population'][0]
else:
    # If population is zero, this ratio is undefined. We can set it to 0 or another sensible default.
    input_df['rooms_per_person'] = 0

# Create the 'bedrooms_per_room' feature.
if input_df['AveRooms'][0] > 0:
    input_df['bedrooms_per_room'] = input_df['AveBedrms'][0] / input_df['AveRooms'][0]
else:
    input_df['bedrooms_per_room'] = 0

final_feature_order = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 
                       'AveOccup', 'Latitude', 'Longitude', 'rooms_per_person', 'bedrooms_per_room']

# Reorder the columns of our input DataFrame to match the training data.
input_df = input_df[final_feature_order]

st.subheader('Final Input Features for Prediction')
st.write(input_df)

if st.button('Predict Price'):
    # --- HIGHLIGHTED CHANGE: The code below is now inside the button's logic ---

    # Step 1: Scale the user's input data.
    scaled_input = scaler.transform(input_df)

    prediction = model.predict(scaled_input)

    # The prediction is an array like [4.53], so we extract the single value from it.
    predicted_price = prediction[0]

    # Convert the model's output (in hundreds of thousands) to an actual dollar value.
    final_price = predicted_price * 100000

    st.success(f'The predicted median house price is: ${final_price:,.0f}')


