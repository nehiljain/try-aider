import subprocess

def main():
    subprocess.run(["jupyter", "nbconvert", "--to", "notebook", "--execute", "app.ipynb", "--inplace"])

if __name__ == "__main__":
    main()
