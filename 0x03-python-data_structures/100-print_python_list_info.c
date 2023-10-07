#include "Python.h"
/**
 * print_python_list_info - prints basic info about Python lists
 * @p: PyObject list
 * Return: void
 */
void print_python_list_info(PyObject *p)
{
	int size, allocated, i;
	PyObject *element;

	if (PyList_Check(p))
	{
		size = PyList_Size(p);
		alloc = ((PyListObject *)p)->allocated;

		printf("[*] Size of the Python List = %d\n", size);
		printf("[*] Allocated = %d\n", allocated);
		for (i = 0; i < size; i++)
		{
			element = PyList_GetItem(p, i);
			printf("Element %d: %s\n", i, Py_TYPE(element)->tp_name);
		}
	}
}
