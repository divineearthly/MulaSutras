#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * Urdhva Tiryagbhyam – Vertically and Crosswise
 * Multiplies two arbitrary-length non-negative integers.
 * Returns a newly allocated string. The caller must free it.
 */
char* urdhva_multiply_c(const char* a_str, const char* b_str) {
    int len_a = (int)strlen(a_str);
    int len_b = (int)strlen(b_str);
    if (len_a == 0 || len_b == 0) return strdup("0");
    if (a_str[0] == '0' || b_str[0] == '0') return strdup("0");

    int len_res = len_a + len_b;
    int* result = (int*)calloc(len_res, sizeof(int));
    if (!result) return NULL;

    for (int i = 0; i < len_a; i++) {
        for (int j = 0; j < len_b; j++) {
            int da = a_str[len_a - 1 - i] - '0';
            int db = b_str[len_b - 1 - j] - '0';
            result[i + j] += da * db;
            result[i + j + 1] += result[i + j] / 10;
            result[i + j] %= 10;
        }
    }

    // Find actual length (skip leading zeros)
    int actual_len = len_res;
    while (actual_len > 1 && result[actual_len - 1] == 0) actual_len--;

    char* out = (char*)malloc(actual_len + 1);
    if (!out) {
        free(result);
        return NULL;
    }
    for (int i = 0; i < actual_len; i++) {
        out[actual_len - 1 - i] = (char)('0' + result[i]);
    }
    out[actual_len] = '\0';
    free(result);
    return out;
}

/*
// For standalone testing (optional):
int main() {
    char* product = urdhva_multiply_c("123", "456");
    printf("%s\n", product);
    free(product);
    return 0;
}
*/
// Add this after the urdhva_multiply_c definition
void free_urdhva_string(char* str) {
    free(str);
}
