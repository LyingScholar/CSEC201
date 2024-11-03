#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};


struct linkedList {
    int size;
    struct Node* head;
};

void initialize(struct linkedList* list) {
    list -> size = 0;
    list -> head = NULL;
}

void prepend(struct linkedList* list, int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = list->head;
    list->head = newNode;
    list->size++;
}

void printList(struct linkedList* list) {
    struct Node* current = list->head; //i just used current instead of temp
    while (current != NULL) {
        printf("%d-", current->data);
        current = current->next;
    }
    printf("\n");//just used for better formatting
}

//I didn't know if you wanted me to change node itself to have a tail AND a head
//to have a both ways going linked list...

void append(struct linkedList* list, int data2) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data2;
    newNode->next = NULL;

    if (list->head == NULL) {
        list->head = newNode;
    }
    else {//lopping till i find the tail
        struct Node* current = list->head;
        while (current->next != NULL) {
            current = current->next;
        }
        current->next = newNode;
    }
    list->size++;
}

void deleteNode(struct linkedList* list, int value) {
    if (list->head == NULL) {//stops when it reaches the end
        return;
    }

    if (list->head->data == value) {//looks for the value at the head
        
        struct Node* temp = list->head;
        list->head = list->head->next;

        //free(temp);//thought this was a good idea, wasn't sure about it
        
        list->size--;
        return;
    }

    struct Node* current = list->head;
    while (current->next != NULL && current->next->data != value) { //scans the list
        current = current->next;
    }
    if (current->next != NULL) {
        
        struct Node* temp = current->next;
        current->next = current->next->next;

        //free(temp);//same thing, wasn't sure if this was required
        
        list->size--;
    }
}



void deleteAt(struct linkedList* list, int position) {//I assumed indexing begins at 0
    if (list->head == NULL || position < 0 || position >= list->size) { return; }
    if (position == 0) {//checks head
        struct Node* temp = list->head;
        list->head = list->head->next;
        
        //free(temp);
        
        list->size--;
        return;
    }

    struct Node* current = list->head; 
    for (int i = 0; i < position - 1; i++) { //scans the list till it reaches the int provided
        current = current->next;
    }

    struct Node* temp = current->next; //just reassign the node pointers, no need to delete here
    current->next = current->next->next;
    
    //free(temp); //could add if need be
    
    list->size--;
}


//this one's pretty direct
void wipeList(struct linkedList* list) {
    struct Node* current = list->head;
    while (current != NULL) {
        struct Node* temp = current;
        current = current->next;
        //free(temp);
    }
    list->head = NULL;
    list->size = 0;
}



int main() {
    struct linkedList list;
    initialize(&list);

    append(&list, 10);
    append(&list, 20);
    append(&list, 30);
    append(&list, 44);
    append(&list, 56);

    printf("Initial ");
    printList(&list);
    prepend(&list, 5);
    printf("After prepending 5: ");
    printList(&list);

    append(&list, 69);//nice
    printf("After appending 69: ");
    printList(&list);

    deleteNode(&list, 30);
    printf("After deleting node with value 30: ");
    printList(&list);


    deleteAt(&list, 2);
    printf("After deleting node at position 2: ");
    //I assumed indexing begins at 0
    printList(&list);
    wipeList(&list);
    printf("After wiping the list: ");
    printList(&list);

    return 0;
}