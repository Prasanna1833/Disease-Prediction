from django.shortcuts import render
import joblib
from .models import History

def printHistory(request):
    histories = History.objects.all().order_by('-timestamp')
    return render(request,'history.html',{'histories':histories})


def home(request):
    symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
            'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 
            'spotting_urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 
            'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 
            'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 
            'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 
            'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 
            'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 
            'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 
            'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 
            'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 
            'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 
            'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 
            'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 
            'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 
            'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 
            'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 
            'belly_pain', 'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 'increased_appetite', 
            'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 
            'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 
            'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 
            'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 
            'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
    return render(request, 'home.html',{'symptoms':symptoms})

def result(request):
    
    
    symptoms = ['itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering', 'chills', 'joint_pain',
            'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting', 'vomiting', 'burning_micturition', 
            'spotting_urination', 'fatigue', 'weight_gain', 'anxiety', 'cold_hands_and_feets', 'mood_swings', 
            'weight_loss', 'restlessness', 'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 
            'high_fever', 'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache', 
            'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes', 'back_pain', 
            'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine', 'yellowing_of_eyes', 
            'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach', 'swelled_lymph_nodes', 'malaise', 
            'blurred_and_distorted_vision', 'phlegm', 'throat_irritation', 'redness_of_eyes', 'sinus_pressure', 
            'runny_nose', 'congestion', 'chest_pain', 'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 
            'pain_in_anal_region', 'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising', 
            'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid', 'brittle_nails', 
            'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts', 'drying_and_tingling_lips', 'slurred_speech', 
            'knee_pain', 'hip_joint_pain', 'muscle_weakness', 'stiff_neck', 'swelling_joints', 'movement_stiffness', 
            'spinning_movements', 'loss_of_balance', 'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 
            'bladder_discomfort', 'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching', 
            'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium', 'red_spots_over_body', 
            'belly_pain', 'abnormal_menstruation', 'dischromic_patches', 'watering_from_eyes', 'increased_appetite', 
            'polyuria', 'family_history', 'mucoid_sputum', 'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 
            'receiving_blood_transfusion', 'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen', 
            'history_of_alcohol_consumption', 'fluid_overload', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations', 
            'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling', 'silver_like_dusting', 
            'small_dents_in_nails', 'inflammatory_nails', 'blister', 'red_sore_around_nose', 'yellow_crust_ooze']
    diseases = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction', 'Peptic ulcer diseae', 'AIDS', 
            'Diabetes', 'Gastroenteritis', 'Bronchial Asthma', 'Hypertension', 'Migraine', 'Cervical spondylosis', 
            'Paralysis (brain hemorrhage)', 'Jaundice', 'Malaria', 'Chicken pox', 'Dengue', 'Typhoid', 'hepatitis A', 
            'Hepatitis B', 'Hepatitis C', 'Hepatitis D', 'Hepatitis E', 'Alcoholic hepatitis', 'Tuberculosis', 
            'Common Cold', 'Pneumonia', 'Dimorphic hemmorhoids(piles)', 'Heart attack', 'Varicose veins', 'Hypothyroidism', 
            'Hyperthyroidism', 'Hypoglycemia', 'Osteoarthritis', 'Arthritis', '(vertigo) Paroymsal Positional Vertigo', 'Acne', 
            'Urinary tract infection', 'Psoriasis', 'Impetigo'] 
    nb = joblib.load('naive_bayes_model.sav')
    clf = joblib.load('decision_tree_model.sav')
    knn = joblib.load('kNearest_model.sav')
    rf = joblib.load('random_forest_model.sav')


    if request.method == 'POST':
        selected_symptoms = []
        selected_symptoms.append(request.POST.get('symptom1'))
        selected_symptoms.append(request.POST.get('symptom2'))
        selected_symptoms.append(request.POST.get('symptom3'))
        selected_symptoms.append(request.POST.get('symptom4'))
        selected_symptoms.append(request.POST.get('symptom5'))

        l2 = [1 if symptom in selected_symptoms else 0 for symptom in symptoms]
       
        naive_bayes = diseases[nb.predict([l2])[0]]
        decision_tree= diseases[clf.predict([l2])[0]]
        kNearest_neighbour= diseases[knn.predict([l2])[0]]
        random_forest= diseases[rf.predict([l2])[0]]
        
        diseases = {"naive_bayes":naive_bayes,"decision_tree":decision_tree,"kNearest_neighbour":kNearest_neighbour,"random_forest":random_forest}
        name=request.POST['name']
        age=request.POST['age']
        symptoms = selected_symptoms
        predicted_disease = diseases
        
        history = History(name=name,age=age,symptoms=symptoms,predicted_disease=predicted_disease)
        history.save()

    return render(request,'result.html',{'naive_bayes':naive_bayes,'decision_tree':decision_tree,'kNearest_neighbour':kNearest_neighbour,'random_forest':random_forest})

