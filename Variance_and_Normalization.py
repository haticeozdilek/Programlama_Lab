import random


def get_n_random_integer(n):
    random.seed(10)
    numbers = []
    for i in range(n):
        s = random.randint(-10, 10)
        numbers.append(s)
    return numbers


def get_mean_for_n_integer(numbers):
    toplam = 0
    kactane = 0
    for sayi in numbers:
        toplam += sayi
        kactane += 1
    return toplam / kactane


def get_std_for_n_integer(numbers):
    toplam = 0
    kactane = 0
    ortalama = get_mean_for_n_integer(numbers)

    for sayi in numbers:
        toplam = toplam + (sayi - ortalama) ** 2
        kactane += 1
    var_1 = toplam / (kactane - 1)
    std_1 = var_1 ** 0.5
    return std_1


def normalizasyon(numbers):
    new_numbers = []
    ortalama = get_mean_for_n_integer(numbers)
    standart_sapma = get_std_for_n_integer(numbers)
    for x in numbers:
        new_x = (x - ortalama) / standart_sapma
        new_numbers.append(new_x)
    return new_numbers


sayilar = get_n_random_integer(5)
print("sayilar: ", sayilar)
ortalama = get_mean_for_n_integer(sayilar)
print("ortalama: ", ortalama)
standart_sapma = get_std_for_n_integer(sayilar)
print("standartsapma: ", standart_sapma)
yeni_sayilar = normalizasyon(sayilar)
print("yenisayi: ", yeni_sayilar)

print(get_mean_for_n_integer(yeni_sayilar))

print(get_std_for_n_integer(yeni_sayilar))


def get_mean_one_std_neighbor_ratio(numbers):
    kacTane = 0
    toplamKacSayi = 0
    ortalama = get_mean_for_n_integer(numbers)
    standart_sapma = get_std_for_n_integer(numbers)
    low = ortalama - standart_sapma
    high = ortalama + standart_sapma

    for x in numbers:
        toplamKacSayi += 1
        if (x > low and x < high):
            kacTane = kacTane + 1
    return kacTane / toplamKacSayi


sayi1 = get_n_random_integer(100000)
print(get_mean_one_std_neighbor_ratio(sayi1))

sayi2 = [75, 32, 25, 14, 47]
length_1 = len(sayi2)
print(sayi2)
for i in range(1, length_1):
    for j in range(i, 0, -1):
        if (sayi2[j] < sayi2[j - 1]):
            temp = sayi2[j - 1]
            sayi2[j - 1] = sayi2[j]
            sayi2[j] = temp

print(sayi2)