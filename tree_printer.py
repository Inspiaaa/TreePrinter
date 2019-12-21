
class Entry:
    def __init__(self, header, children=None):
        self.header = header
        self.children = [] if children is None else children


class TreePrinter:
    def __init__(self, dispatch_table):
        self.dispatch_table = dispatch_table

    def _print(self, top, matrix):
        is_last = matrix[-1]
        bars = matrix[:-1]

        for bar in bars:
            if bar:
                print("   ", end="")
            else:
                print("│  ", end="")

        if is_last:
            print("└──", end="")
        else:
            print("├──", end="")

        print(top.header)

        if len(top.children) == 0:
            return

        children = []
        for child in top.children:
            entry = self._dispatch_obj(child)
            if type(entry) == list:
                children.extend(entry)
            else:
                children.append(entry)

        for child in children[:-1]:
            self._print(child, (*matrix, False))

        # Last child
        self._print(children[-1], (*matrix, True))

    def _dispatch_obj(self, obj):
        if type(obj) == Entry:
            return obj

        if type(obj) == str:
            return Entry(obj)

        if type(obj) == int:
            return Entry(str(obj))

        return self.dispatch_table[type(obj)](obj)

    def print(self, start, top):
        print(start)
        entry = self._dispatch_obj(top)

        if type(entry) == list and len(entry) > 0:
            for e in entry[:-1]:
                self._print(e, (False,))
            self._print(entry[-1], (True,))
        else:
            self._print(entry, (True,))

class Templates:
    EXPLICIT_LIST = {list: lambda l:
    [Entry("List", [i for i in l])]}

    INDEXED_LIST = {list: lambda l:
        [Entry(str(i), [value]) for i, value in enumerate(l)]
    }
    IMPLICIT_DICT = {dict: lambda d:
        [Entry(str(key), [value]) for key, value in d.items()]
    }
    EXPLICIT_DICT = {dict: lambda d:
        [Entry("Dict", [Entry(key, [value]) for key, value in d.items()])]
    }


if __name__ == '__main__':
    data = {
        "Eras": {
            "Baroque": ["Bach", "Händel"],
            "Classical": ["Mozart", "Schubert", "Beethoven"],
            "Romantic": ["Chopin", "Dvorak"],
            "Modern": ["Ravel"]
        }
    }
    
    dispatch_table = {
        dict: lambda d: [Entry(key, [value]) for key, value in d.items()],
        list: lambda l: [Entry(value) for value in l]
    }
    
    printer = TreePrinter(dispatch_table)
    printer.print("History of Music", data)
