#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - a function that prints some basic
 * info about Python lists.
 * @p: the python list.
 */
void print_python_list(PyObject *p)
{
	PyListObject *info = (PyListObject *) p;
	long int i, size = PyList_Size(p);
	const char *s = NULL;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", info->allocated);
	for (i = 0; i < size; ++i)
	{
		s = (info->ob_item[i])->ob_type->tp_name;
		printf("Element %zd: %s\n", i, s);
		if (s[0] == 'b' && s[1] == 'y' && s[2] == 't' && s[3] == 'e' && s[4] == 's')
			print_python_bytes((PyObject *) info->ob_item[i]);
	}
}

/**
 * print_python_bytes - a function that prints some basic
 * info about Python lists.
 * @p: the python list.
 */
void print_python_bytes(PyObject *p)
{
	long int i, size;
	char *s = NULL;

	printf("[.] bytes object info\n");

	if (PyBytes_CheckExact(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = PyBytes_AsString(p);
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", s);
	size = size <= 9 ? size + 1 : 10;
	printf("  first %zd bytes: ", size);
	for (i = 0; i < size; ++i)
		printf("%02hhx%c", s[i], i == size - 1 ? '\n' : ' ');
}
