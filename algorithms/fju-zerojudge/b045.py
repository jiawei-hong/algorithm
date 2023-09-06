import string


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)

    return text.translate(translator)


n = int(input())


for _ in range(n):
    s = remove_punctuation(input().lower()).replace(' ', '')

    print('Yes' if s == s[::-1] else 'No')
