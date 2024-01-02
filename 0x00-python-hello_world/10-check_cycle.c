#include <stddef.h>

struct listint {
    int data;
    struct listint *next;
};

typedef struct listint listint_t;

/**
 * check_cycle - Checking for a cycle in a link list
 * @list: A pointer to the head of the linked list.
 *
 * Return: 1 if there is a cycle, 0 if there is no cycle.
 */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	if (list == NULL || list->next == NULL)
	{
		return 0;
	}
	slow = list;
	fast = list->next;

	while (fast != NULL && fast->next != NULL)
	{
		if (slow == fast)
		{
			return 1;
		}

	slow = slow->next;
	fast = fast->next->next;
	}

	return 0;
}
