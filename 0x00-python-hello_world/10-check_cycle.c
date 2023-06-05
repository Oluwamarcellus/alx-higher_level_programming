#include "lists.h"

/**
 *check_cycle - checks if a singly linked list has a cycle in it
 *@list: linked list
 *Return: 0 or 1
 */

int check_cycle(listint_t *list)
{
	listint_t *fast;

	fast = list;
	while (list != NULL && fast != NULL)
	{
		list = list->next;
		fast = fast->next->next;
		if (list == fast)
			return (1);
	}
	return (0);
}
