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
	int len = 0, i, mid, *num = NULL;

	for ( ; temp; temp = temp->next)
		++len;

	num = (int *) malloc(sizeof(int) * len);
	if (!num)
	{
		printf("Memory allocation error");
		exit(1);
	}

	for (i = 0, temp = *head; temp; temp = temp->next)
		num[i++] = temp->n;

	for (mid = len / 2, i = 0; i < mid; ++i)
		if (num[i] != num[len - 1 - i])
			return (free(num), 0);

	free(num);
	}

	return (1);
}