# def heart(request):
#     model = joblib.load('heart_disease_model.sav')
#     list = []
#     hasHeartDisease = 0
#     if request.method == 'POST':
#         list.append(request.POST.get('age'))
#         list.append(request.POST.get('sex'))
#         list.append(request.POST.get('type'))
#         list.append(request.POST.get('bp'))
#         list.append(request.POST.get('cholestrol'))
#         list.append(request.POST.get('sugar'))
#         list.append(request.POST.get('cardiograph'))
#         list.append(request.POST.get('heart_rate'))
#         list.append(request.POST.get('angina'))
#         list.append(request.POST.get('depression'))
#         list.append(request.POST.get('slope'))
#         list.append(request.POST.get('vessels'))
#         list.append(request.POST.get('effect'))

#         hasHeartDisease = model.predict([list])[0]
         
#     return render(request,'heart.html',{'hasHeartDisease':hasHeartDisease})

def heart(request):
    model = joblib.load('heart_disease_model.sav')
    features = ['age', 'sex', 'type', 'bp', 'cholestrol', 'sugar', 'cardiograph', 
                'heart_rate', 'angina', 'depression', 'slope', 'vessels', 'effect']
    values = []

    if request.method == 'POST':
        for feature in features:
            value = request.POST.get(feature)
            if value is not None:
                values.append(float(value))  # Convert the input value to float
            else:
                # Handle missing values appropriately, e.g., by setting a default value
                values.append(0.0)

        hasHeartDisease = model.predict([values])[0]
    else:
        hasHeartDisease = 0  # Default value if the form is not submitted

    return render(request, 'heart.html', {'hasHeartDisease': hasHeartDisease})

def parkinson(request):
    model = joblib.load('parkinsons_model.sav')
    features = ['avgmdvp', 'maxadvp', 'minadvp', 'percentmdvp', 'absmdvp', 'rapmdvp', 'ppqmdvp', 
                'jitter', 'shimmdvp', 'dbmdvp', 'Shimmer1', 'Shimmer2', 'MDVP','Shimmer3', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1','spread2','D2','PPE']
    values = []

    if request.method == 'POST':
        for feature in features:
            value = request.POST.get(feature)
            if value is not None:
                values.append(float(value))  # Convert the input value to float
            else:
                # Handle missing values appropriately, e.g., by setting a default value
                values.append(0.0)

        hasParkinson = model.predict([values])[0]
    else:
        hasParkinson = 0  # Default value if the form is not submitted
    return render(request,'parkinson.html',{'hasParkinson':hasParkinson})

# def diabetes(request):
#     model = joblib.load('diabetes_model.sav')
#     hasDiabetes = 0
#     list = []
#     if request.method == 'POST':
        
#         list.append(request.POST.get('pregnancy'))
#         list.append(request.POST.get('glucose'))
#         list.append(request.POST.get('bp'))
#         list.append(request.POST.get('thickness'))
#         list.append(request.POST.get('insulin'))
#         list.append(request.POST.get('bmi'))
#         list.append(request.POST.get('pedigree'))
#         list.append(request.POST.get('age'))
        
#         hasDiabetes = model.predict([list])[0]

#     return render(request,'diabetes.html',{'hasDiabetes':hasDiabetes })

def diabetes(request):
    model = joblib.load('diabetes_model.sav')
    features = ['pregnancy', 'glucose',  'bp', 'thickness', 'insulin', 'bmi', 
                'pedigree', 'age']
    values = []

    if request.method == 'POST':
        for feature in features:
            value = request.POST.get(feature)
            if value is not None:
                values.append(float(value))  # Convert the input value to float
            else:
                # Handle missing values appropriately, e.g., by setting a default value
                values.append(0.0)

        hasDiabetes = model.predict([values])[0]
    else:
        hasDiabetes = 0  # Default value if the form is not submitted

    return render(request, 'diabetes.html', {'hasDiabetes': hasDiabetes})

# def error(request,unknown_path):
#     return render(request,'error.html',{'path':unknown_path},status=404)

def not_found(request,unknown_path):
    return render(request,'error.html',{'path':unknown_path},status=404)