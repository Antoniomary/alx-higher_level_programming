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
	listint_t *temp, *slow, *fast, *prev;

	prev = slow = fast = *head;
	temp = NULL;
	/* move to the first half of list and reverse it while moving */
	while (fast && fast->next)
	{
		fast = fast->next->next;
		prev = slow;
		slow = slow->next;
		prev->next = temp;
		temp = prev;
	}

	/* if the list is odd, we move one node forward */
	if (fast)
		slow = slow->next;

	while (temp && slow)
	{
		if (temp->n != slow->n)
			return (0);
		temp =temp->next;
		slow = slow->next;
	}
	}

	return (1);
}
