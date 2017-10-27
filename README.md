# python script

## find_all_substring

1st parameter : target string

2nd parameter : pattern string

return : a list of all index found

example :

```python
find_all_substring("hello and hello and hi there", "hello")
# [0, 10]
# the first hello start from index 0
# the second hello start from index 10
```

## md5

command line tool

usage :

```bash
usage:
python md5.py <value>
python md5.py -LEA <hash value> <origin message> <salt length> <append message>
```

`-LEA` means length extension attack
