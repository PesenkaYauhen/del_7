#Найдите наименьшее натуральное число N>=10, такое, что оно не делится на 7,
# но если любую его цифру заменить на 7, то получится число, кратное 7.

for n in range(10, 100):
    if n % 7 == 0:

        n_str = str(n) # конвертируем число в строку
        n_str_1 = "7" + n_str[1] # меняем первое число на 7
        n_str_2 = n_str[0] + "7"
        #n_str_3 = n_str[0] + n_str[1] +"7"
        #n_str_4 = n_str[0] + n_str[1] + n_str[2]+ "7"
        if int(n_str_1 ) % 7 == 0 and int(n_str_2) % 7 == 0 : # проверяем соблюдается ли деление на 7 при замене
            print(n)
