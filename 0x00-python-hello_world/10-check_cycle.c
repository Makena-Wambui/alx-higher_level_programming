#include "lists.h"
/**
 * check_cycle - this function checks for a loop in a linked list
 * @list: pointer to node
 * Return: 1 if cycle found, otherwise 0.
 */

int check_cycle(listint_t *list)
{
	/*introduce 2 pointers temp and ptr*/
	listint_t *temp = list;
	listint_t *ptr = list;
	/*all of these pointers point to the first node*/

	/**
	 * introduce a while loop
	 * where temp, ptr, list are not null.
	 * if they are then it means there is no cycle
	 */
	while (temp && ptr && ptr->next)
	{
		/*temp moves forward by one position*/
		temp = temp->next;
		/*ptr moves forward by two positions*/
		ptr = ptr->next->next;
		/*if temp equals to ptr then a cycle has been encountered*/
		if (temp == ptr)
			return (1);
	}
	return (0);
}
