#include "lists.h"
/**
 * check_cycle - checks if a single linked list has cycle
 * @list: the single linked list
 * Return: 0 or 1
 */
int check_cycle(listint_t *list)
{
	listint_t *a = list, *b = list;

	if (!list)
		return (0);
	while (a->next && b->next->next)
	{
		b = b->next->next;
		a = a->next;
		if (a == b)
			return (1);
	}
	return (0);
}
