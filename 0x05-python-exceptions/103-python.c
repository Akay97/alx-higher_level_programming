#define PY_SSIZE_T_MAX ((size_t)-1)

#include <Python.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        fprintf(stderr, "  [ERROR] Invalid List Object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List: %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; ++i) {
        printf("Element %ld: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        fprintf(stderr, "  [ERROR] Invalid Bytes Object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;
    char *str;

    printf("[.] Bytes object info\n");
    printf("  [.] Size: %ld\n", size);
    printf("  [.] trying string: %s\n", (str = PyBytes_AsString(p)) ? str : "(null)");

    printf("  [.] first 10 bytes: ");
    for (i = 0; i < size && i < 10; ++i) {
        printf("%02hhx%c", str[i], i + 1 < size ? ' ' : '\n');
    }
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        fprintf(stderr, "  [ERROR] Invalid Float Object\n");
        return;
    }

    printf("[.] Float object info\n");
    printf("  [.] value: %f\n", ((PyFloatObject *)p)->ob_fval);
}

