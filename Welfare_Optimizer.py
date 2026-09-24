#include <stdio.h>
#include <stdlib.h>
typedef struct Node 
{
    int coeff;          // Coefficient of the term
    int power;          // Power of the term
    struct Node *next;  // Pointer to the next term
} Node;
// Function to create a new node
Node* createNode(int coeff, int power) 
{
    Node *newNode = (Node*)malloc(sizeof(Node));
    if (newNode == NULL) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    newNode->coeff = coeff;
    newNode->power = power;
    newNode->next = NULL;
    return newNode;
}
// Function to insert a term into the polynomial
void insertTerm(Node **head, int coeff, int power) {
    Node *newTerm = createNode(coeff, power);
    if (*head == NULL) {
        *head = newTerm;
    } else {
        Node *temp = *head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        temp->next = newTerm;
    }
}
// Function to add two polynomials
Node* addPolynomials(Node *poly1, Node *poly2) 
{
    Node *result = NULL;
    Node *temp1 = poly1;
    Node *temp2 = poly2;
    while (temp1 != NULL && temp2 != NULL)
    {
        if (temp1->power > temp2->power) {
            insertTerm(&result, temp1->coeff, temp1->power);
            temp1 = temp1->next;
        }
        else if (temp1->power < temp2->power) {
            insertTerm(&result, temp2->coeff, temp2->power);
            temp2 = temp2->next;
        } 
        else 
        {
            insertTerm(&result, temp1->coeff + temp2->coeff, temp1->power);
            temp1 = temp1->next;
            temp2 = temp2->next;
        }
    }
    // Adding remaining terms of poly1
    while (temp1 != NULL) {
        insertTerm(&result, temp1->coeff, temp1->power);
        temp1 = temp1->next;
    }
    // Adding remaining terms of poly2
    while (temp2 != NULL) {
        insertTerm(&result, temp2->coeff, temp2->power);
        temp2 = temp2->next;
    }
    return result;
}
// Function to display a polynomial
void displayPolynomial(Node *poly)
    {
    if (poly == NULL) {
        printf("Polynomial is empty.\n");
        return;
    }
    Node *temp = poly;
    while (temp != NULL)
    {
        printf("%dx^%d ", temp->coeff, temp->power);
        if (temp->next != NULL)
            printf("+ ");
        temp = temp->next;
    }
    printf("\n");
}

// Function to free the memory allocated for a polynomial
void freePolynomial(Node *poly) {
    Node *temp;
    while (poly != NULL) {
        temp = poly;
        poly = poly->next;
        free(temp);
    }
}
int main()
{
    Node *poly1 = NULL;
    Node *poly2 = NULL;
    Node *result = NULL;

    // Inserting terms into polynomial 1
    insertTerm(&poly1, 3, 2);
    insertTerm(&poly1, 5, 1);
    insertTerm(&poly1, 2, 0);

    // Inserting terms into polynomial 2
    insertTerm(&poly2, 4, 3);
    insertTerm(&poly2, 2, 1);
    insertTerm(&poly2, 1, 0);

    printf("Polynomial 1: ");
    displayPolynomial(poly1);

    printf("Polynomial 2: ");
    displayPolynomial(poly2);

    result = addPolynomials(poly1, poly2);
    printf("Result of addition: ");
    displayPolynomial(result);

    // Freeing memory allocated for polynomials
    freePolynomial(poly1);
    freePolynomial(poly2);
    freePolynomial(result);

    return 0;
}
output:
Polynomial 1: 3x^2 + 5x^1 + 2x^0 

Polynomial 2: 4x^3 + 2x^1 + 1x^0 

Result of addition: 4x^3 + 3x^2 + 7x^1 + 3x^0 

