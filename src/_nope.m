/* Boilerplate is largely cribbed from matplotlib macosx backend */
/*
-----------------------------------------------------------------------------
*  Copyright (C) 2013 Min RK
*
*  Distributed under the terms of the 2-clause BSD License.
*-----------------------------------------------------------------------------
*/

#include <Cocoa/Cocoa.h>
#include <Foundation/Foundation.h>
#include <Python.h>

#if PY_MAJOR_VERSION >= 3
    #define PY3K 1
#else
    #define PY3K 0
#endif

PyObject * nope(PyObject* self) {
    #if __MAC_OS_X_VERSION_MIN_REQUIRED >= 1090
    id activity = [
        [NSProcessInfo processInfo]
            beginActivityWithOptions:NSActivityUserInitiatedAllowingIdleSystemSleep reason:@"Because Reasons"
    ];
    #else
    // Nothing to do on 10.8 or below
    #endif
    return Py_None;
}

static struct PyMethodDef methods[] = {
   {"nope",
    (PyCFunction)nope,
    METH_NOARGS,
    "Disable App Nap."
   },
   {NULL,          NULL, 0, NULL}/* sentinel */
};



#if PY3K

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "_nope",
    "_nope extension",
    -1,
    methods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyObject* PyInit__nope(void)

#else

void init_nope(void)
#endif
{

    PyObject *module;

#if PY3K
    module = PyModule_Create(&moduledef);
    if (module==NULL) return NULL;
#else
    module = Py_InitModule4("_nope",
                            methods,
                            "Disable App Nap on OS X 10.9",
                            NULL,
                            PYTHON_API_VERSION);
#endif

#if PY3K
    return module;
#endif
}
