#Papatient  Risk Report
name = input('Enter your name: ')
age = int(input('Enter your age: '))
if age <18:
    print(f'Hello {name}, Sorry this service is only applicable for adults( 18 yrs and above).')
else:
    weight = float(input('Enter your weight in KG: '))
    height = float(input('Enter your height in metres: '))
    bmi = weight / (height **2)
    print(f'hello {name} Your body mass index is :{bmi:.2f}')
    #risks
    if bmi < 18:
        print('Category: Underweight')
        print('Health risks: Nutritional deficiency, weakened immune system, osteoporosis etc.')
        print('Recomendations: Seek medical attention for appropriate diet plan.')
    elif bmi  >= 18 and bmi <=25:
        print('Category: Normal weight')
        print(' Health risks: Low risks of chronic diseases.')
        print('Recomendations: Continue wit regular exercise,balanced diet and healthy lifestyle.')
    elif bmi >25 and bmi <=30:
        print('Category: Overweight')
        print('Health risks: Increased risks of type 2 diabetes, hypertension,cardiovascular diseases etc.')
        print('Recommendattions: Start regularly exercising, adopt a healthy living lifestyle (Avoid junk foods) and seek medical consultation.')
    else:
        print('Category: Obese')
        print('Health risks: Very high risks of chronic diseases ie heart diseases, stroke, cancers, type 2 diabetes etc.')
        print('Recommendations: Seek immediate medical attention, following a very strict diet plan and regular exercises. Measure you vitals')
    
    if bmi < 18:
        risk_level = 'moderate'
    elif 18 <= bmi <= 25:
        risk_level = 'low'
    elif 25<= bmi <=30:
         if age <40:
             risk_level = 'moderate'
         else:
             risk_level = 'high'    
    else:
        if age <40:
            risk_level = 'high'
        else:
            risk_level = 'very high'
    print(f'Hello {name}, Based on your BMi of {bmi:.2f} and age of {age}, Your general health risk level is {risk_level}. Please take necessary actions.')
   

print('\n-----------------------General summary report-----------------------')
print('Name: ', name)
print('age: ', age)
print('BMI: ', f'{bmi:.2f}')
print('Risk Level: ', risk_level)