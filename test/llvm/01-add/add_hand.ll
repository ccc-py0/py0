source_filename = "add.c"
target triple = "x86_64-pc-windows-msys"

; Function Attrs: noinline nounwind optnone uwtable
define dso_local i32 @add(i32 %a, i32 %b) #0 {
  %T1 = add i32 %a, %b
  ret i32 %T1
}