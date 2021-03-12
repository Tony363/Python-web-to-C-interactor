# A simple Python web to C interactor

## Use method:

* Input value to C by argv method by default. If using stdin is desiered, the program need to do a little bit adjust.

* The compiled C program was placed in root by default. However, adjust is also avaliable if needed.

* **The program has not been tested yet.**

* `SECRET_KEY` must be replaced by a permanent value and store in a non-public file before deployment.
* Use `os.urandom(32)` in Python is a good way to generate a secret key.
* The directory of the C program could be modify , `./main` is default. 