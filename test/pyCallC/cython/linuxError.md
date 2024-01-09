

* https://stackoverflow.com/questions/34637319/hello-world-program-in-cython-fails-with-gcc-after-installation-of-python-dev-an

```
root@fqdn:~/ccc/py0/test/pyCallC/cython# python3 setup.py build_ext --inplace
running build_ext
root@fqdn:~/ccc/py0/test/pyCallC/cython# gcc -fPIC $(python3-config --cflags --ldflags) callee.c main.c
/tmp/cc0Drnfa.o: In function `__Pyx_PyInt_As_int':
/root/ccc/py0/test/pyCallC/cython/callee.c:3930: undefined reference to `PyExc_OverflowError'
/root/ccc/py0/test/pyCallC/cython/callee.c:3930: undefined reference to `PyErr_SetString'
/root/ccc/py0/test/pyCallC/cython/callee.c:3817: undefined reference to `PyLong_AsLong'
/root/ccc/py0/test/pyCallC/cython/callee.c:3817: undefined reference to `PyErr_Occurred'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLong':
/root/ccc/py0/test/pyCallC/cython/callee.c:4660: undefined reference to `PyLong_Type'
/root/ccc/py0/test/pyCallC/cython/callee.c:4665: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:4666: undefined reference to `PyExc_TypeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:4666: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLongWrongResultType':
/root/ccc/py0/test/pyCallC/cython/callee.c:4602: undefined reference to `PyExc_DeprecationWarning'
/root/ccc/py0/test/pyCallC/cython/callee.c:4602: undefined reference to `PyErr_WarnFormat'
/root/ccc/py0/test/pyCallC/cython/callee.c:4615: undefined reference to `PyExc_TypeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:4615: undefined reference to `PyErr_Format'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_GetAttrStr_ClearAttributeError':
/root/ccc/py0/test/pyCallC/cython/callee.c:2712: undefined reference to `_PyThreadState_UncheckedGet'
/root/ccc/py0/test/pyCallC/cython/callee.c:2713: undefined reference to `PyExc_AttributeError'
/tmp/cc0Drnfa.o: In function `__Pyx_PyErr_GivenExceptionMatches':
/root/ccc/py0/test/pyCallC/cython/callee.c:4395: undefined reference to `PyErr_GivenExceptionMatches'
/root/ccc/py0/test/pyCallC/cython/callee.c:4395: undefined reference to `PyErr_GivenExceptionMatches'
/tmp/cc0Drnfa.o: In function `__Pyx_InBases':
/root/ccc/py0/test/pyCallC/cython/callee.c:4300: undefined reference to `PyBaseObject_Type'
/root/ccc/py0/test/pyCallC/cython/callee.c:4300: undefined reference to `PyBaseObject_Type'
/tmp/cc0Drnfa.o: In function `__Pyx_PyErr_GivenExceptionMatchesTuple':
/root/ccc/py0/test/pyCallC/cython/callee.c:4379: undefined reference to `PyBaseObject_Type'
/tmp/cc0Drnfa.o: In function `__Pyx_AddTraceback':
/root/ccc/py0/test/pyCallC/cython/callee.c:3544: undefined reference to `_PyThreadState_UncheckedGet'
/root/ccc/py0/test/pyCallC/cython/callee.c:3565: undefined reference to `PyFrame_New'
/root/ccc/py0/test/pyCallC/cython/callee.c:3573: undefined reference to `PyTraceBack_Here'
/tmp/cc0Drnfa.o: In function `__Pyx_CreateCodeObjectForTraceback':
/root/ccc/py0/test/pyCallC/cython/callee.c:3496: undefined reference to `PyUnicode_FromFormat'
/root/ccc/py0/test/pyCallC/cython/callee.c:3498: undefined reference to `PyUnicode_AsUTF8'
/root/ccc/py0/test/pyCallC/cython/callee.c:3529: undefined reference to `PyCode_NewEmpty'
/tmp/cc0Drnfa.o: In function `__Pyx_CLineForTraceback':
/root/ccc/py0/test/pyCallC/cython/callee.c:3277: undefined reference to `_PyObject_GetDictPtr'
/root/ccc/py0/test/pyCallC/cython/callee.c:3294: undefined reference to `_Py_FalseStruct'
/root/ccc/py0/test/pyCallC/cython/callee.c:3298: undefined reference to `_Py_TrueStruct'
/root/ccc/py0/test/pyCallC/cython/callee.c:3298: undefined reference to `PyObject_Not'
/root/ccc/py0/test/pyCallC/cython/callee.c:3290: undefined reference to `PyErr_Clear'
/root/ccc/py0/test/pyCallC/cython/callee.c:3296: undefined reference to `_Py_FalseStruct'
/root/ccc/py0/test/pyCallC/cython/callee.c:3296: undefined reference to `PyObject_SetAttr'
/tmp/cc0Drnfa.o: In function `__Pyx_CreateCodeObjectForTraceback':
/root/ccc/py0/test/pyCallC/cython/callee.c:3529: undefined reference to `PyCode_NewEmpty'
/tmp/cc0Drnfa.o: In function `__pyx_insert_code_object':
/root/ccc/py0/test/pyCallC/cython/callee.c:3370: undefined reference to `PyMem_Realloc'
/tmp/cc0Drnfa.o: In function `__Pyx_CLineForTraceback':
/root/ccc/py0/test/pyCallC/cython/callee.c:3287: undefined reference to `PyObject_Not'
/root/ccc/py0/test/pyCallC/cython/callee.c:3287: undefined reference to `_Py_TrueStruct'
/root/ccc/py0/test/pyCallC/cython/callee.c:3287: undefined reference to `_Py_FalseStruct'
/tmp/cc0Drnfa.o: In function `__Pyx_PyDict_GetItemStr':
/root/ccc/py0/test/pyCallC/cython/callee.c:903: undefined reference to `_PyDict_GetItem_KnownHash'
/tmp/cc0Drnfa.o: In function `__pyx_insert_code_object':
/root/ccc/py0/test/pyCallC/cython/callee.c:3350: undefined reference to `PyMem_Malloc'
/tmp/cc0Drnfa.o: In function `__Pyx_CLineForTraceback':
/root/ccc/py0/test/pyCallC/cython/callee.c:3287: undefined reference to `_Py_FalseStruct'
/tmp/cc0Drnfa.o: In function `__Pyx_PyDict_GetItemStr':
/root/ccc/py0/test/pyCallC/cython/callee.c:904: undefined reference to `PyErr_Clear'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_GetAttrStr':
/root/ccc/py0/test/pyCallC/cython/callee.c:2704: undefined reference to `PyObject_GetAttr'
/tmp/cc0Drnfa.o: In function `__Pyx_CLineForTraceback':
/root/ccc/py0/test/pyCallC/cython/callee.c:3298: undefined reference to `_Py_FalseStruct'
/root/ccc/py0/test/pyCallC/cython/callee.c:3298: undefined reference to `_Py_TrueStruct'
/tmp/cc0Drnfa.o: In function `__Pyx_PyFunction_FastCallDict':
/root/ccc/py0/test/pyCallC/cython/callee.c:2870: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2870: undefined reference to `_Py_CheckRecursionLimit'
/root/ccc/py0/test/pyCallC/cython/callee.c:2926: undefined reference to `PyEval_EvalCodeEx'
/root/ccc/py0/test/pyCallC/cython/callee.c:2938: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2938: undefined reference to `_Py_CheckRecursionLimit'
/root/ccc/py0/test/pyCallC/cython/callee.c:2938: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2870: undefined reference to `_Py_CheckRecursiveCall'
/tmp/cc0Drnfa.o: In function `__Pyx_PyFunction_FastCallNoKw':
/root/ccc/py0/test/pyCallC/cython/callee.c:2825: undefined reference to `_PyThreadState_UncheckedGet'
/root/ccc/py0/test/pyCallC/cython/callee.c:2835: undefined reference to `PyFrame_New'
/root/ccc/py0/test/pyCallC/cython/callee.c:2844: undefined reference to `PyEval_EvalFrameEx'
/root/ccc/py0/test/pyCallC/cython/callee.c:2825: undefined reference to `_PyThreadState_UncheckedGet'
/root/ccc/py0/test/pyCallC/cython/callee.c:2835: undefined reference to `PyFrame_New'
/root/ccc/py0/test/pyCallC/cython/callee.c:2844: undefined reference to `PyEval_EvalFrameEx'
/tmp/cc0Drnfa.o: In function `__Pyx_PyInt_From_int':
/root/ccc/py0/test/pyCallC/cython/callee.c:3625: undefined reference to `PyLong_FromLong'
/tmp/cc0Drnfa.o: In function `complex_and_slow_calc_c':
/root/ccc/py0/test/pyCallC/cython/callee.c:2051: undefined reference to `PyMethod_Type'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_FastCallDict':
/root/ccc/py0/test/pyCallC/cython/callee.c:3019: undefined reference to `PyCFunction_Type'
/root/ccc/py0/test/pyCallC/cython/callee.c:3039: undefined reference to `PyFunction_Type'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_FastCall_fallback':
/root/ccc/py0/test/pyCallC/cython/callee.c:2999: undefined reference to `PyTuple_New'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_Call':
/root/ccc/py0/test/pyCallC/cython/callee.c:2954: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2954: undefined reference to `_Py_CheckRecursionLimit'
/root/ccc/py0/test/pyCallC/cython/callee.c:2958: undefined reference to `PyThreadState_Get'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_FastCallDict':
/root/ccc/py0/test/pyCallC/cython/callee.c:3039: undefined reference to `PyFunction_Type'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_FastCall_fallback':
/root/ccc/py0/test/pyCallC/cython/callee.c:2999: undefined reference to `PyTuple_New'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_Call':
/root/ccc/py0/test/pyCallC/cython/callee.c:2954: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2954: undefined reference to `_Py_CheckRecursionLimit'
/root/ccc/py0/test/pyCallC/cython/callee.c:2958: undefined reference to `PyThreadState_Get'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_CallMethO':
/root/ccc/py0/test/pyCallC/cython/callee.c:2979: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2979: undefined reference to `_Py_CheckRecursionLimit'
/root/ccc/py0/test/pyCallC/cython/callee.c:2983: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2984: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:2985: undefined reference to `PyExc_SystemError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2985: undefined reference to `PyErr_SetString'
/root/ccc/py0/test/pyCallC/cython/callee.c:2979: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2979: undefined reference to `_Py_CheckRecursionLimit'
/root/ccc/py0/test/pyCallC/cython/callee.c:2983: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2984: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:2985: undefined reference to `PyExc_SystemError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2985: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__Pyx_PyInt_As_int':
/root/ccc/py0/test/pyCallC/cython/callee.c:3930: undefined reference to `PyExc_OverflowError'
/root/ccc/py0/test/pyCallC/cython/callee.c:3930: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `complex_and_slow_calc_c':
/root/ccc/py0/test/pyCallC/cython/callee.c:2074: undefined reference to `PyErr_Occurred'
/tmp/cc0Drnfa.o: In function `__Pyx__GetModuleGlobalName':
/root/ccc/py0/test/pyCallC/cython/callee.c:2787: undefined reference to `_PyDict_GetItem_KnownHash'
/root/ccc/py0/test/pyCallC/cython/callee.c:2791: undefined reference to `PyErr_Occurred'
/tmp/cc0Drnfa.o: In function `__Pyx_GetBuiltinName':
/root/ccc/py0/test/pyCallC/cython/callee.c:2740: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:2741: undefined reference to `PyExc_NameError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2741: undefined reference to `PyErr_Format'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_GetAttrStr':
/root/ccc/py0/test/pyCallC/cython/callee.c:2704: undefined reference to `PyObject_GetAttr'
/tmp/cc0Drnfa.o: In function `__Pyx_PyInt_As_int':
/root/ccc/py0/test/pyCallC/cython/callee.c:3817: undefined reference to `PyLong_AsLong'
/root/ccc/py0/test/pyCallC/cython/callee.c:3817: undefined reference to `PyErr_Occurred'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_FastCallDict':
/root/ccc/py0/test/pyCallC/cython/callee.c:3025: undefined reference to `PyCFunction_Type'
/root/ccc/py0/test/pyCallC/cython/callee.c:3029: undefined reference to `_PyCFunction_FastCallKeywords'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_Call':
/root/ccc/py0/test/pyCallC/cython/callee.c:2958: undefined reference to `PyThreadState_Get'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_FastCallDict':
/root/ccc/py0/test/pyCallC/cython/callee.c:3029: undefined reference to `_PyCFunction_FastCallKeywords'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_Call':
/root/ccc/py0/test/pyCallC/cython/callee.c:2958: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2949: undefined reference to `PyObject_Call'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_CallMethO':
/root/ccc/py0/test/pyCallC/cython/callee.c:2983: undefined reference to `PyThreadState_Get'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_Call':
/root/ccc/py0/test/pyCallC/cython/callee.c:2954: undefined reference to `_Py_CheckRecursiveCall'
/root/ccc/py0/test/pyCallC/cython/callee.c:2949: undefined reference to `PyObject_Call'
/root/ccc/py0/test/pyCallC/cython/callee.c:2959: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:2960: undefined reference to `PyExc_SystemError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2960: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_CallMethO':
/root/ccc/py0/test/pyCallC/cython/callee.c:2983: undefined reference to `PyThreadState_Get'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_Call':
/root/ccc/py0/test/pyCallC/cython/callee.c:2954: undefined reference to `_Py_CheckRecursiveCall'
/root/ccc/py0/test/pyCallC/cython/callee.c:2959: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:2960: undefined reference to `PyExc_SystemError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2960: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_GetAttrStr':
/root/ccc/py0/test/pyCallC/cython/callee.c:2704: undefined reference to `PyObject_GetAttr'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLong':
/root/ccc/py0/test/pyCallC/cython/callee.c:4660: undefined reference to `PyLong_Type'
/tmp/cc0Drnfa.o: In function `__Pyx_PyInt_As_int':
/root/ccc/py0/test/pyCallC/cython/callee.c:3817: undefined reference to `PyLong_AsLong'
/root/ccc/py0/test/pyCallC/cython/callee.c:3930: undefined reference to `PyExc_OverflowError'
/root/ccc/py0/test/pyCallC/cython/callee.c:3930: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_CallMethO':
/root/ccc/py0/test/pyCallC/cython/callee.c:2979: undefined reference to `_Py_CheckRecursiveCall'
/root/ccc/py0/test/pyCallC/cython/callee.c:2979: undefined reference to `_Py_CheckRecursiveCall'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLong':
/root/ccc/py0/test/pyCallC/cython/callee.c:4665: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:4666: undefined reference to `PyExc_TypeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:4666: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLongWrongResultType':
/root/ccc/py0/test/pyCallC/cython/callee.c:4602: undefined reference to `PyExc_DeprecationWarning'
/root/ccc/py0/test/pyCallC/cython/callee.c:4602: undefined reference to `PyErr_WarnFormat'
/tmp/cc0Drnfa.o: In function `__Pyx_PyInt_As_int':
/root/ccc/py0/test/pyCallC/cython/callee.c:3930: undefined reference to `PyExc_OverflowError'
/root/ccc/py0/test/pyCallC/cython/callee.c:3930: undefined reference to `PyErr_SetString'
/root/ccc/py0/test/pyCallC/cython/callee.c:3817: undefined reference to `PyLong_AsLong'
/root/ccc/py0/test/pyCallC/cython/callee.c:3817: undefined reference to `PyErr_Occurred'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLong':
/root/ccc/py0/test/pyCallC/cython/callee.c:4665: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:4666: undefined reference to `PyExc_TypeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:4666: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLongWrongResultType':
/root/ccc/py0/test/pyCallC/cython/callee.c:4615: undefined reference to `PyExc_TypeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:4615: undefined reference to `PyErr_Format'
/tmp/cc0Drnfa.o: In function `__Pyx_PyInt_As_int':
/root/ccc/py0/test/pyCallC/cython/callee.c:3817: undefined reference to `PyErr_Occurred'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLongWrongResultType':
/root/ccc/py0/test/pyCallC/cython/callee.c:4602: undefined reference to `PyExc_DeprecationWarning'
/root/ccc/py0/test/pyCallC/cython/callee.c:4602: undefined reference to `PyErr_WarnFormat'
/root/ccc/py0/test/pyCallC/cython/callee.c:4602: undefined reference to `PyExc_DeprecationWarning'
/root/ccc/py0/test/pyCallC/cython/callee.c:4602: undefined reference to `PyErr_WarnFormat'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLong':
/root/ccc/py0/test/pyCallC/cython/callee.c:4665: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:4666: undefined reference to `PyExc_TypeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:4666: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__Pyx_PyNumber_IntOrLongWrongResultType':
/root/ccc/py0/test/pyCallC/cython/callee.c:4615: undefined reference to `PyExc_TypeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:4615: undefined reference to `PyErr_Format'
/root/ccc/py0/test/pyCallC/cython/callee.c:4615: undefined reference to `PyExc_TypeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:4615: undefined reference to `PyErr_Format'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_GetAttrStr':
/root/ccc/py0/test/pyCallC/cython/callee.c:2704: undefined reference to `PyObject_GetAttr'
/tmp/cc0Drnfa.o: In function `__Pyx_copy_spec_to_module':
/root/ccc/py0/test/pyCallC/cython/callee.c:2331: undefined reference to `PyObject_GetAttrString'
/root/ccc/py0/test/pyCallC/cython/callee.c:2334: undefined reference to `_Py_NoneStruct'
/root/ccc/py0/test/pyCallC/cython/callee.c:2338: undefined reference to `PyDict_SetItemString'
/root/ccc/py0/test/pyCallC/cython/callee.c:2342: undefined reference to `PyExc_AttributeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2342: undefined reference to `PyErr_ExceptionMatches'
/root/ccc/py0/test/pyCallC/cython/callee.c:2343: undefined reference to `PyErr_Clear'
/tmp/cc0Drnfa.o: In function `__Pyx_check_single_interpreter':
/root/ccc/py0/test/pyCallC/cython/callee.c:2312: undefined reference to `PyThreadState_Get'
/root/ccc/py0/test/pyCallC/cython/callee.c:2318: undefined reference to `PyExc_ImportError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2318: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__pyx_pymod_create':
/root/ccc/py0/test/pyCallC/cython/callee.c:2356: undefined reference to `PyObject_GetAttrString'
/root/ccc/py0/test/pyCallC/cython/callee.c:2358: undefined reference to `PyModule_NewObject'
/root/ccc/py0/test/pyCallC/cython/callee.c:2364: undefined reference to `PyModule_GetDict'
/tmp/cc0Drnfa.o: In function `__Pyx_InitString':
/root/ccc/py0/test/pyCallC/cython/callee.c:4460: undefined reference to `PyUnicode_InternFromString'
/root/ccc/py0/test/pyCallC/cython/callee.c:4462: undefined reference to `PyUnicode_Decode'
/root/ccc/py0/test/pyCallC/cython/callee.c:4464: undefined reference to `PyUnicode_FromStringAndSize'
/root/ccc/py0/test/pyCallC/cython/callee.c:4467: undefined reference to `PyBytes_FromStringAndSize'
/root/ccc/py0/test/pyCallC/cython/callee.c:4471: undefined reference to `PyObject_Hash'
/tmp/cc0Drnfa.o: In function `__pyx_pymod_exec_callee':
/root/ccc/py0/test/pyCallC/cython/callee.c:2395: undefined reference to `PyExc_RuntimeError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2395: undefined reference to `PyErr_SetString'
/root/ccc/py0/test/pyCallC/cython/callee.c:2423: undefined reference to `PyModule_GetDict'
/tmp/cc0Drnfa.o: In function `__Pyx_PyImport_AddModuleRef':
/root/ccc/py0/test/pyCallC/cython/callee.c:1092: undefined reference to `PyImport_AddModule'
/root/ccc/py0/test/pyCallC/cython/callee.c:1092: undefined reference to `PyImport_AddModule'
/tmp/cc0Drnfa.o: In function `__pyx_pymod_exec_callee':
/root/ccc/py0/test/pyCallC/cython/callee.c:2427: undefined reference to `PyObject_SetAttrString'
/tmp/cc0Drnfa.o: In function `__Pyx_get_runtime_version':
/root/ccc/py0/test/pyCallC/cython/callee.c:4413: undefined reference to `Py_GetVersion'
/tmp/cc0Drnfa.o: In function `__pyx_pymod_exec_callee':
/root/ccc/py0/test/pyCallC/cython/callee.c:2440: undefined reference to `PyFrame_Type'
/root/ccc/py0/test/pyCallC/cython/callee.c:2442: undefined reference to `PyTuple_New'
/tmp/cc0Drnfa.o: In function `__Pyx_check_binary_version':
/root/ccc/py0/test/pyCallC/cython/callee.c:4441: undefined reference to `PyOS_snprintf'
/root/ccc/py0/test/pyCallC/cython/callee.c:4451: undefined reference to `PyErr_WarnEx'
/tmp/cc0Drnfa.o: In function `__pyx_pymod_exec_callee':
/root/ccc/py0/test/pyCallC/cython/callee.c:2443: undefined reference to `PyBytes_FromStringAndSize'
/root/ccc/py0/test/pyCallC/cython/callee.c:2444: undefined reference to `PyUnicode_FromStringAndSize'
/root/ccc/py0/test/pyCallC/cython/callee.c:2480: undefined reference to `PyImport_GetModuleDict'
/root/ccc/py0/test/pyCallC/cython/callee.c:2476: undefined reference to `PyObject_SetAttr'
/root/ccc/py0/test/pyCallC/cython/callee.c:2481: undefined reference to `PyDict_GetItemString'
/root/ccc/py0/test/pyCallC/cython/callee.c:2482: undefined reference to `PyDict_SetItemString'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_GetAttrStr':
/root/ccc/py0/test/pyCallC/cython/callee.c:2704: undefined reference to `PyObject_GetAttr'
/tmp/cc0Drnfa.o: In function `__Pyx_GetBuiltinName':
/root/ccc/py0/test/pyCallC/cython/callee.c:2740: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:2741: undefined reference to `PyExc_NameError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2741: undefined reference to `PyErr_Format'
/tmp/cc0Drnfa.o: In function `__Pyx_PyObject_IsTrue':
/root/ccc/py0/test/pyCallC/cython/callee.c:4587: undefined reference to `_Py_TrueStruct'
/root/ccc/py0/test/pyCallC/cython/callee.c:4588: undefined reference to `_Py_FalseStruct'
/root/ccc/py0/test/pyCallC/cython/callee.c:4588: undefined reference to `_Py_NoneStruct'
/root/ccc/py0/test/pyCallC/cython/callee.c:4589: undefined reference to `PyObject_IsTrue'
/tmp/cc0Drnfa.o: In function `__Pyx_Import':
/root/ccc/py0/test/pyCallC/cython/callee.c:3094: undefined reference to `PyDict_New'
/tmp/cc0Drnfa.o: In function `__pyx_pymod_exec_callee':
/root/ccc/py0/test/pyCallC/cython/callee.c:2544: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:2545: undefined reference to `PyExc_ImportError'
/root/ccc/py0/test/pyCallC/cython/callee.c:2545: undefined reference to `PyErr_SetString'
/tmp/cc0Drnfa.o: In function `__Pyx__ImportDottedModule_Lookup':
/root/ccc/py0/test/pyCallC/cython/callee.c:3176: undefined reference to `PyImport_GetModuleDict'
/tmp/cc0Drnfa.o: In function `__Pyx_PyDict_GetItemStr':
/root/ccc/py0/test/pyCallC/cython/callee.c:903: undefined reference to `_PyDict_GetItem_KnownHash'
/root/ccc/py0/test/pyCallC/cython/callee.c:904: undefined reference to `PyErr_Clear'
/tmp/cc0Drnfa.o: In function `__Pyx_ImportDottedModule':
/root/ccc/py0/test/pyCallC/cython/callee.c:3256: undefined reference to `PyErr_Occurred'
/root/ccc/py0/test/pyCallC/cython/callee.c:3257: undefined reference to `PyErr_Clear'
/tmp/cc0Drnfa.o: In function `__Pyx_Import':
/root/ccc/py0/test/pyCallC/cython/callee.c:3121: undefined reference to `PyImport_ImportModuleLevelObject'
/tmp/cc0Drnfa.o: In function `__pyx_pymod_exec_callee':
/root/ccc/py0/test/pyCallC/cython/callee.c:2510: undefined reference to `PyDict_SetItem'
/root/ccc/py0/test/pyCallC/cython/callee.c:2519: undefined reference to `PyDict_New'
/root/ccc/py0/test/pyCallC/cython/callee.c:2521: undefined reference to `PyDict_SetItem'
/tmp/cc0Drnfa.o: In function `__Pyx_ImportDottedModule':
/root/ccc/py0/test/pyCallC/cython/callee.c:3251: undefined reference to `PyErr_Clear'
/tmp/cc0Drnfa.o: In function `PyInit_callee':
/root/ccc/py0/test/pyCallC/cython/callee.c:2300: undefined reference to `PyModuleDef_Init'
/tmp/ccbDSwL7.o: In function `main':
/root/ccc/py0/test/pyCallC/cython/main.c:5: undefined reference to `PyImport_AppendInittab'
/root/ccc/py0/test/pyCallC/cython/main.c:6: undefined reference to `Py_Initialize'
/root/ccc/py0/test/pyCallC/cython/main.c:7: undefined reference to `PyImport_ImportModule'
/root/ccc/py0/test/pyCallC/cython/main.c:12: undefined reference to `Py_Finalize'
collect2: error: ld returned 1 exit status
```