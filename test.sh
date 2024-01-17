set -x

python py0.py convert example/fib.py0 irasm
python py0.py convert example/fib.py0 ir.ll
# python py0.py run example/muladd.py0 py0
# python py0.py run example/muladd.py0 py
# python py0.py run example/muladd.py0 js
# python py0.py convert example/muladd.py0 cpp

# python py0.py run example/power.py0 py0

# python py0.py convert example/fib.py0 irobj
# python py0.py convert example/fib.py0 irasm
# python py0.py run     example/fib.py0 py0
# python py0.py convert example/mt.py0 cpp
# python py0.py run example/mt.py0 js
# python py0.py run example/mt.py0 py

# python py0.py run example/fib.py0 cpp

# python py0.py run example/typed.py0 py
# python py0.py run example/typed.py0 js

# python py0.py run example/mt.py0 py
# python py0.py run example/mt.py0 js

# python py0.py convert example/assign.py0 py
# python py0.py parse example/assign.py0 py
# python py0.py convert example/assign.py0 py
# python py0.py convert example/fib.py0 py
# python example/fib.py

# python py0.py convert example/fib.py0 c
# 應該是有 main 就跑 main() ，沒 main 就當函式庫
# 反正我們主程式本來就想在 python 裡跑。

# ==== 以下作廢 =====
# ? 上面這個刻意加入了 main() ，否則會沒有主程式，C 無法執行
# ? 或許應該改成將函數都輸出到 example/fib.c，然後非函數全寫入 example/fibMain.c 檔案。
# ? 但是對真的要當函式庫的部分，又該怎麼辦呢？

# python py0.py convert example/fib.py0 js
# deno run example/fib.js

# python py0.py convert example/fib.py0 py
# python example/fib.py


# python py0.py convert example/fib.py0 js
# deno run example/fib.js

# python py0.py convert example/mt.py0 js
# deno run example/mt.js

# python py0.py convert example/mt.py0 py
# python example/mt.py

# python py0.py convert example/test.py0 js
# deno run example/test.js

# python py0.py convert example/test.py0 py
# python example/test.py
# python py0.py example/test.py0 py



