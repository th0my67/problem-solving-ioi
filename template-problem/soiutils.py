import sys, os

def load_test(filename, testdir="tests", extension=".in", debug=False):
    # Redirecting the selected file to standard input for debugging purposes
    print(__file__)
    os.chdir(os.path.dirname(__file__))
    sys.stdin = open(os.path.join(testdir, f"{filename}.in"), "r")
    sys.stdout = open(os.path.join(testdir, f"{filename}.run.out"), "w")