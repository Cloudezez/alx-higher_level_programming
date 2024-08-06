#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: pointer to the head of the list
 * Return: 1 if there is a cycle, 0 otherwise
 */
int check_cycle(listint_t *list)
{
    listint_t *slow = list;
    listint_t *fast = list;

    while (fast != NULL && fast->next != NULL)
    {
        slow = slow->next;        /* Move slow pointer by 1 step */
        fast = fast->next->next;  /* Move fast pointer by 2 steps */

        if (slow == fast)
            return (1);  /* There is a cycle */
    }

    return (0);  /* No cycle */
}

