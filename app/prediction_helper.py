import streamlit as st
import pandas as pd
import joblib # Import joblib for loading
from sklearn.preprocessing import LabelEncoder # Still need LabelEncoder class for loading
from sklearn.compose import ColumnTransformer # Still need ColumnTransformer class for loading
from xgboost import XGBClassifier # Still need XGBClassifier class for loading

le_y = joblib.load('artifacts/label_encoder_y.joblib')
preprocessor = joblib.load('artifacts/preprocessor.joblib')
xgboost_model = joblib.load('artifacts/xgb_model.joblib')


def get_age_group(age):
    bins = [18, 26, 36, 46, 56, 71, float('inf')]
    labels = ['18-25', '26-35', '36-45', '46-55', '56-70', '70+']
    abc=pd.cut([age], bins=bins, labels=labels, right=False)
    return abc[0]

def prepare_input(age,gender,zone,occupation,income_levels,consume_frequency,current_brand,preferable_consumption_size,
                          awareness_of_other_brands,reasons_for_choosing_brands,flavor_preference,purchase_channel,
                          packaging_preference,health_concerns,typical_consumption_situations):
    
    age_group=get_age_group(age)

    # Create a dictionary with input values and dummy values for missing features
    input_data = {
        'gender' : gender,
        'zone' : zone,
        'occupation' : occupation,
        'income_levels' : income_levels,
        'consume_frequency(weekly)' : consume_frequency,
        'current_brand' : current_brand,
        'preferable_consumption_size' : preferable_consumption_size,
        'awareness_of_other_brands' : awareness_of_other_brands,
        'reasons_for_choosing_brands' : reasons_for_choosing_brands,
        'flavor_preference' : flavor_preference,
        'purchase_channel' : purchase_channel,
        'packaging_preference' : packaging_preference,
        'health_concerns' : health_concerns,
        'typical_consumption_situations' : typical_consumption_situations, 
        'age_group' : age_group
    }

    # Ensure all columns for features and cols_to_scale are present
    df = pd.DataFrame([input_data])

    #transform
    input_data=preprocessor.transform(df)

    return input_data


def predict(age,gender,zone,occupation,income_levels,consume_frequency,current_brand,preferable_consumption_size,
                          awareness_of_other_brands,reasons_for_choosing_brands,flavor_preference,purchase_channel,
                          packaging_preference,health_concerns,typical_consumption_situations):
    # Prepare input data
    input_df = prepare_input(age,gender,zone,occupation,income_levels,consume_frequency,current_brand,preferable_consumption_size,
                          awareness_of_other_brands,reasons_for_choosing_brands,flavor_preference,purchase_channel,
                          packaging_preference,health_concerns,typical_consumption_situations)

    predict_data=xgboost_model.predict(input_df)
    result=le_y.inverse_transform(predict_data)

    return result
