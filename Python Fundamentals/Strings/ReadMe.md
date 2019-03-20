 # Advanced Strings
 > ## Strings are just a list of charecters

- Characters can be: 
    - Letters  ` [A-Za-z] `
	- Numbers  ` [0-9] `
	- Symbols  ` @ $ # ~ `
	    - [Unicode Characters Site](https://pythonforundergradengineers.com/unicode-characters-in-python.html)
	- Spaces   `_ _`
	- Escape Character `\n \r \t`

> ## String Indexing
- Each character has an index

|Char#  |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |11|
|:-:    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|Char   |W  |E  |B  |E  |R  |   |S  |T  |A  |T  |E  |
|+ Index|0  |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
|- Index|-11|-10|-9 |-8 |-7 |-6 |-5 |-4 |-3 |-2 |-1 |

```python
# Select characters out of a string
school = 'Weber State'
print ('character 1 :')
print (school[0])
print ('character 4 :')
print (school[3])
print ('character 7 :')
print (school[-4])
```

[More info on Strings](https://realpython.com/python-strings/)
