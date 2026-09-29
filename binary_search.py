# Given a list of sorted words write a function that performs a binary search for a word and returns wheter it is in the list
def main():
    word_list = ["apple","banana","orange","laptop","knife","fire","exist","microwave","long", "shot",]
    word_list.sort()
    print(word_list)
    chosen_word = input("Please enter a word: ")
    was_found = binary_search_word(word_list, chosen_word)
    print("That word was found") if was_found else print("That word was not found")


def binary_search_word(words: list, target: str) -> bool:
    right = len(words)-1
    left = 0
    while left <= right:
        mid = (right+left) // 2 #middle of the list
        mid_case = words[mid]
        if mid_case == target:
            return True
        elif target > mid_case:
            left = mid+1

        else: #target < mid_case
            right = mid-1
    return False

if __name__ == "__main__":
    main()
