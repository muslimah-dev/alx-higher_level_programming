#include "lists.h"

/**
 * reverse - reverses when it reaches half of the list
 * @h_r: head
 * return: no return.
 */
void reverse(listint_t **h_r)
{
	listint_t *previous;
	listint_t *c;
	listint_t *follow;

	previous = NULL;
	c = *h_r;

	while (c)
	{
		follow = c->next;
		c->next = previous;
		previous = c;
		c = follow;
	}
	*h_r = previous;
}

/**
 * compare - compares each int of the list
 *
 * @h1: head of the first half
 * @h2: head of the second half
 * Return: 1 if are equals, 0 if not
 */

int compare(listint_t *h1, listint_t *h2)
{
	listint_t *t1;
	listint_t *t2;

	t1 = h1;
	t2 = h2;

	while (t1 != NULL && t2 != NULL)
	{
		if (t1->n == t2->n)
		{
			t1 = t1->next;
			t2 = t2->next;
		}
		else
		{
			return (0);
		}
	}

	if (t1 == NULL && t2 == NULL)
	{
		return (1);
	}

	return (0);
}

/**
 * is_palindrome - checks if a singly linked list
 * is a palindrome
 * @head: pointer to head of list
 * Return: 0 if it is not a palindrome,
 * 1 if it is a palndrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *lag, *last, *prev_lag;
	listint_t *second_half, *mid;
	int is_pal;

	lag = last = prev_lag = *head;
	mid = NULL;
	is_pal = 1;

	if (*head != NULL && (*head)->next != NULL)
	{
		while (last != NULL && last->next != NULL)
		{
			last = last->next->next;
			prev_lag = lag;
			lag = lag->next;
		}
		if (last != NULL)
		{
			mid = lag;
			lag = lag->next;
		}

		second_half = lag;
		prev_lag->next = NULL;
		reverse(&second_half);
		is_pal = compare(*head, second_half);

		if (mid != NULL)
		{
			prev_lag->next = mid;
			mid->next = second_half;
		}
		else
		{
			prev_lag->next = second_half;
		}
	}
	return (is_pal);
}
