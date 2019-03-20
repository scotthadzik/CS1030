 # Advanced Strings
 ## Strings are just a list of characters

>- Characters can be: 
>    - Letters  ` [A-Za-z] `
>	  - Numbers  ` [0-9] `
>	  - Symbols  ` @ $ # ~ `
>	    - [Unicode Characters Site](https://pythonforundergradengineers.com/unicode-characters-in-python.html)
>	  - Spaces   `_ _`
>	  - Escape Character `\n \r \t`

 ## String Indexing
>- Each character has an index
>
>|Char#  |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |11|
>|:-:    |:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
>|Char   |W  |E  |B  |E  |R  |   |S  |T  |A  |T  |E  |
>|+ Index|0  |1  |2  |3  |4  |5  |6  |7  |8  |9  |10 |
>|- Index|-11|-10|-9 |-8 |-7 |-6 |-5 |-4 |-3 |-2 |-1 |
>
>```python
># Select characters out of a string
>school = 'WEBER STATE'
>print ('character 1 :' + school[0])
>print ('character 4 :' + school[3])
>print ('character 7 :' + school[-4])
>```
>
## Slicing Strings

>- ### SYNTAX -- string [`start` : `end`]
>	- begin at `start` and extending up to but not including `end`
>	- school[0:3] --> `WEB`	
>	- `start` blank
>		- start at index 0
>		- **school[:3] r--> `WEB`**
>	- `end` blank
>		- go until the end of the string
>		- school[8:] --> `ATE` 
>```python
># Select a substring
>print ('start = 0 end = 4: ' + school[0:4])
>print ('start = 0 end = 5: ' + school[0:5])
>```
>```python
>print ('start = 2 end = 5: ' + school[2:5])
>print ('start = -5 end = : ' + school[-5:-1])
>```
>```python
>print ('start = -5 end = : ' + school[-5:])
>print ('start =  end = : ' + school[:])
>```

- String have a length property


[More info on Strings](https://realpython.com/python-strings/)
