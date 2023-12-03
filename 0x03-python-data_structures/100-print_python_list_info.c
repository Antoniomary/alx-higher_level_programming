#include <Python.h>
#include <listobject.h>
#include <object.h>
#include <stdio.h>

/**
 * print_python_list_info - a function that prints some basic info about
 * Python lists.
 * @p: the python object as a list
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t i, size = PyList_Size(p);
	PyListObject *info = (PyListObject *) p;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", info->allocated);

	for (i = 0; i < size; ++i)
		printf("Element %zd: %s\n", i, (info->ob_item[i])->ob_type->tp_name);
}
