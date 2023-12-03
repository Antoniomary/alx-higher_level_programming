#include "lists.h"

/**
 * is_palindrome - a function in C that checks if a singly linked list is
 * a palindrome.
 * @head:  double pointer to head node.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	if (*head && (*head)->next)
	{
	listint_t *temp = *head;
	listint_t *ptr1, *ptr2;

	ptr1 = ptr2 = *head;
	while (ptr2 && ptr2->next)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
	}

	if (ptr2)
		ptr1 = ptr1->next;

	temp = ptr1;
	ptr2 = NULL;
	ptr1 = ptr1->next;
	while (ptr1)
	{
		temp->next = ptr2;
		ptr2 = ptr1;
		ptr1 = ptr1->next;
	}
	temp = ptr2;
	ptr1 = *head;

	while (temp && ptr1)
	{
		if (temp->n != ptr1->n)
			return (0);
		temp =temp->next;
		ptr1 = ptr1->next;
	}
	}

	return (1);
}
