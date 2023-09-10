#include "lists.h"
/**
 * is_palindrome - return if its palindrome or not
 * @head: head list
 * @end: end list
 * Return: 0 if its not palind 1 if it is
 */
int is_palindrome(listint_t **head)
{
	if (head == NULL || *head == NULL)
		return (1);
	return (comp_palind(head, *head));
}

/**
 * comp_palind - function to know if it is palindrome
 * @head: head list
 * @end: end list
 */

int comp_palind(listint_t **head, listint_t *end)
{
	if (end == NULL)
		return (1);
	if (comp_palind(head, end->next) && (*head)->n == end->n)
	{
		*head = (*head)->next;
		return (1);
	}
	return (0);
}
