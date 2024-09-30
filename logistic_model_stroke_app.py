import PySimpleGUI as sg
import pandas as pd
import joblib

logistic_grid = joblib.load('logistic_model_stroke_web.pkl')

def predict_stroke(values):
    try:
        new_user_data = {
            'age': float(values['age']),
            'hypertension': 1 if values['hypertension'] == 'Ya' else 0,
            'heart_disease': 1 if values['heart_disease'] == 'Ya' else 0,
            'avg_glucose_level': float(values['glucose']),
            'bmi': float(values['bmi']),
            'gender_Male': 1 if values['gender'] == 'Laki-laki' else 0,
            'gender_Other': 1 if values['gender'] == 'Lainnya' else 0,
            'ever_married_Yes': 1 if values['married'] == 'Ya' else 0,
            'work_type_Never_worked': 1 if values['work_type'] == 'Tidak Pernah Bekerja' else 0,
            'work_type_Private': 1 if values['work_type'] == 'Swasta' else 0,
            'work_type_Self-employed': 1 if values['work_type'] == 'Wiraswasta' else 0,
            'work_type_children': 1 if values['work_type'] == 'Anak-anak' else 0,
            'Residence_type_Urban': 1 if values['residence'] == 'Perkotaan' else 0,
            'smoking_status_formerly smoked': 1 if values['smoking'] == 'Dulu Merokok' else 0,
            'smoking_status_never smoked': 1 if values['smoking'] == 'Tidak Pernah Merokok' else 0,
            'smoking_status_smokes': 1 if values['smoking'] == 'Merokok' else 0,
        }

        new_user_df = pd.DataFrame([new_user_data])

        stroke_prediction = logistic_grid.predict(new_user_df)

        if stroke_prediction[0] == 1:
            return "Hasil: Kemungkinan Stroke"
        else:
            return "Hasil: Tidak Kemungkinan Stroke"
    except Exception as e:
        return f"Error: {str(e)}, periksa input Anda."

layout = [
    [sg.Text('Umur'), sg.InputText(key='age')],
    [sg.Text('Hipertensi'), sg.Combo(['Tidak', 'Ya'], default_value='Tidak', key='hypertension')],
    [sg.Text('Penyakit Jantung'), sg.Combo(['Tidak', 'Ya'], default_value='Tidak', key='heart_disease')],
    [sg.Text('Glukosa Rata-rata'), sg.InputText(key='glucose')],
    [sg.Text('BMI'), sg.InputText(key='bmi')],
    [sg.Text('Jenis Kelamin'), sg.Combo(['Perempuan', 'Laki-laki', 'Lainnya'], default_value='Perempuan', key='gender')],
    [sg.Text('Status Pernikahan'), sg.Combo(['Ya', 'Tidak'], default_value='Tidak', key='married')],
    [sg.Text('Pekerjaan'), sg.Combo(['Swasta', 'Wiraswasta', 'Tidak Pernah Bekerja', 'Anak-anak'], default_value='Swasta', key='work_type')],
    [sg.Text('Tempat Tinggal'), sg.Combo(['Perkotaan', 'Pedesaaan'], default_value='Perkotaan', key='residence')],
    [sg.Text('Status Merokok'), sg.Combo(['Dulu Merokok', 'Tidak Pernah Merokok', 'Merokok'], default_value='Tidak Pernah Merokok', key='smoking')],
    [sg.Button('Prediksi'), sg.Button('Keluar')],
    [sg.Text('Hasil Prediksi:', size=(20, 1)), sg.Text('', key='result', size=(30, 1))],
]

window = sg.Window('Prediksi Stroke', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Keluar':
        break

    if event == 'Prediksi':
        result = predict_stroke(values)
        window['result'].update(result)

window.close()


