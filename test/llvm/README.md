# LLVM IR

## 範例


```llvm
; ModuleID = 'add.c'
source_filename = "add.c"
target datalayout = "e-m:w-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
target triple = "x86_64-pc-windows-msys"

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @add(i32 %0, i32 %1) #0 {
  %3 = alloca i32, align 4 # 
  %4 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  store i32 %1, i32* %4, align 4
  %5 = load i32, i32* %3, align 4
  %6 = load i32, i32* %4, align 4
  %7 = add nsw i32 %5, %6
  ret i32 %7
}

attributes #0 = { noinline nounwind optnone uwtable "correctly-rounded-divide-sqrt-fp-math"="false" "disable-tail-calls"="false" "frame-pointer"="none" "less-precise-fpmad"="false" "min-legal-vector-width"="0" "no-infs-fp-math"="false" "no-jump-tables"="false" "no-nans-fp-math"="false" "no-signed-zeros-fp-math"="false" "no-trapping-math"="true" "stack-protector-buffer-size"="8" "target-cpu"="x86-64" "target-features"="+cx8,+fxsr,+mmx,+sse,+sse2,+x87" "unsafe-fp-math"="false" "use-soft-float"="false" }

!llvm.module.flags = !{!0, !1}
!llvm.ident = !{!2}

!0 = !{i32 1, !"wchar_size", i32 2}
!1 = !{i32 7, !"PIC Level", i32 2}
!2 = !{!"clang version 11.0.0 (https://github.com/msys2/MSYS2-packages 9ef552a3c4cc9410d2b1fb6f22a0cdda3bc09a64)"}

```

## 解說

alloca 

在 LLVM IR 中，alloca 指令用于在当前函数的堆栈帧存储器中分配内存，以表示局部变量。它的语法如下：%ptr = alloca <type> [, <#elements>][, align <alignment>]。其中，<type> 是要分配的数据类型，<#elements> 是要分配的元素数，<alignment> 是对齐方式。例如，%ptr = alloca i32, align 4 将分配一个 4 字节的堆栈元素，该元素将遵循 4 字节的对齐方式。指向堆栈元素的指针存储在本地标识符 %ptr 中。alloca 指令通常用于表示局部（自动）变量。

其中

```
nsw : No Signed Wrap
nuw : No Unsigned Wrap
```

nuw and nsw stand for “No Unsigned Wrap” and “No Signed Wrap”, respectively. If the nuw and/or nsw keywords are present, the result value of the add is a poison value if unsigned and/or signed overflow, respectively, occurs.

## MS Copilot

為何這裡需要 alloca 然後再 load, store

```llvm
define dso_local i32 @add(i32 %0, i32 %1) #0 {
  %3 = alloca i32, align 4 # 
  %4 = alloca i32, align 4
  store i32 %0, i32* %3, align 4
  store i32 %1, i32* %4, align 4
  %5 = load i32, i32* %3, align 4
  %6 = load i32, i32* %4, align 4
  %7 = add nsw i32 %5, %6
  ret i32 %7
}
```

不能直接運算嗎?

在 LLVM IR 中，alloca 指令用于在当前函数的堆栈帧存储器中分配内存，以表示局部变量。它的语法如下：%ptr = alloca <type> [, <#elements>][, align <alignment>]。其中，<type> 是要分配的数据类型，<#elements> 是要分配的元素数，<alignment> 是对齐方式。例如，%ptr = alloca i32, align 4 将分配一个 4 字节的堆栈元素，该元素将遵循 4 字节的对齐方式。指向堆栈元素的指针存储在本地标识符 %ptr 中。alloca 指令通常用于表示局部（自动）变量。123.

在你的代码中，alloca 指令用于在堆栈帧存储器中分配两个整数变量的内存，这些变量将用于计算函数的返回值。store 指令用于将函数参数值存储在分配的内存中，load 指令用于从内存中加载变量的值，以便进行计算。因此，alloca 指令是必需的，因为它为局部变量分配了内存空间，而 load 和 store 指令则用于将数据存储在内存中和从内存中加载数据。