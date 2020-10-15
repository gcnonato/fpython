import subprocess
import sys


def run(cmd):
    proc = subprocess.Popen(cmd,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE,
                            )
    stdout, stderr = proc.communicate()

    return proc.returncode, stdout, stderr

# code, out, err = run([sys.executable, 'run.py'])
code, out, err = run([sys.executable, 'bd.py'])

print(f"out: {out}")
print(f"err: '{err}'")
print(f"exit: {code}")
