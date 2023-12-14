#include "lists.h"
/**
 * deleteatbeginning - this function deletes a node at the beginning of a list.
 * @head: pointer to head node
 * Return: nothing.
 */
void deleteatbeginning(struct node *head)
{
	struct node *temp;

	temp = head;
	if (head == NULL)
	{
		printf("Empty list.\n");
		return;
	}
	else
	{
		head = head->next;
		head->prev = 0;
		temp->next = 0;
		free(temp);
	}
}
