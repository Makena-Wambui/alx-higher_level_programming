#include "lists.h"
/**
 * creation - this function creates a node of a doubly linked list
 * Return: nothing
 */

void creation(void)
{
	struct node *head, *newnode, *temp;
	int choice = 1;

	while (choice)
	{
	newnode = malloc(sizeof(struct node));
	if (newnode == NULL)
	{
		printf("Malloc failure.\n");
		return;
	}
	printf("Enter your data: \n");
	scanf("%d", &newnode->data);
	newnode->next = NULL;
	newnode->prev = NULL;
	if (head == NULL)
	{
		head = temp = newnode;
	}
	else
	{
		temp->next = newnode;
		newnode->prev = temp;
		temp = newnode;
	}
	printf("Do you want to continue? \n");
	scanf("%d", &choice);
	}
}
