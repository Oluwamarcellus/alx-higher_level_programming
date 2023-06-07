#include "lists.h"

/**
 *insert_node - inserts a number into a sorted singly linked list
 *@head: linked list
 *@number: new data
 *Return: new added list
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *tmp2;

	if (head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;
	if (!*head)
	{
		*head = new;
		return (new);
	}
	tmp = *head;
	while (tmp != NULL && tmp->next != NULL)
	{
		if (tmp->next->n >= number)
			break;
		tmp = tmp->next;
	}
	tmp2 = tmp->next;
	tmp->next = new;
	new->next = tmp2;
	return (new);
}
