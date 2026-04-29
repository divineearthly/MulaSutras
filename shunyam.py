#!/usr/bin/env python3
"""
Shunyam Saamyasamuccaye - Lossless compressor (Termux-friendly)
Finds the longest repeated substring by scanning lengths.
"""

def find_longest_repeated_substring(s: str):
    """Return longest substring appearing at least twice, and its length."""
    n = len(s)
    if n < 2:
        return None, 0
    # Start from the longest possible repeat and go down
    # To keep it fast, limit to 200 chars max
    max_len = min(n // 2, 200)
    for length in range(max_len, 2, -1):
        seen = set()
        for i in range(n - length + 1):
            sub = s[i:i + length]
            if sub in seen:
                # Found a repeat at this length
                return sub, length
            seen.add(sub)
    return None, 0

def shunyam_compress(text: str) -> tuple:
    compressed = text
    dictionary = {}
    symbol_index = 0
    while True:
        sub, length = find_longest_repeated_substring(compressed)
        if sub is None or len(sub) <= 2:
            break
        marker = f"~{symbol_index}~"
        # Replace the second occurrence (and all further ones) with marker
        first_pos = compressed.find(sub)
        second_pos = compressed.find(sub, first_pos + 1)
        if second_pos == -1:
            break
        compressed = compressed[:second_pos] + marker + compressed[second_pos + len(sub):]
        dictionary[marker] = sub
        symbol_index += 1
    return compressed, dictionary

def shunyam_decompress(compressed: str, dictionary: dict) -> str:
    text = compressed
    for marker, original in dictionary.items():
        text = text.replace(marker, original, 1)
    return text

if __name__ == "__main__":
    import sys
    if len(sys.argv) == 2:
        with open(sys.argv[1], 'r') as f:
            original = f.read()
        print(f"Original size: {len(original)} bytes")
        comp, d = shunyam_compress(original)
        print(f"Compressed size: {len(comp)} bytes")
        ratio = (1 - len(comp)/len(original))*100 if original else 0
        print(f"Compression: {ratio:.2f}%")
        restored = shunyam_decompress(comp, d)
        assert restored == original, "Lossless check failed!"
        print("Integrity: ✅")
    else:
        print("Usage: python shunyam.py <file>")
        sample = "the rain in spain falls mainly in the plain in spain"
        print(f"Demo: '{sample}'")
        c, d = shunyam_compress(sample)
        print(f"Compressed: '{c}'")
        print(f"Dictionary: {d}")
