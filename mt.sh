set -x
python py0.py convert example/mt.py0 js
deno run example/mt.js

python py0.py convert example/mt.py0 py
python example/mt.py
