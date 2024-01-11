#include <Python.h>

/**
 * print_python_string - a function that prints Python strings.
 * @p: the python string to print.
 */
void print_python_string(PyObject *p)
{
	long int len;
	char *type = NULL;
	wchar_t *val = NULL;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	type = PyUnicode_IS_COMPACT_ASCII(p) ? "ascii" : "unicode object";
	len = ((PyASCIIObject *)(p))->length;
	val = PyUnicode_AsWideCharString(p, &len);

	printf("  type: compact %s\n", type);
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", val);
}
