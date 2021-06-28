import subprocess
from flask import flash


def cmd_run(command):
    if not command:
        return 200001, None
    if len(command) > 1000:
        return 200002, None
    (status, output) = subprocess.getstatusoutput(command)
    # output = output.replace("\r\n",'\<br>').replace("\n",'<br>').replace("\s",' ')
    if status != 0:
        flash(output)
        return 200003, None
    else:
        flash("command run success!")
        return 0, output


if __name__ == "__main__":
    command = "ls -123 /"
    cmd_run(command)
