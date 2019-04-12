def imc_calc(weight, height):
    imc = weight / (height * height)
    imc = imc_info(imc)
    return imc

def imc_info(imc):
    if imc <= 16:
        return 'Magreza Grave'
    elif (imc > 16 and imc < 17):
        return 'Magreza Moderada'
    elif (imc >= 17 and imc < 18.5):
        return 'Magreza Leve'
    elif (imc >= 18.5 and imc < 25):
        return 'Peso Ideal'
    elif (imc >= 25 and imc < 30):
        return 'Sobrepeso'
    elif (imc >= 30 and imc < 35):
        return 'Obesidade Grau I'
    elif (imc >= 35 and imc < 40):
        return 'Obesidade Grau II (Severa)'
    else:
        return 'Obesidade Grau III (Mórbita)'

def init_calc():
    try:
        weight =  float(input('Informe o seu peso: \n'))
        height =  float(input('Informe a sua altura: \n'))
        result = imc_calc(weight, height)
        print("Resutado: ", result)
    except:
        print('Por favor, informe os dados corretamente!')
        weight = 0
        height = 0
        init_calc()
    
init_calc()