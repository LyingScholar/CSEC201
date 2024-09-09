#include <stdio.h>
#include <stdlib.h>
#include <string.h>


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