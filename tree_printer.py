
class TreePrinter:
    class Entry:
        def __init__(self, header, children=None):
            self.header = header
            self.children = [] if children is None else children

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

        for child in top.children[:-1]:
            self._print(self._dispatch_obj(child), (*matrix, False))

        # Last child
        self._print(self._dispatch_obj(top.children[-1]), (*matrix, True))

    def _dispatch_obj(self, obj):
        if type(obj) == TreePrinter.Entry:
            return obj

        if type(obj) == str:
            return TreePrinter.Entry(obj)

        if type(obj) == int:
            return TreePrinter.Entry(str(obj))

        return self.dispatch_table[type(obj)](obj)

    def print(self, top):
        self._print(self._dispatch_obj(top), (True,))
