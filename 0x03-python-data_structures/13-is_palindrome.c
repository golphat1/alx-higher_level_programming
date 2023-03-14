#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/* Definition of a singly linked list node */
typedef struct listint_s {
    int n;
    struct listint_s *next;
} listint_t;

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to the head of the list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 *         An empty list is considered a palindrome.
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;
    listint_t *next = NULL;

    /* Find the middle of the list and reverse the first half */
    while (fast != NULL && fast->next != NULL) {
        fast = fast->next->next;
        next = slow->next;
        slow->next = prev;
        prev = slow;
        slow = next;
    }

    /* Adjust the middle pointer for odd-length lists */
    if (fast != NULL)
        slow = slow->next;

    /* Compare the reversed first half with the second half */
    while (prev != NULL && slow != NULL) {
        if (prev->n != slow->n)
            return 0;
        prev = prev->next;
        slow = slow->next;
    }

    return 1;
}

/* Example usage */
int main(void)
{
    listint_t *head = NULL;

    /* Create a list with the values 1, 2, 3, 2, 1 */
    listint_t *node1 = malloc(sizeof(listint_t));
    listint_t *node2 = malloc(sizeof(listint_t));
    listint_t *node3 = malloc(sizeof(listint_t));
    listint_t *node4 = malloc(sizeof(listint_t));
    listint_t *node5 = malloc(sizeof(listint_t));
    node1->n = 1;
    node1->next = node2;
    node2->n = 2;
    node2->next = node3;
    node3->n = 3;
    node3->next = node4;
    node4->n = 2;
    node4->next = node5;
    node5->n = 1;
    node5->next = NULL;
    head = node1;

    /* Test the function */
    printf("%d\n", is_palindrome(&head));  // Output: 1

    /* Free the memory */
    free(node1);
    free(node2);
    free(node3);
    free(node4);
    free(node5);

    return 0;
}
