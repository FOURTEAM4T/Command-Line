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
    if com == "good job":
        print("\033[32;1m:) Thank You\033[0m")
        ans = "True"
        mode_answers(ans)
    else:
        ans = "False"
        mode_answers(ans)