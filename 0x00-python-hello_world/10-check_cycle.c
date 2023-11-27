#include "lists.h"

/**
 * check_cycle - a function that checks if a singly linked list has a cycle.
 * @list: the head node of the singly linked list to check.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	while (temp && list && list->next)
	{
		temp = temp->next;
		list = list->next->next;

		if (temp == list)
			return (1);
	}

	return (0);
}
