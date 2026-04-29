#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>

/**
 * Urdhva Tiryagbhyam – Vertically and Crosswise
 * Parallel, iterative grid multiplier. Handles any length.
 * Returns a newly allocated string; free with free_urdhva_string().
 */
char* urdhva_multiply_c(const char* a_str, const char* b_str) {
    int len_a = (int)strlen(a_str);
    int len_b = (int)strlen(b_str);
    if (len_a == 0 || len_b == 0) return strdup("0");
    if (a_str[0] == '0' || b_str[0] == '0') return strdup("0");

    int len_res = len_a + len_b;
    int* result = (int*)calloc(len_res, sizeof(int));
    if (!result) return NULL;

    // Get the number of available threads
    int num_threads = omp_get_max_threads();

    // Per-thread local arrays to avoid atomic operations
    int** local = (int**)malloc(num_threads * sizeof(int*));
    for (int t = 0; t < num_threads; t++) {
        local[t] = (int*)calloc(len_res, sizeof(int));
    }

    // Parallel region: each thread accumulates into its own local array
    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        #pragma omp for collapse(2)
        for (int i = 0; i < len_a; i++) {
            for (int j = 0; j < len_b; j++) {
                int da = a_str[len_a - 1 - i] - '0';
                int db = b_str[len_b - 1 - j] - '0';
                local[tid][i + j] += da * db;
            }
        }
    }

    // Merge all thread-local arrays into the main result array
    for (int t = 0; t < num_threads; t++) {
        for (int i = 0; i < len_res; i++) {
            result[i] += local[t][i];
        }
        free(local[t]);
    }
    free(local);

    // Single-threaded carry propagation
    for (int i = 0; i < len_res - 1; i++) {
        result[i + 1] += result[i] / 10;
        result[i] %= 10;
    }

    // Remove leading zeros
    int actual_len = len_res;
    while (actual_len > 1 && result[actual_len - 1] == 0) actual_len--;

    // Convert to string
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

/**
 * Free a string allocated by urdhva_multiply_c.
 */
void free_urdhva_string(char* str) {
    free(str);
}
