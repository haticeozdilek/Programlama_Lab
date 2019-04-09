# Hırsız belli bir ağırlık taşıya biliyor bu ağırlık sınırında en fazla kaç eşyayla geri döndüğü durumu veren fonk.
class Item(object):

    def __init__(self, n, v, w):
        self.name = n
        self.weight = w
        self.value = v


def maximum_object(objects, weight):
    items = []
    miktar = 0

    for i in range(len(objects)):
        temp_items = []
        amount = weight
        j = i
        while (amount >= 0 and j >= 0):

            if (amount - objects[j].weight >= 0):
                amount -= objects[j].weight
                if objects[j] not in temp_items:
                    temp_items.append(objects[j])
                j -= 1

            else:
                j -= 1
        if (len(temp_items) > miktar):
            miktar = len(temp_items)
            items = temp_items
    return items

item_1 = Item("clock", 175, 10)
item_2 = Item("Painting", 90, 9)
item_3 = Item("Radio", 20, 4)
item_4 = Item("Vase", 50, 2)
item_5 = Item("Book", 10, 1)
item_6 = Item("Computer", 200, 20)

objects = [item_1, item_2, item_3, item_4, item_5, item_6]
result = maximum_object(objects, 20)