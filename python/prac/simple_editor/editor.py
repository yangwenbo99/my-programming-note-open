#!/bin/python3

""" A simple editor

The editor has 2 modes, insert mode and normal mode. Under insert mode,
things inputted will be directly written into the file. Use Under normal mode,

For manual of the usage of the editor, refer to README.md
"""

__promote_sign__ = ": "

def insert_mode():
    res = []
    while True:
        try:
            newline = input();
        except EOFError:
            break
        newline += "\n"
        res.append(newline)
    return res

def promote():
    key_in = input(__promote_sign__)
    return key_in.split()

class EditingFile:
    __history_buf_size__ = 100
    def __init__(self, file_name):
        self._file_name = file_name
        with open(file_name, "r") as f:
            self._contents = f.readlines()
        self._current_line = 0
        self._history_list = []
        self._marks = {}
    
    def modify(self, ls, le, new_contents):
        # change the contents
        removed = self._contents[ls:le]
        self._contents[ls:le] = new_contents
        # Record the history
        self._history_list.append(
                {   "start": ls, 
                    "old": removed, 
                    "new": new_contents
                    });
        if len(self._history_list) > self.__history_buf_size__:
            self._history_list.remove(0)
        # line numbers
        new_le = ls + len(new_contents)
        for i in self._marks:
            if self._marks[i] >= le:
                self._marks[i] += new_le - le
            elif self._marks[i] >= ls:
                self._marks[i] = ls

    def undo(self):
        last_record = self._history_list.pop()
        ls = last_record["start"]
        le = ls + len(last_record["new"])
        self._contents[ls:le] = last_record["old"]
        # line numbers
        old_le = ls + len(last_record["old"])
        for i in self._marks:
            if self._marks[i] >= le:
                self._marks[i] += old_le - le
            elif self._marks[i] >= ls:
                self._marks[i] = ls
    
    def print(self, n = 1):
        try: 
            for i in range(self._current_line, self._current_line+n):
                print(i, "\t", self._contents[i], end="")
        except IndexError:
            print("--File Ended--")

    def write(self, file_name = None):
        """Write changes into the file given, if not given, write to the 
        current file, if given, self._file_name will be changed to
        the given name.

        Exception may be raised because of open()
        """
        if file_name == None:
            file_name = self._file_name
        with open(self._file_name, "w") as f:
            for i in self._contents:
                f.write(i)
        self._file_name = file_name

    def insert(self, new_contents):
        self.modify(self._current_line, self._current_line, new_contents);
        self._current_line += len(new_contents)
    def append(self, new_contents):
        self.modify(self._current_line+1, self._current_line+1, 
                new_contents);
        self._current_line += len(new_contents)
    def append_end(self, new_contents):
        self._current_line = len(self._contents)
        self.insert(new_contents)
    def substitude(self, new_contents):
        self.modify(self._current_line, self._current_line+1, new_contents);

    def mark(self, mark_name):
        """ Mark current line, if the mark_name has been used, it will 
        be overwritten"""
        self._marks[mark_name] = self._current_line
    def goto_mark(self, mark_name):
        """Go to the given mark
        
        KeyError may be raised"""
        self._current_line = self._marks[mark_name]
    def goto_top(self, num):
        """Go to a line counted from top

        IndexError may be raised"""
        self._current_line = num
    def goto_bottom(self, num):
        """Go to a line counted from bottom

        IndexError may be raised"""
        self._current_line = len(self._contents) - num
    def goto_current(self, num):
        """Go to a line counted relative to the current line

        IndexError may be raised"""
        self._current_line += num
        
if __name__ == "__main__":
    from sys import argv

    unsaved = False
    opened = None

    if len(argv) >= 2:
        try:
            opened = EditingFile(argv[1])
            print(f"File \"{argv[1]}\" opened")
        except Exception as e:
            print("Error opening file: ", e)

    while True:
        command = promote()
        if len(command) == 0:
            continue
        first_wd = command[0]
        try:
            if first_wd == "e":
                if opened == None:
                    opened = EditingFile(command[1])
                elif not unsaved:
                    opened = EditingFile(command[1])
                else:
                    print("File not saved, save before switching.")
            elif first_wd == "w":
                if opened == None:
                    print("File not opened")
                elif not unsaved:
                    pass
                elif len(command) >= 2:
                    opened.write(command[2])
                else:
                    opened.write()
                unsaved = False
            elif first_wd == "q":
                if unsaved:
                    print("File unsaved")
                else:
                    break
            elif first_wd == "p":
                if len(command) >= 2:
                    opened.print(int(command[1]))
                else:
                    opened.print()
            elif first_wd == "i":
                unsaved = True
                opened.insert(insert_mode())
            elif first_wd == "a":
                unsaved = True
                opened.append(insert_mode())
            elif first_wd == "A":
                unsaved = True
                opened.append_end(insert_mode())
            elif first_wd == "s":
                unsaved = True
                opened.substitude(insert_mode())
            elif first_wd == "g":
                if len(command) >= 2:
                    opened.goto_top(int(command[1]))
                else:
                    opened.goto_top(0);
            elif first_wd == "G":
                if len(command) >= 2:
                    opened.goto_bottom(int(command[1]))
                else:
                    opened.goto_bottom(0);
            elif first_wd == "h":
                opened.goto_current(int(command[1]))
            elif first_wd == "m":
                opened.mark(command[1])
            elif first_wd == "k":
                opened.goto_mark(command[1])
            else:
                print("Syntax Error")

        except IndexError as e:
            print("Line out of range or too few arguments", e)
        except FileNotFoundError as e:
            print("File not found", e)
        except PermissionError as e:
            print("Permission denied", e)
        except AttributeError as e:
            print("File not opened", e)
        except Exception as e:
            print("Unknown error, you are strongly suggested to save and exit");
            print(e)







        
