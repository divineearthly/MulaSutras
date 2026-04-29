#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <omp.h>

char* urdhva_multiply_c(const char* a, const char* b) {
    int la = (int)strlen(a), lb = (int)strlen(b);
    if (la == 0 || lb == 0) return strdup("0");
    if (strcmp(a, "0") == 0 || strcmp(b, "0") == 0) return strdup("0");

    int len_res = la + lb;
    int* result = (int*)calloc(len_res, sizeof(int));
    if (!result) return NULL;

    int nt = omp_get_max_threads();
    int** local = (int**)malloc(nt * sizeof(int*));
    for (int t = 0; t < nt; t++) local[t] = (int*)calloc(len_res, sizeof(int));

    #pragma omp parallel
    {
        int tid = omp_get_thread_num();
        #pragma omp for collapse(2)
        for (int i = 0; i < la; i++)
            for (int j = 0; j < lb; j++) {
                int da = a[la-1-i] - '0';
                int db = b[lb-1-j] - '0';
                local[tid][i+j] += da * db;
            }
    }
    for (int t = 0; t < nt; t++) {
        for (int i = 0; i < len_res; i++) result[i] += local[t][i];
        free(local[t]);
    }
    free(local);
    for (int i = 0; i < len_res-1; i++) {
        result[i+1] += result[i] / 10;
        result[i] %= 10;
    }
    int act = len_res;
    while (act > 1 && result[act-1] == 0) act--;
    char* out = (char*)malloc(act + 1);
    for (int i = 0; i < act; i++) out[act-1-i] = (char)('0' + result[i]);
    out[act] = '\0';
    free(result);
    return out;
}

void free_urdhva_string(char* str) { free(str); }
