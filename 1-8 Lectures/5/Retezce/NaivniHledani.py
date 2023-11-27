def naive_search(needle, haystack):
    needle_len = len(needle)
    haystack_len = len(haystack)

    for i in range(haystack_len - needle_len + 1):
        if haystack[i:i + needle_len] == needle:
            return i

    return -1

# Příklad použití
haystack = "ababcababcabc"
needle = "abc"

result = naive_search(needle, haystack)

if result != -1:
    print(f"Podřetězec '{needle}' byl nalezen na pozici {result}.")
else:
    print(f"Podřetězec '{needle}' nebyl nalezen v řetězci.")
