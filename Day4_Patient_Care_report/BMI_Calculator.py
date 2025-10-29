#BMI calculator (body mass index)
#Is calculated by comparing persons weight by their height
#Expressed as weight in Kg /height in m
#used to assess body composition and potential health risks based on individuals weight and height
#Provides general indication of body fat and corelation to chronic diseases such: Type 2 diabetes,
#  certain cancer etec. However, its not a direct measure of body fats.

            #<18= underweight
            #18 - 25 = normal weight
            #25 - 30 = overweight
            #> 30 = obese

weight = float(input('Enter your weight in KG: '))
height = float(input('Enter your height in metres: '))

bmi = weight / (height **2)

print(f'Your Body Mass Index(BMI) is {bmi:.2f}')

#classifications

if bmi < 18:
    print('Category: Underweight')
    print('Recomendations: Seek medical advice for a healthy diet plan')
elif 18 <= bmi < 25:
    print('Category: Normal')
    print('Excellent!! keep up a healthy lifestyele')
elif 25 <=  bmi < 30:
    print('Category: Overweight.')
    print('Recomendations: Do regular exercise and kindly seek medical consultation!')
else:
    print('Category: Obese')
    print('Kindly seek medical advice!!')



