#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - a function that inserts a number into a
 * sorted singly linked list.
 * @head: double pointer to head node of the singly linked list.
 * @number: the number to insert.
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new = NULL, *temp = *head;

	new = malloc(sizeof(listint_t));
	if (!new)
		return (NULL);

	new->n = number, new->next = NULL;

	if (*head == NULL) /* the list is empty */
		*head = new;
	else /* list is not empty */
	{
		/* checks if number to add is the smallest so as to put it at beginning */
		if ((*head)->n > number)
		{
			new->next = *head;
			*head = new;
		}
		else /* number to add is not the smallest */
		{
			/* traverse the list */
			while (temp->next)
			{
				/* means the position to insert is not at end */
				if (temp->next->n > number)
				{
					new->next = temp->next;
					temp->next = new;
					return (new);
				}
				temp = temp->next;
			}

			/* means position to add is at end */
			temp->next = new;
		}
	}

	return (new);
}
