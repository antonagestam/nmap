# nmap

Map a number from one range to another

```python
from nmap import nmap

mapfn = nmap(0, 100, 500, 1000)
mapfn(100)  # 1000
```
