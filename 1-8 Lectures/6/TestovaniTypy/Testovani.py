def palindrom(text):
    cleaned_text = ''.join(c.lower() for c in text if c.isalnum())
    length = len(cleaned_text)
    for i in range(length // 2):
        if cleaned_text[i] != cleaned_text[length - 1 - i]:
            return False
    return True

def palindrom_test():
    assert palindrom('aa')
    assert not palindrom('abc')
    assert palindrom('radar')
    assert palindrom('level')
    assert not palindrom('hello')
    assert palindrom('madam')
    assert not palindrom('python')
    assert palindrom('A man a plan a canal Panama')
    assert palindrom('Able , was I saw eLba')

palindrom_test()
