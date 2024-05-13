from django.shortcuts import render
import joblib
import pickle
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
       
        name=request.POST['name']
        age=request.POST['age']
        symptom1=request.POST.get('symptom1')
        symptom2=request.POST.get('symptom2')

        errors=[]
        if not name:
            errors.append("Name is the required field, Enter your name.")

        if not age:
            errors.append("Age is the required field, Enter your age.")

        if not symptom1:
            errors.append("Symptom 1 is necessary, Enter the first symptom.")

        if not symptom2:
            errors.append("At least 2 symptoms are necessary.")
        
        if errors:
            return render(request,'result.html',{'errors':errors})

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
    prev = False
    if request.method == 'POST':
        prev = not prev
        age=request.POST['age']
        sex=request.POST['sex'] 
        typpe=request.POST.get('type')
        bp=request.POST.get('bp')
        cholestrol=request.POST.get('cholestrol')
        sugar=request.POST.get('sugar')
        cardiograph=request.POST.get('cardiograph')
        heart_rate=request.POST.get('heart_rate')
        angina=request.POST.get('angina')
        depression=request.POST.get('depression')
        slope=request.POST.get('slope')
        vessels=request.POST.get('vessels')
        effect=request.POST.get('effect')

        error = False
        if not age or not sex or  not typpe or not bp or not cholestrol or not sugar or  not cardiograph or not heart_rate or  not angina or not depression or not slope or not vessels or  not effect:
            error = True
            return render(request, 'heart.html', {'error': error})

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

    return render(request, 'heart.html', {'hasHeartDisease': hasHeartDisease,'prev':prev})

def parkinson(request):
    model = joblib.load('parkinsons_model.sav')
    features = ['avgmdvp', 'maxadvp', 'minadvp', 'percentmdvp', 'absmdvp', 'rapmdvp', 'ppqmdvp', 
                'jitter', 'shimmdvp', 'dbmdvp', 'Shimmer1', 'Shimmer2', 'MDVP','Shimmer3', 'NHR', 'HNR', 'RPDE', 'DFA', 'spread1','spread2','D2','PPE']
    values = []
    prev = False
    if request.method == 'POST':
        prev = not prev
        avgmdvp=request.POST.get('avgmdvp')
        maxadvp=request.POST.get('maxadvp') 
        minadvp=request.POST.get('minadvp')
        percentmdvp=request.POST.get('percentmdvp')
        absmdvp=request.POST.get('absmdvp')
        rapmdvp=request.POST.get('rapmdvp')
        ppqmdvp=request.POST.get('ppqmdvp')
        jitter=request.POST.get('jitter')
        shimmdvp=request.POST.get('shimmdvp')
        dbmdvp=request.POST.get('dbmdvp')
        Shimmer1=request.POST.get('Shimmer1')
        Shimmer2=request.POST.get('Shimmer2')
        MDVP=request.POST.get('MDVP')
        Shimmer3=request.POST.get('Shimmer3')
        NHR=request.POST.get('NHR')
        HNR=request.POST.get('HNR')
        RPDE=request.POST.get('RPDE')
        DFA=request.POST.get('DFA')
        spread1=request.POST.get('spread1')
        spread2=request.POST.get('spread2')
        D2=request.POST.get('D2')
        PPE=request.POST.get('PPE')
       

        error = False
        if not avgmdvp or not maxadvp or  not minadvp or not percentmdvp or not absmdvp or not rapmdvp or  not ppqmdvp or not jitter or  not shimmdvp or not dbmdvp or not Shimmer1 or not Shimmer2 or  not MDVP or not Shimmer3 or not NHR or not HNR or  not RPDE or not DFA or  not spread1 or not spread2 or not D2 or not PPE:
            error = True
            return render(request, 'parkinson.html', {'error': error})
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
    return render(request,'parkinson.html',{'hasParkinson':hasParkinson,'prev':prev})

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
    prev = False
    if request.method == 'POST':
        prev = not prev
        pregnancy=request.POST.get('pregnancy')
        glucose=request.POST.get('glucose') 
        bp=request.POST.get('bp')
        thickness=request.POST.get('thickness')
        insulin=request.POST.get('insulin')
        bmi=request.POST.get('bmi')
        pedigree=request.POST.get('pedigree')
        age=request.POST.get('age')
        
        error = False
        if not pregnancy or not glucose or  not bp or not thickness or not insulin or not bmi or  not pedigree or not age:
            error = True
            return render(request, 'diabetes.html', {'error': error})
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

    return render(request, 'diabetes.html', {'hasDiabetes': hasDiabetes,'prev':prev})

# def error(request,unknown_path):
#     return render(request,'error.html',{'path':unknown_path},status=404)

