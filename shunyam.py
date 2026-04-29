#!/usr/bin/env python3
"""
Shunyam Saamyasamuccaye (When the sum is the same, that sum is zero)
A Vedic lossless data compressor based on repeated pattern cancellation.
"""

def find_longest_repeated_substring(s: str):
    n = len(s)
    longest = ""
    for length in range(1, n):
        seen = {}
        for i in range(n - length + 1):
            sub = s[i:i + length]
            if sub in seen:
                if length > len(longest):
                    longest = sub
            else:
                seen[sub] = i
    return longest if longest else None, len(longest)


def shunyam_compress(text: str) -> tuple:
    compressed = text
    dictionary = {}
    symbol_index = 0
    while True:
        sub, length = find_longest_repeated_substring(compressed)
        if sub is None or len(sub) <= 2:
            break
        marker = f"~{symbol_index}~"
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
        print(f"Dictionary entries: {len(d)}")
        ratio = (1 - len(comp) / len(original)) * 100 if original else 0
        print(f"Compression ratio: {ratio:.2f}%")
        restored = shunyam_decompress(comp, d)
        assert restored == original, "Lossless check failed!"
        print("Lossless integrity: ✅ verified")
    else:
        print("Usage: python shunyam.py <filename>")
        sample = "the rain in spain falls mainly in the plain in spain"
        print(f"\nDemo on: '{sample}'")
        c, d = shunyam_compress(sample)
        print(f"Compressed: '{c}'")
        print(f"Dictionary: {d}")
        print(f"Restored: '{shunyam_decompress(c, d)}'")
