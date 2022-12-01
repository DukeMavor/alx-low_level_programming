#include "main.h"
#include <stdio.h>
/**
 * binary_to_uint - change binary to int
 * @b: string of binary
 * Return: unsigned int
 */
unsigned int binary_to_uint(const char *b)
{
	unsigned int long sum;
	unsigned int long d;
	unsigned int len;
	unsigned int i;
	unsigned int leftmost;
	unsigned int leftfound = 0;

	sum = 0;
	len = 0;
	d = 1;
	i = 0;
	if (!b || !*b)
		return (0);
	while (b[len])
	{
		if (b[len] != '1' && b[len] != '0')
			return (0);
		if (b[len] == '1' && leftfound == 0)
		{
			leftmost = len;
			leftfound = 1;
		}
		len++;
	}

	len = len - leftmost;
	d = d << (len - 1);
	i = leftmost;
	while (b[i])
	{
		sum += (b[i] - '0') * d;
		d >>= 1;
		i++;
	}
	return (sum);
}
