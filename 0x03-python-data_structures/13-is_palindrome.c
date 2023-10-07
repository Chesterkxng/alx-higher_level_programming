#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * is_palindrome - a function that check
 * @head: listint_t
 * Return: 0 if not 1 if
 */
int is_palindrome(listint_t **head)
{
	size_t length = 0, i = 0, j;
	listint_t *cursor = *head;
	int array[64] = {0};

	if (*head == NULL)
		return (1);
	while (cursor)
	{
		length++;
		array[i] = cursor->n;
		cursor =  cursor->next;
		i++;
	}
	for (j = 0; j < length / 2; j++)
	{
		if (array[j] != array[length - j - 1])
		{
			return (0);
		}
	}
	return (1);
}
