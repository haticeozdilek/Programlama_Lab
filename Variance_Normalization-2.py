import random


def get_n_random_integer(n):
    numbers = []
    for i in range(n):
        s = random.randint(-100, 100)
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
print("sayilar:", sayilar)
ortalama = get_mean_for_n_integer(sayilar)
print("ortalama:", ortalama)
standart_sapma = get_std_for_n_integer(sayilar)
print("standart sapma:", standart_sapma)
yeni_sayilar = normalizasyon(sayilar)
print("yenisayi:", yeni_sayilar)

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


sayilar_1 = get_n_random_integer(100000)
print(get_mean_one_std_neighbor_ratio(sayilar_1))

sayilar_2 = [75, 32, 25, 14, 47]


def insertion(numbers):
    sayilar_2 = numbers
    karsilastirma_sayisi = 0
    yerdegistirme_sayisi = 0
    length_1 = len(sayilar_2)

    for i in range(1, length_1):

        for j in range(i, 0, -1):

            karsilastirma_sayisi += 1

            if (sayilar_2[j] < sayilar_2[j - 1]):

                yerdegistirme_sayisi += 1
                temp = sayilar_2[j - 1]
                sayilar_2[j - 1] = sayilar_2[j]
                sayilar_2[j] = temp
            else:
                break

    return sayilar_2, karsilastirma_sayisi, yerdegistirme_sayisi


sayilar_1 = get_n_random_integer(10)
sayilar_2 = insertion(sayilar_1)
print("siralanmis dizi:  ", sayilar_2[0])
print("karsilastirma sayisi:  ", sayilar_2[1])
print("yerdegistirme sayisi:  ", sayilar_2[2])


def get_mean_of_swap_in_insertion(numTrials, numInt):
    swap_sayisi = []
    for i in range(numTrials):
        sayilar_1 = get_n_random_integer(numInt)
        sayilar_2 = insertion(sayilar_1)
        s_1 = sayilar_2[2]
        swap_sayisi.append(s_1)

    mean_1 = get_mean_for_n_integer(swap_sayisi)
    std_1 = get_std_for_n_integer(swap_sayisi)

    return numInt, int(mean_1), int(std_1)


print(get_mean_of_swap_in_insertion(10, 1000))


def bubbleSort(arr):
    n = len(arr)
    karsilastirma_sayisi = 0
    yerdegistime_sayisi = 0

    for i in range(n):

        for j in range(0, n - i - 1):
            karsilastirma_sayisi += 1

            if arr[j] > arr[j + 1]:
                yerdegistime_sayisi += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return yerdegistime_sayisi


sayilar_1 = get_n_random_integer(10)
print(sayilar_1)
swap_sayisi = bubbleSort(sayilar_1)
print(sayilar_1)
print(swap_sayisi)


def get_mean_of_swap_in_bubble(numTrials, numInt):
    swap_sayilari = []
    for i in range(numTrials):
        sayilar_1 = get_n_random_integer(numInt)
        s_1 = sayilar_2 = bubbleSort(sayilar_1)
        swap_sayilari.append(s_1)

    mean_1 = get_mean_for_n_integer(swap_sayilari)
    std_1 = get_std_for_n_integer(swap_sayilari)

    return numInt, int(mean_1), int(std_1)


print(get_mean_of_swap_in_bubble(10, 1000))

random.seed(42)
result_1 = get_mean_of_swap_in_insertion(10, 10)
random.seed(42)
result_2 = get_mean_of_swap_in_bubble(10, 10)

print("insertion: ", result_1)
print("bubble:  ", result_2)