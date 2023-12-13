#include "lists.h"
/**
 * add_at_beg - this function adds a node at the beginning
 * of a doubly linked list
 * @head: pointer to the first node in the list
 * Return: newnode, a pointer to the newly added node
 */
struct node *add_at_beg(struct node *head)
{
	struct node *newnode;

	newnode = malloc(sizeof(struct node));
	if (newnode == NULL)
	{
		printf("Malloc failure.\n");
		return (NULL);
	}
	newnode->prev = NULL;
	newnode->next = head;
	if (head != NULL)
	{
	head->prev = newnode;
	}
	head = newnode;

	return (newnode);
}
