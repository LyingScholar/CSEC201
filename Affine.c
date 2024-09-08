#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
    char modeOfOperation[20], keyFile[100], plainFile[100], cipherFile[100];
    int a, b;

    printf("Enter mode of operation: ");
    scanf("%s", modeOfOperation);

    printf("Enter the encryption key location: ");
    scanf("%s", keyFile);

    printf("Enter the plain text location: ");
    scanf("%s", plainFile);

    printf("Enter the cipher text location: ");
    scanf("%s", cipherFile);



    return 0;
}