#include "lists.h"
/**
 * display_and_count - this function displays and counts the number
 * of elements in a doubly linked list
 * Return: total number of elements.
 */

size_t display_and_count(void)
{
	struct node *head, *temp;
	size_t total;

	temp = head;
	total = 0;
	while (temp != NULL)
	{
		printf("%d\n", temp->data);
		temp = temp->next;
		total++;
	}
	return (total);
}
