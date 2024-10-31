import os
import win11toast
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
    if com == "/test":
        print("ivisible tester")
        win11toast.toast("Invisible tester!")
        ans = "True"
        mode_answers(ans)
    else:
        ans = "False"
        mode_answers(ans)