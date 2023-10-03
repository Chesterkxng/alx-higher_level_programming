#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
/**
 * *insert_node - insert a node in a sorted linked list
 * @head: linked list
 * @number: number to insert
 * Return: a pointer to the linked list
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *cursor, *step_back;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL || !head)
		return (NULL);
	new_node->n = number;
	if (!*head || (*head)->n >= number)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}
	cursor = *head;
	while (cursor != NULL && cursor->n < number)
	{
		step_back = cursor;
		cursor = cursor->next;
	}
	step_back->next =  new_node;
	new_node->next = cursor;
	return (new_node);
}
