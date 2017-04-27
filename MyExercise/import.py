import import1


fun = import1.myfun

fun("asdf")

from Common.subimport import MyTestFunction

MyTestFunction("1234")

print(dir(import1))

import Common.subimport

Common.subimport.MyTestFunction("asdf")
