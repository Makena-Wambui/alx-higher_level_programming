#ifndef LISTS_H
#define LISTS_H
#include <stdio.h>
#include <stdlib.h>
struct node
{
	int data;
	struct node *next;
	struct node *prev;
};
void creation(void);
size_t display_and_count(void);
struct node *add_at_beg(struct node *head);
void deleteatbeginning(struct node *head);
void delete_from_end(struct node *tail);







#endif
