#include "lists.h"
/**
 * check_cycle - checks if a single linked list has cycle
 * @list: the single linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *a, *b;

	if (!list)
		return (0);
	a = list;
	b = list;
	while (a->next != NULL && b->next->next != NULL)
	{
		b = b->next->next;
		a = a->next;

		if (a == b)
			return (1);
	}
	return (0);
}
