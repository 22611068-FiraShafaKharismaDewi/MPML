import pickle
import streamlit as st
import numpy as np

# Membaca model
onlinefood_model = pickle.load(open('model_onlinefood.sav','rb'))

# Judul web
st.title('Predictions Online Food')
# Input data dengan contoh angka valid untuk pengujian
Age = st.text_input('Age')
Gender = st.text_input('Gender')
Marital_Status = st.text_input('Marital Status')
Occupation = st.text_input('Occupation')
Monthly_Income = st.text_input('Monthly Income')
Educational_Qualifications = st.text_input('Educational Qualifications')
Family_size = st.text_input('Family size')
latitude = st.text_input('latitude')
longitude = st.text_input('longitude')
Pin_code = st.text_input('Pin code')
Feedback = st.text_input('Feedback')

onlinefood_predict = ''

# Membuat tombol untuk prediksi
if st.button('Predict'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(Age), float(Gender), float(Marital_Status),
                            float(Occupation), float(Monthly_Income), float(Educational_Qualifications), 
                            float(Family_size), float(latitude), float(longitude), 
                            float(Pin_code), float(Feedback)]])
        # Lakukan prediksi
        predict_onlinefood = onlinefood_model.predict(inputs)
        
        if predict_onlinefood[0] == 1:
            onlinefood_predict = 'Yes'
            st.success(onlinefood_predict)
        else:
            onlinefood_predict = '<span style="color:red">Bukan Pokemon Lagendary</span>'
            st.markdown(onlinefood_predict, unsafe_allow_html=True)
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")