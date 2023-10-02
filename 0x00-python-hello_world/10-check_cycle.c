#include "lists.h"

/**
 * check_cycle - check for a cycle
 * @list: list
 * Return: 0 if any cycle
 * 1 othewise
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare, *head;

	head = list;
	turtle = head;
	hare = head;

	if (!list || !turtle->next || !turtle->next->next)
		return (0);
	do {
		turtle = turtle->next;
		if (hare && hare->next)
			hare = hare->next->next;
	} while (hare != turtle && hare);
	if (!hare)
		return (0);
	return (1);
}
