import random
import tkinter as tk
from tkinter import messagebox
from tkinter.constants import E, END


def is_it_prime(n):
    d = 2
    while d < n:
        if n % d != 0:
            d += 1
        else:
            return False
    return True


def get_prime_numbers(fi=200):
    L = list(range(31, fi))
    prime_numbers = []
    for i in L:
        if is_it_prime(i):
            prime_numbers.append(i)
    return prime_numbers


def find_all_dividers(n):
    d = 2
    dividers = set()
    while d <= n:
        if n % d != 0:
            d += 1
        else:
            dividers.add(d)
            d += 1
    return dividers


def find_e(fi):
    flag = True
    while flag == True:
        e = random.choice(range(1000))
        if e % 2 == 0:
            e -= 1
        flag = (bool(find_all_dividers(e) & find_all_dividers(fi)))
    return e


def find_d(e, fi):
    # d - число обратное е по модулю fi => (d * e) % fi = 1
    d = 1
    while (d * e) % fi != 1:
        d += 1
    return d


def RSA_encode(message, e, mod):
    message_in_ASCII = []
    for i in message:
        message_in_ASCII.append(ord(i))
        # message_in_ASCII.reverse()

    encrypted_message = []
    for i in message_in_ASCII:
        a = i ** e % mod
        encrypted_message.append(a)
    return encrypted_message


def RSA_decode(encrypted_message, d, mod):
    decrypted_message = []
    for i in encrypted_message:
        a = i ** d % mod
        decrypted_message.append(a)

    message = []
    for i in decrypted_message:
        message.append(chr(i))
    return message


# ------

def tk_p_q_mod_fi():
    p, q = random.choices(get_prime_numbers(), k=2)
    e1.delete(0, END)
    e2.delete(0, END)
    e1.insert(0, p)
    e2.insert(0, q)
    mod_label['text'] = f'mod:  {p * q}'
    fi_label['text'] = f'φ: {(p - 1) * (q - 1)}'


def tk_keys():
    p = int(e1.get())
    q = int(e2.get())
    mod = p * q
    fi = (p - 1) * (q - 1)
    e = find_e(fi)
    d = find_d(e, fi)
    public_label['text'] = f'Открытый ключ: {{{e}, {mod}}}'
    privat_label['text'] = f'Личный ключ: {{{d}, {mod}}}'
    e_label['text'] = f'e: {e}'
    d_label['text'] = f'd: {d}'
    print(p, q, mod, fi, '___', e, d)


def self_tk_p_q_mod_fi():
    try:
        p = int(e1.get())
        q = int(e2.get())
        print(p, q)
    except:
        messagebox.showerror('О нет', 'Введите простые числа больше 30!')
    if is_it_prime(p) and is_it_prime(q) and p > 17 and q > 17:  # 30
        e1.delete(0, END)
        e2.delete(0, END)
        e1.insert(0, p)
        e2.insert(0, q)
        mod_label['text'] = f'mod:  {p * q}'
        fi_label['text'] = f'φ: {(p - 1) * (q - 1)}'
    else:
        messagebox.showerror('О нет', 'Числа p и q должны быть простыми, а так же больше 30!')


def tk_RSA_encode():
    m = entry_text.get(1.0, END)
    e = e_label.cget('text')
    e = int(e[3:])
    mod = int(e1.get()) * int(e2.get())
    exit_text.delete(1.0, END)
    exit_text.insert(1.0, RSA_encode(m, e, mod))


def tk_RSA_decode():
    m = exit_text.get(1.0, END)
    print('do split: ', m)
    m = m.split()
    print('posle split :', m)
    m = [int(item) for item in m]
    d = d_label.cget('text')
    d = int(d[3:])
    mod = int(e1.get()) * int(e2.get())
    print('m: ', m, '\nd: ', d, '\nmod: ', mod)
    m_decode = ''.join(RSA_decode(m, d, mod))
    entry_text.delete(1.0, END)
    entry_text.insert(1.0, m_decode)


# ---