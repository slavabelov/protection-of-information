import random
from Lab2 import make_primes

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя !?.,;:\n-'

array_primes = make_primes(1000)

while True:
    x = random.randint(7, 37)
    if x in array_primes:
        y = random.randint(7, 37)
        if y in array_primes:
            break


def Euler(p, q):
    result = (p-1)*(q-1)
    print('Функция Эйлера: ' + str(result))
    return result

a = Euler(x, y)
mod = x * y


def open_exponent():

    da = True
    while da:
        num = random.randint(1, 100)
        if num in array_primes and num < a and a % num != 0:
            right_num = num
            da = False
    print("Свободная экспонента: " + str(right_num))
    return right_num

def num_d():

    true = True
    i = 0
    right_d = 0
    while true:
        d = array_primes[i]
        if o_e * d % a == 1:
            right_d = d
            true = False
        else:
            i += 1
    print('Число d: ' + str(right_d))
    return right_d

o_e = open_exponent()
n_d = num_d()

def RSA(word):

    input = word
    input = input.lower()
    output=[]
    output_mod = []
    dec_numbers = []
    dec_output = []

    for character in input:
        number = alphabet.index(character)
        output.append(number)
    print(output)


    for numbers in output:
        mod_num = pow(numbers, o_e) % mod
        output_mod.append(mod_num)
    print(output_mod)


    for numbers_decrypted in output_mod:
        dec_num = pow(numbers_decrypted, n_d) % mod
        dec_numbers.append(dec_num)
    print(dec_numbers)


    for numb in dec_numbers:
        dec_word = alphabet[numb]
        dec_output.append(dec_word)
    print(dec_output)


    dec_output = ''.join(dec_output)
    print(dec_output)


if __name__ == "__main__":
    RSA("зло есть, стрегобор. меньшее, большее, среднее. суть одна. "
        "не мне тебя судить, я тоже не только добро творил в жизни."
        "но теперь, если придётся выбирать между одним злом и другим, "
        "я предпочту не выбирать вовсе")


