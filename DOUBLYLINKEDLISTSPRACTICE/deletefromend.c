#include "lists.h"
/**
 * delete_from_end - this function deletes the last node from a list.
 * @tail: pointer to the last node
 * Return: nothing.
 */
void delete_from_end(struct node *tail)
{
	struct node *temp;
	
	if (tail == NULL)
	{
		printf("Empty list.\n");
		return;
	}
	temp = tail;
	tail->prev->next = NULL;
	tail = temp->prev;
	free(temp);
}
