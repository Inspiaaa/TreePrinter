# Treeprinter
![Python 3.7](https://img.shields.io/badge/Python-3.x-blue.svg?style=for-the-badge&logo=python)

A simple python script to recursively print a nested tree structure. It's simple to use and can support a tree structure containing user defined types.
Very useful for visualising nested data such as:

 - File structure
 - Abstract syntax tree

Getting started
--
Copy the script into your local workspace and import it
```python
import tree_printer as tp
```

> If you want you can import it as `tp` because `tree_printer` can be quite annoying to type in every time you need it

To use it you have to instantiate a `TreePrinter` instance and declare a dispatch table which defines how the printer should handle each type. The dispatch table is a dictionary. To then print you must simply call the `print` method of your printer instance.

An example:
```python
import tree_printer as tp


data = {  
    "Eras": {  
        "Baroque": ["Bach", "Händel"],  
        "Classical": ["Mozart", "Schubert", "Beethoven"],  
        "Romantic": ["Chopin", "Dvorak"],  
        "Modern": ["Ravel"]  
    }  
}

dispatch_table = {
	dict: lambda d: [tp.Entry(key, [value]) for key, value in d.items()],
	list: lambda l: [tp.Entry(value) for value in l]
}

printer = tp.TreePrinter(dispatch_table)  
printer.print("History of Music", data)
```

Console:
```
History of Music
└──Eras
   ├──Baroque
   │  ├──Bach
   │  └──Händel
   ├──Classical
   │  ├──Mozart
   │  ├──Schubert
   │  └──Beethoven
   ├──Romantic
   │  ├──Chopin
   │  └──Dvorak
   └──Modern
      └──Ravel
```

The dispatch table's keys are the type you want to handle. For example, to handle a `list` the key must be `list`. The value of it is a lambda that takes the instance of that list as an argument and returns a `tp.Entry` or a list of `tp.Entry`.
```python
{list: lambda instance: tp.Entry("Header", [])}
```

The first argument of the `Entry` constructor is the header and the second argument is a `list` of all its children.
