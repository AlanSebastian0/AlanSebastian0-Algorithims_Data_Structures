import random


def bubble_sort(a_list: list) -> list:
    length = len(a_list) - 1
    for j in range(length):
        # optimisation no need to compare the end of the list as it is sorted
        for i in range(length - j):
            if a_list[i] > a_list[i + 1]:
                a_list[i], a_list[i + 1] = a_list[i + 1], a_list[i]  # swap the numbers
    return a_list


def insert_sort(a_list: list) -> list:
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i > 0 and a_list[i - 1] > value:
            a_list[i] = a_list[i - 1]
            i -= 1  # continue down the sorted part of the list
        a_list[i] = value
    return a_list


def main():
    random_list = [random.randint(1, 512) for _ in range(5000)]
    bubble_list = bubble_sort(random_list)
    insert_list = insert_sort(random_list)

    example_list = sorted(random_list)

    print(bubble_list == example_list)
    print(insert_list == example_list)


if __name__ == "__main__":
    main()
