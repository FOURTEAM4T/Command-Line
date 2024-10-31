# Command-Line
Command Line to make simple your life

# How to install
Install zip file from releases. Extract all files. Open .../Command_Line/ComLine/ComLine.exe. WARNING!!! Command Line now availible only for Windows after 7 and Linux.
# All commands
1."/close" closing program.
2."/keytap" tapping every keys. Example :
/keytap
a
3."/print" prints everything. Example:
/print
example
example
4."/file.create" creates files.
5."/del.file" deletes files.
6."/create.dir" creates folders.
7."/del.dir" deletes folders.
8."/open" opens files.
9."/help" opens help file.
10."/caesar" encrypts Caesar cipher.
11."/info" shows device info.
12."/location" shows your location info.
13."/ip" Shows ip info. Example:
/ip
Type your ip: 1.1.1.1
('ip: ', '1.1.1.1')
('city: ', 'Sydney')
('region: ', 'New South Wales')
('country: ', 'Australia')
(COMING SOON)
14."/country.info" information about your country.
15."/upgrade" not useful for now.
16."/install" installing modifications to Command Line.
17."/unistall" unistalling modifications from Command Line.
18."/modes" prints all installes modification.
# How to create own modification(mode)
You must create mode at Python 3.12. Else versions of Python will show "ImportError" or "wrong magic number".

You can create 3 types of modes:
New commands:
Example:
import os
def mode_answers(answer):
    try:
        os.chdir("..")
        os.chdir("mode_editor")
        os.remove("answer.4t")
    except:
        pass
    f = open("answer.4t","w")
    f.write(answer)
    f.close()
    os.chdir("..")
    os.chdir("ComLine")
def system():
    pass
def main(com):
    if com == "/command":
        print("That's working!")
        ans = "True"
        mode_answers(ans)
    else:
        ans = "False"
        mode_answers(ans)

New commands mode are creating new commands,
System modes:
Example
import os
def mode_answers(answer):
    try:
        os.chdir("..")
        os.chdir("mode_editor")
        os.remove("answer.4t")
    except:
        pass
    f = open("answer.4t","w")
    f.write(answer)
    f.close()
    os.chdir("..")
    os.chdir("ComLine")
def system():
    os.system("image.jpeg")
def main(com):
    ans = "False"
    mode_answers(ans)

System modes are changing visual in Command Line (You can use it for other goals.)
All in:
Include in new commands and visual.
