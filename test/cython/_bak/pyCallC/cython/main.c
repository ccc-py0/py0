#include <Python.h>
#include “calee.h”
int main() {
  // Init module & Python 直譯器 
  PyImport_AppendInittab("callee", PyInit_callee);
  Py_Initialize();
  PyImport_ImportModule("callee");
 
  // 呼叫 function
  printf("%d\n", complex_and_slow_calc_c(3, 2, 4));
  // 釋放 Python 直譯器佔用資源
  Py_Finalize();
}