#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))
    {
        Py_UNICODE *str = PyUnicode_AsUnicode(p);
        Py_ssize_t length = PyUnicode_GetLength(p);

        printf("String data: ");
        for (Py_ssize_t i = 0; i < length; ++i)
	{
            printf("%lc", str[i]);
        }
        printf("\n");

        printf("  Address of the object: %p\n", (void *)p);
        printf("  Length: %ld\n", length);
    }
    else 
    {
        PyErr_Print();
        fprintf(stderr, "Invalid String Object\n");
    }
}

int main()
{
    Py_Initialize();

    PyObject *str1 = PyUnicode_DecodeUTF8("Hello, World!", 13, "strict");
    PyObject *str2 = PyUnicode_DecodeUTF8("Python 3.4", 10, "strict");
    PyObject *int_obj = PyLong_FromLong(42);

    print_python_string(str1);
    print_python_string(str2);
    print_python_string(int_obj);

    Py_XDECREF(str1);
    Py_XDECREF(str2);
    Py_XDECREF(int_obj);

    Py_Finalize();

    return (0);
}
