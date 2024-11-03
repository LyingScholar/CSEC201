#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FILENAME 256
#define BUFFER_SIZE 1024

void xor_encrypt_decrypt(FILE *key_file, FILE *input_file, FILE *output_file);
int get_mode();
void get_filename(char *prompt, char *filename);



int main() {
    char key_filename[MAX_FILENAME];
    char plaintext_filename[MAX_FILENAME];
    char ciphertext_filename[MAX_FILENAME];
    FILE *key_file, *input_file, *output_file;
    int mode;

    mode = get_mode();
    get_filename("Enter the filename containing the encryption key: ", key_filename);
    get_filename("Enter the filename for the plain text: ", plaintext_filename);
    get_filename("Enter the filename for the cipher text: ", ciphertext_filename);

    key_file = fopen(key_filename, "rb");
    if (key_file == NULL) {
        fprintf(stderr, "Error opening key file.\n");
        exit(1);
    }

    if (mode == 1) {
        input_file = fopen(plaintext_filename, "rb");
        output_file = fopen(ciphertext_filename, "wb");
    } else {
        input_file = fopen(ciphertext_filename, "rb");
        output_file = fopen(plaintext_filename, "wb");
    }

    if (input_file == NULL || output_file == NULL) {
        fprintf(stderr, "Error opening input or output file.\n");
        exit(1);
    }

    xor_encrypt_decrypt(key_file, input_file, output_file);

    fclose(key_file);
    fclose(input_file);
    fclose(output_file);


    printf("Operation completed successfully.\n");

    return 0;
}

void xor_encrypt_decrypt(FILE *key_file, FILE *input_file, FILE *output_file) {
    unsigned char key_buffer[BUFFER_SIZE];
    unsigned char input_buffer[BUFFER_SIZE];
    unsigned char output_buffer[BUFFER_SIZE];
    size_t key_bytes, input_bytes;
    size_t i, j;

    key_bytes = fread(key_buffer, 1, BUFFER_SIZE, key_file);

    while ((input_bytes = fread(input_buffer, 1, BUFFER_SIZE, input_file)) > 0) {
        for (i = 0, j = 0; i < input_bytes; i++, j++) {
            if (j >= key_bytes) {
                j = 0;
            }
            output_buffer[i] = input_buffer[i] ^ key_buffer[j];
        }
        fwrite(output_buffer, 1, input_bytes, output_file);
    }
}

int get_mode() {
    int mode;
    printf("Select mode of operation:\n");
    printf("1. Encrypt\n");
    printf("2. Decrypt\n");
    printf("Enter your choice (1 or 2): ");
    scanf("%d", &mode);
    while (getchar() != '\n');

    if (mode != 1 && mode != 2) {
        fprintf(stderr, "Invalid mode selected. Exiting.\n");
        exit(1);
    }

    return mode;
}



void get_filename(char *prompt, char *filename) {
    printf("%s", prompt);
    fgets(filename, MAX_FILENAME, stdin);
    filename[strcspn(filename, "\n")] = 0;
}