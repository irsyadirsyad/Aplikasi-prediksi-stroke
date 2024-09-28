import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.spinner import Spinner
from kivy.uix.scrollview import ScrollView
from kivy.uix.anchorlayout import AnchorLayout
import pandas as pd
import joblib

# Memuat model prediksi stroke yang telah dilatih
logistic_grid = joblib.load('logistic_model_stroke_web.pkl')

class StrokePredictionApp(App):
    def build(self):
        # Menggunakan ScrollView untuk memastikan UI tidak terpotong pada layar kecil
        root = ScrollView(size_hint=(1, None), size=(400, 600))

        # Membuat GridLayout untuk tata letak yang lebih rapi dan bersih
        self.layout = GridLayout(cols=2, padding=10, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))

        # Field input numerik
        self.age_input = TextInput(hint_text='Umur', input_filter='float', multiline=False)
        self.hypertension_input = Spinner(text='Tidak', values=('Tidak', 'Ya'))
        self.heart_disease_input = Spinner(text='Tidak', values=('Tidak', 'Ya'))
        self.glucose_input = TextInput(hint_text='Glukosa Rata-rata', input_filter='float', multiline=False)
        self.bmi_input = TextInput(hint_text='BMI', input_filter='float', multiline=False)

        # Field input kategori menggunakan Spinner (dropdown)
        self.gender_input = Spinner(text='Perempuan', values=('Laki-laki', 'Perempuan', 'Lainnya'))
        self.married_input = Spinner(text='Tidak', values=('Ya', 'Tidak'))
        self.work_type_input = Spinner(text='Swasta', values=('Swasta', 'Wiraswasta', 'Tidak Pernah Bekerja', 'Anak-anak'))
        self.residence_type_input = Spinner(text='Perkotaan', values=('Perkotaan', 'Pedesaaan'))
        self.smoking_input = Spinner(text='Tidak Pernah Merokok', values=('Dulu Merokok', 'Tidak Pernah Merokok', 'Merokok'))

        # Menambahkan elemen-elemen UI ke dalam layout secara teratur
        self.add_widget_to_layout('Umur', self.age_input)
        self.add_widget_to_layout('Hipertensi', self.hypertension_input)
        self.add_widget_to_layout('Penyakit Jantung', self.heart_disease_input)
        self.add_widget_to_layout('Glukosa Rata-rata', self.glucose_input)
        self.add_widget_to_layout('BMI', self.bmi_input)
        self.add_widget_to_layout('Jenis Kelamin', self.gender_input)
        self.add_widget_to_layout('Status Pernikahan', self.married_input)
        self.add_widget_to_layout('Pekerjaan', self.work_type_input)
        self.add_widget_to_layout('Tempat Tinggal', self.residence_type_input)
        self.add_widget_to_layout('Status Merokok', self.smoking_input)

        # Membuat tombol untuk prediksi dalam AnchorLayout agar terletak di tengah
        anchor_layout = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None, height=50)
        self.predict_button = Button(text="Prediksi", size_hint=(0.5, 1))
        self.predict_button.bind(on_press=self.predict_stroke)
        anchor_layout.add_widget(self.predict_button)

        # Membuat label untuk menampilkan hasil prediksi
        self.result_label = Label(text="", size_hint_y=None, height=50)

        # Menambahkan tombol dan hasil prediksi ke dalam layout
        self.layout.add_widget(Label(text=''))  # Placeholder for alignment
        self.layout.add_widget(anchor_layout)   # Letakkan tombol di baris layout

        # Menambahkan label hasil prediksi di bawah tombol
        self.layout.add_widget(Label(text='Hasil Prediksi:', size_hint_y=None, height=40))
        self.layout.add_widget(self.result_label)

        # Menambahkan layout ke dalam root scrollview
        root.add_widget(self.layout)

        return root

    def add_widget_to_layout(self, label_text, widget):
        """Helper function to add label and widget to the layout"""
        label = Label(text=label_text, size_hint_y=None, height=40)
        widget.size_hint_y = None
        widget.height = 40
        self.layout.add_widget(label)
        self.layout.add_widget(widget)

    def predict_stroke(self, instance):
        try:
            # Mengumpulkan data input dan mengonversi ke format yang diperlukan oleh model
            new_user_data = {
                'age': float(self.age_input.text),
                'hypertension': 1 if self.hypertension_input.text == 'Ya' else 0,
                'heart_disease': 1 if self.heart_disease_input.text == 'Ya' else 0,
                'avg_glucose_level': float(self.glucose_input.text),
                'bmi': float(self.bmi_input.text)
            }

            # Memproses input jenis kelamin
            gender = self.gender_input.text.strip().lower()
            if gender == 'laki-laki':
                new_user_data['gender_Male'] = 1
                new_user_data['gender_Other'] = 0
            elif gender == 'lainnya':
                new_user_data['gender_Male'] = 0
                new_user_data['gender_Other'] = 1
            else:  # default Perempuan
                new_user_data['gender_Male'] = 0
                new_user_data['gender_Other'] = 0

            # Memproses status pernikahan
            new_user_data['ever_married_Yes'] = 1 if self.married_input.text == 'Ya' else 0

            # Memproses jenis pekerjaan
            work_type = self.work_type_input.text
            new_user_data['work_type_Never_worked'] = 1 if work_type == 'Tidak Pernah Bekerja' else 0
            new_user_data['work_type_Private'] = 1 if work_type == 'Swasta' else 0
            new_user_data['work_type_Self-employed'] = 1 if work_type == 'Wiraswasta' else 0
            new_user_data['work_type_children'] = 1 if work_type == 'Anak-anak' else 0

            # Memproses tipe tempat tinggal
            new_user_data['Residence_type_Urban'] = 1 if self.residence_type_input.text == 'Perkotaan' else 0

            # Memproses status merokok
            smoking_status = self.smoking_input.text.strip().lower()
            new_user_data['smoking_status_formerly smoked'] = 1 if smoking_status == 'dulu merokok' else 0
            new_user_data['smoking_status_never smoked'] = 1 if smoking_status == 'tidak pernah merokok' else 0
            new_user_data['smoking_status_smokes'] = 1 if smoking_status == 'merokok' else 0

            # Mengonversi dictionary ke DataFrame untuk prediksi model
            new_user_df = pd.DataFrame([new_user_data])

            # Melakukan prediksi menggunakan model yang telah dilatih
            stroke_prediction = logistic_grid.predict(new_user_df)

            # Menampilkan hasil prediksi
            if stroke_prediction[0] == 1:
                self.result_label.text = "Hasil: Kemungkinan Stroke"
            else:
                self.result_label.text = "Hasil: Tidak Kemungkinan Stroke"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}, periksa input Anda."

# Menjalankan aplikasi
if __name__ == '__main__':
    StrokePredictionApp().run()