def cardio(request):
    model = joblib.load('cardio.pkl')
    features = ['gender', 'smoking', 'glucose', 'age', 'bmi', 'diabetes', 'hypertension', 
                'HbA1c']
    values = []
    prev = False
    if request.method == 'POST':
        prev = not prev
        gender=request.POST.get('gender')
        smoking=request.POST.get('smoking') 
        glucose=request.POST.get('glucose')
        age=request.POST.get('age')
        bmi=request.POST.get('bmi')
        diabetes=request.POST.get('diabetes')
        hypertension=request.POST.get('hypertension')
        HbA1c=request.POST.get('HbA1c')
        
        error = False
        if not gender or not smoking or  not glucose or not age or not bmi or not diabetes or  not hypertension or not HbA1c :
            error = True
            return render(request, 'cardio.html', {'error': error})
        for feature in features:
            value = request.POST.get(feature)
            if value is not None:
                values.append(float(value))  # Convert the input value to float
            else:
                # Handle missing values appropriately, e.g., by setting a default value
                values.append(0.0)

        hasCardio = model.predict([values])[0]
    else:
        hasCardio = 0  # Default value if the form is not submitted
    return render(request,'cardio.html',{'hasCardio':hasCardio,'prev':prev})

def gestational(request):
   
    model = pickle.load(open('gestation.pkl', 'rb'))
    features = ['age', 'history', 'dia_BP', 'pregnancy', 'loss', 'OGTT', 'gestation', 
                'default','haemoglobin','bmi','PCOS','cycle','HDL','sys_BP','prediabetes']
    values = []
    prev = False
    if request.method == 'POST':
        prev = not prev
        age=request.POST.get('age')
        history=request.POST.get('history') 
        dia_BP=request.POST.get('dia_BP')
        pregnancy=request.POST.get('pregnancy')
        loss=request.POST.get('loss')
        OGTT=request.POST.get('OGTT')
        gestation=request.POST.get('gestation')
        default=request.POST.get('default')
        haemoglobin=request.POST.get('haemoglobin')
        bmi=request.POST.get('bmi') 
        PCOS=request.POST.get('PCOS')
        cycle=request.POST.get('cycle')
        HDL=request.POST.get('HDL')
        sys_BP=request.POST.get('sys_BP')
        prediabetes=request.POST.get('prediabetes')
        
        
        error = False
        if not age or not history or  not dia_BP or not pregnancy or not loss or not OGTT or  not gestation or not default or  not haemoglobin or not bmi or not PCOS or not cycle or  not HDL or not sys_BP or not prediabetes  :
            error = True
            return render(request, 'gestational.html', {'error': error})
        for feature in features:
            value = request.POST.get(feature)
            if value is not None:
                values.append(float(value))  # Convert the input value to float
            else:
                # Handle missing values appropriately, e.g., by setting a default value
                values.append(0.0)

        hasGestational = model.predict([values])[0]
    else:
        hasGestational = 0  # Default value if the form is not submitted
   

    return render(request,'gestational.html',{'hasGestational':hasGestational,'prev':prev})

def nephropathy(request):
    # model = joblib.load('nephropathy.pkl')
    model = pickle.load(open('nephropathy.pkl', 'rb'))
    features = ['sex', 'smoking', 'DBP', 'HDLC', 'age', 'drinking', 'HbA1c', 
                'LDLC','duration','bmi','FBG','insulin','retinopathy','SBP','peptide']
    values = []
    prev = False
    if request.method == 'POST':
        prev = not prev
        sex=request.POST.get('sex')
        smoking=request.POST.get('smoking') 
        DBP=request.POST.get('DBP')
        HDLC=request.POST.get('HDLC')
        age=request.POST.get('age')
        drinking=request.POST.get('drinking')
        HbA1c=request.POST.get('HbA1c')
        LDLC=request.POST.get('LDLC')
        duration=request.POST.get('duration')
        bmi=request.POST.get('bmi') 
        FBG=request.POST.get('FBG')
        insulin=request.POST.get('insulin')
        retinopathy=request.POST.get('retinopathy')
        SBP=request.POST.get('SBP')
        peptide=request.POST.get('peptide')
        
        
        error = False
        if not sex or not smoking or  not DBP or not HDLC or not age or not drinking or  not HbA1c or not LDLC or  not duration or not bmi or not FBG or not insulin or  not retinopathy or not SBP or not peptide  :
            error = True
            return render(request, 'nephropathy.html', {'error': error})
        for feature in features:
            value = request.POST.get(feature)
            if value is not None:
                values.append(float(value))  # Convert the input value to float
            else:
                # Handle missing values appropriately, e.g., by setting a default value
                values.append(0.0)

        hasNephropathy = model.predict([values])[0]
    else:
        hasNephropathy = 0  # Default value if the form is not submitted
   

    return render(request,'nephropathy.html',{'hasNephropathy':hasNephropathy,'prev':prev})


def not_found(request,unknown_path):
    return render(request,'error.html',{'path':unknown_path },status=404)

def about(request):
    return render(request,'about.html')