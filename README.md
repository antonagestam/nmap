# nmap

Map a number from one range to another

```python
>>> from nmap import nmap
>>> mapfn = nmap(0, 100, 500, 1000)
>>> mapfn(0)
500.0
>>> mapfn(50)
750.0
>>> mapfn(100)
1000.0
```

Example using the `normfn` argument to cast output to int

```python
>>> from nmap import nmap
>>> mapfn = nmap(500, 1000, 1, 10, normfn=int)
>>> mapfn(500)
1
>>> mapfn(750)
5
>>> mapfn(1000)
10
```
