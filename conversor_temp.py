def temp_conversor(original_temp, original_type):
    if original_type == 'f':
        #Formula para converter Fahrenheit em Celsius
        temp_c =  (original_temp - 32) * 5 / 9
        result =  str(original_temp) + ' °F equivalem a ' + str(round(temp_c,2)) + ' °C'
        return result
    elif original_type == 'c':
        #Formula para converter Celsius em Fahrenheit
        temp_f = (original_temp * 9) / 5 + 32
        result =  str(original_temp) + ' °C equivalem a ' + str(round(temp_f,2)) + ' °F'
        return result
    else:
        return original_temp

while True:
    print(temp_conversor(int(input('Informe a temperatura original: ')), input('Informe a medida original: ').lower()))
    print(30 * '-')