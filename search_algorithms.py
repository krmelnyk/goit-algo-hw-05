# search_algorithms.py

def kmp_search(text: str, pattern: str) -> int:
    if not pattern:
        return 0

    lps = _build_lps(pattern)
    i = j = 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == len(pattern):
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return -1


def _build_lps(pattern: str):
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1

    return lps


def rabin_karp_search(text: str, pattern: str) -> int:
    if not pattern:
        return 0

    base = 256
    prime = 101

    m = len(pattern)
    n = len(text)

    if m > n:
        return -1

    pattern_hash = 0
    text_hash = 0
    h = 1

    for _ in range(m - 1):
        h = (h * base) % prime

    for i in range(m):
        pattern_hash = (base * pattern_hash + ord(pattern[i])) % prime
        text_hash = (base * text_hash + ord(text[i])) % prime

    for i in range(n - m + 1):
        if pattern_hash == text_hash:
            if text[i:i + m] == pattern:
                return i

        if i < n - m:
            text_hash = (
                base * (text_hash - ord(text[i]) * h) + ord(text[i + m])
            ) % prime

            if text_hash < 0:
                text_hash += prime

    return -1


def boyer_moore_search(text: str, pattern: str) -> int:
    if not pattern:
        return 0

    bad_char = _build_bad_char_table(pattern)
    m = len(pattern)
    n = len(text)

    shift = 0

    while shift <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[shift + j]:
            j -= 1

        if j < 0:
            return shift
        else:
            shift += max(1, j - bad_char.get(text[shift + j], -1))

    return -1


def _build_bad_char_table(pattern: str):
    table = {}
    for i, char in enumerate(pattern):
        table[char] = i
    return table
