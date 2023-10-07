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
	int length = 0, i = 0, j;
	listint_t *cursor = *head;
	int *array;

	if (*head == NULL)
		return (1);
	array = malloc(sizeof(int) * 1024);
	if (!array)
		return (0);
	cursor = *head;
	while (cursor)
	{
		array[i] = cursor->n;
		length++;
		cursor = cursor->next;
		i++;
	}
	for (j = 0; j < length / 2; j++)
	{
		if (array[j] != array[length - j - 1])
		{
			free(array);
			return (0);
		}
	}
	free(array);
	return (1);
}
