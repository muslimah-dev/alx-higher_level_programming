#ifndef LISTS_H
#define LISTS_H

#include <stdlib.h>

/**
 * struct listint_s - a singly linked list
 * @n: data
 * @next: next data
 * Description: singly list project.
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
} listint_t
int check_cycle(listint_t *list);

