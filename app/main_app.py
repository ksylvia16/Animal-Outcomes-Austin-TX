import numpy as np
import streamlit as st
import pickle
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.pipeline import Pipeline

from sklearn.preprocessing import OneHotEncoder, StandardScaler
import pandas as pd

# bring in categorical values
animal_breed_list = pickle.load(open('./model/animal_breed_list.pkl','rb'))
animal_color_list = pickle.load(open('./model/animal_color_list.pkl','rb'))
animal_type_list = pickle.load(open('./model/animal_type_list.pkl','rb'))
animal_condition_list = pickle.load(open('./model/intake_cond_list.pkl','rb'))

intake_type = st.selectbox(
    'What type of intake is this?',
    ['Stray', 'Owner Surrender', 'Public Assist', 'Euthanasia Request',
     'Wildlife', 'Abandoned']
)

type = st.selectbox(
    'What is the type of animal',
    animal_type_list
)

color = st.selectbox(
    'What color is the animal?',
    animal_color_list
)

breed = st.selectbox(
    'What breed is the animal?',
    animal_breed_list
)

if breed.find('mix') == -1:
    mix = 0
else:
    mix = 1

intake_cond = st.selectbox(
    'What condition is the animal?',
    animal_condition_list
)

month_map = {
    'January': '1',
    'February': '2',
    'March': '3',
    'April': '4',
    'May': '5',
    'June': '6',
    'July': '7',
    'August': '8',
    'September': '9',
    'October': '10',
    'November': '11',
    'December': '12'
}

month = st.selectbox(
    'What month is it?',
    month_map.keys()
)

day = st.selectbox(
    'What day is it?',
    ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
)

prev_adopt = st.number_input(
    'How many previous adoption?',
    step=1
)

prev_transfer = st.number_input(
    'How many previous transfers?',
    step=1
)

prev_ret_to_owner= st.number_input(
    'How many previous returns to owner?',
    step=1
)

prev_rto_adopt = st.number_input(
    'How many previous return to owner adoptions?',
    step=1
)

prev_disposal = st.number_input(
    'How many times has the animal been brought for disposal?',
    step=1
)

prev_missing = st.number_input(
    'How many times has the animal gone missing?',
    step=1
)

age_upon_intake = st.number_input(
    'What is the animal\'s age upon intake (in years)?'
)

named_in_map = {
    'Yes': 1,
    'No': 0
}

is_named_in = st.selectbox(
    'Is the animal named upon intake?',
    named_in_map.keys()
)

sex = st.selectbox(
    'What is the sex of the animal?',
    ['Male','Female']
)

is_neutered = st.selectbox(
    'Is the animal neutered',
    ['Neutered/Spayed','Intact']
)

days_in_shelter = st.number_input(
    'How many days has the animal been in a shelter?',
    value=0
)

if age_upon_intake > 6:
    age_type = '6 Years-10 Years'
elif 2 < age_upon_intake <= 6:
    age_type = '2 Years-6 Years'
elif .5 < age_upon_intake <= 2:
    age_type = '6 Months-2 Years'
else:
    age_type = '< 6 Months '

# sanitize user input
encoder = pickle.load(open('./model/input_encoder.pkl','rb'))
numeric_input = np.array([prev_adopt,prev_transfer,prev_ret_to_owner,
                          prev_rto_adopt,prev_disposal,prev_missing,
                          age_upon_intake,named_in_map[is_named_in],
                          mix,days_in_shelter])
categorical_input = np.array([
    type, color, breed, intake_type, intake_cond,
    month_map[month], day, sex, is_neutered, age_type
]).reshape(1,-1)[0]
categorical_input = encoder.transform(categorical_input.reshape(1,-1))[0]
user_input = np.hstack([numeric_input,categorical_input])

# load the models
stray_model = pickle.load(open('./model/stray_pipe.pkl','rb'))
ownersurrender_model = pickle.load(open('./model/ownersurrender_pipe.pkl','rb'))
passist_model = pickle.load(open('./model/pubassist_pipe.pkl','rb'))
euth_model = pickle.load(open('./model/euth_pipe.pkl','rb'))
wlife_model = pickle.load(open('./model/wlife_pipe.pkl','rb'))
abandoned_model = pickle.load(open('./model/abandoned_pipe.pkl','rb'))

# determine prediction
pred = []
if intake_type == 'Stray':
    pred = stray_model.predict(user_input.reshape(1,-1))
elif intake_type == 'Owner Surrender':
    pred = ownersurrender_model.predict(user_input.reshape(1,-1))
elif intake_type == 'Public Assist':
    pred = passist_model.predict(user_input.reshape(1,-1))
elif intake_type == 'Euthanasia Request':
    pred = euth_model.predict(user_input.reshape(1,-1))
elif intake_type == 'Wildlife':
    pred = wlife_model.predict(user_input.reshape(1,-1))
elif intake_type == 'Abandoned':
    pred = abandoned_model.predict(user_input.reshape(1,-1))

if st.button('Make Prediction'):
    if pred == [1]:
        st.write('We Predict an Adoption')
    elif pred == [0]:
        st.write('We do not predict an Adoption')
