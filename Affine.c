#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define ALPHABET_SIZE 26


int main() {
    char modeOfOperation[20], keyFile[100], plainFile[100], cipherFile[100];
    int a, b;
    FILE *key_fp, *input_fp, *output_fp;

    printf("Enter mode of operation: ");
    scanf("%s", modeOfOperation);

    printf("Enter the encryption key location: ");
    scanf("%s", keyFile);

    printf("Enter the plain text location: ");
    scanf("%s", plainFile);

    printf("Enter the cipher text location: ");
    scanf("%s", cipherFile);

    key_fp = fopen(keyFile, "r");
    if (key_fp == NULL) {
        printf("Error opening key file.\n");
        return 1;
    }
    fscanf(key_fp, "%d %d", &a, &b);
    fclose(key_fp);

    if (strcmp(modeOfOperation, "encrypt") == 0) {
        input_fp = fopen(plainFile, "r");
        output_fp = fopen(cipherFile, "w");
    } else if (strcmp(modeOfOperation, "decrypt") == 0) {
        input_fp = fopen(cipherFile, "r");
        output_fp = fopen(plainFile, "w");
    } else {
        printf("Invalid mode. Please enter 'encrypt' or 'decrypt'.\n");
        return 1;
    }

    if (input_fp == NULL || output_fp == NULL) {
        printf("Error opening input or output file.\n");
        return 1;
    }

    
    if (strcmp(modeOfOperation, "encrypt") == 0) {
        encrypt(input_fp, output_fp, a, b);
        printf("Encryption completed.\n");
    } else {
        decrypt(input_fp, output_fp, a, b);
        printf("Decryption completed.\n");
    }

    fclose(input_fp);
    fclose(output_fp);

    return 0;
}

void encrypt(FILE *input, FILE *output, int a, int b) {
    int ch;
    while ((ch = fgetc(input)) != EOF) {
        if (isalpha(ch)) {
            char base = isupper(ch) ? 'A' : 'a';
            ch = ((a * (ch - base) + b) % ALPHABET_SIZE + ALPHABET_SIZE) % ALPHABET_SIZE;
            fputc(ch + base, output);
        } else {
            fputc(ch, output);
        }
    }
}

void decrypt(FILE *input, FILE *output, int a, int b) {
    int a_inv = mod_inverse(a, ALPHABET_SIZE);
    int ch;
    while ((ch = fgetc(input)) != EOF) {
        if (isalpha(ch)) {
            char base = isupper(ch) ? 'A' : 'a';
            ch = ((a_inv * ((ch - base - b + ALPHABET_SIZE) % ALPHABET_SIZE)) % ALPHABET_SIZE + ALPHABET_SIZE) % ALPHABET_SIZE;
            fputc(ch + base, output);
        } else {
            fputc(ch, output);
        }
    }
}

int mod_inverse(int a, int m) {
    a = a % m;
    for (int x = 1; x < m; x++)
        if ((a * x) % m == 1)
            return x;
    return 1;
}