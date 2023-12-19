#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <bytesobject.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - a function that prints some basic
 * info about Python lists.
 * @p: the python list object.
 */
void print_python_list(PyObject *p)
{
	PyListObject *info = (PyListObject *) p;
	PyVarObject *info1 = (PyVarObject *)p;
	long int i, size = info1->ob_size;
	const char *s = NULL;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (PyList_CheckExact(p) == 0)
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", info->allocated);
	for (i = 0; i < size; ++i)
	{
		s = (info->ob_item[i])->ob_type->tp_name;
		printf("Element %zd: %s\n", i, s);
		if (strcmp(s, "bytes") == 0)
			print_python_bytes((PyObject *) info->ob_item[i]);
		else if (strcmp(s, "float") == 0)
			print_python_float((PyObject *) info->ob_item[i]);
	}
}

/**
 * print_python_bytes - a function that prints some basic
 * info about Python bytes.
 * @p: the python byte object.
 */
void print_python_bytes(PyObject *p)
{
	long int i, size;
	char *s = NULL;
	PyBytesObject *bytes = (PyBytesObject *) p;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (PyBytes_CheckExact(p) == 0)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	s = bytes->ob_sval;
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	printf("  trying string: %s\n", s);
	size = size <= 9 ? size + 1 : 10;
	printf("  first %zd bytes: ", size);
	for (i = 0; i < size; ++i)
		printf("%02hhx%c", s[i], i == size - 1 ? '\n' : ' ');
}

/**
 * print_python_float - a function that prints some basic
 * info about Python float.
 * @p: the python float object.
 */
void print_python_float(PyObject *p)
{
	char *ptr = NULL;
	PyFloatObject *obj = (PyFloatObject *) p;

	fflush(stdout);
	printf("[.] float object info\n");

	if (PyFloat_CheckExact(p) == 0)
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	ptr = PyOS_double_to_string(obj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", ptr);
	PyMem_Free(ptr);
}
