#include <stdio.h>
#include <stdlib.h>

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow = *head, *fast = *head, *prev = NULL, *temp;

	if (*head == NULL || (*head)->next == NULL)
	{
		return (1);
	}

	while (fast != NULL && fast->next != NULL)
	{
		fast = fast->next->next;

		temp = slow->next;
		slow->next = prev;
		prev = slow;
	slow = temp;
	}

	if (fast != NULL)
	{
		slow = slow->next;
	}

	while (slow != NULL)
	{
		if (slow->n != prev->n)
		{
			return (0);
		}

		slow = slow->next;
		prev = prev->next;
	}

	return (1);
}
