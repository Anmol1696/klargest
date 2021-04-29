# KLargest
A python module to provide K largest values from an input.

GitHub: https://github.com/Anmol1696/klargest <br>
DockerHub: https://hub.docker.com/repository/docker/anmol1696/klargest

# Implementation
Using a min heap of constant size(k), storing the k largest values is implemented as model class `KLargest`.

In order to add values to object function, `add(self, num, *args)` where the `num` is the value and args could be any values related to the key. The k largest values are selected based on `num`.

The class stores k largest values in object variable `heap`, which can be extracted using class property `values` as a genetrator

For forming a class object from an input iterator(stream, list, iterable), use the a classmethod `from_input_iter(cls, k, input_iter, extractor=lambda x: x, **kwargs)`.
As per the current implementation, `input_iter` must be an iterable, and k must be a positive integer. `extractor` is function used for ectraction of values from the iterable and passing to `add` func. The signature of extraction should be of tuple form. So depending on the input iterable, extractor is defined.

## Example usage
Inorder to run following examples, either install using one of the following
- `python setup.py install` to have pacakage available loaclly
- use interactive python directly in docker, open shell with `make docker-run DOCKER_COMMAND=python`

Example usage with only numbers
```python
from klargest import KLargest

k = 2
k_largest_obj = KLargest(k)
k_largest_obj.add(10)
k_largest_obj.add(11)
k_largest_obj.add(12)
k_largest_obj.add(12)

## Extract largest value
print("k largest values:", list(k_largest_obj.values))
## >>> k largest values: [12, 12]
```

Example 2, with extra keys
```python
from klargest import KLargest

k = 2
k_largest_obj = KLargest(k)
k_largest_obj.add(10, "key:10")
k_largest_obj.add(11, "key:11")
k_largest_obj.add(12, "key:12")
k_largest_obj.add(12, "key:12+1")

## Extract largest value
print("k largest values:", list(k_largest_obj.values))
## >>> k largest values: [12, 12]

## Keys assosiated k largest values
print("k largest keys:", list(k_largest_obj.keys))
## >>> k largest keys: ['key:12', 'key:12+1']
```

Example 3, from iterator, you can pass an iterator to use a class method to compute k largest vaules
```python
from klargest import KLargest

k = 2
data = [10, 11, 12, 12]
k_largest_obj = KLargest.from_input_iter(k, data, extractor=lambda x: (x,))

## Extract largest value
print("k largest values:", list(k_largest_obj.values))
## >>> k largest values: [12, 12]
```

Example 4, from iterator, you can pass an iterator with a key to use a class method to compute k largest vaules
```python
from klargest import KLargest

k = 2
data = [(10, "0010"), (11, "0011"), (12, "0012"), (12, "1012")]
k_largest_obj = KLargest.from_input_iter(k, data)

## Extract largest value
print("k largest values:", list(k_largest_obj.values))
## >>> k largest values: [12, 12]
```

# Time and Space complexity
## Time Complexity
- Build min heap of first k elements from input, `O(k)`
- For each element after k, compare to root, switch if smaller, hepify, `O((n-k)*log(k))`

Total time complexity, `O(k + (n-k)*logk)`. For large values on n, simplifies to `O(nlogk)`

## Space complexity
Using min heap, of size k, space complexity becomes `O(k)`

# Run
## Docker
Requires Docker, tested on version `20.10.5`. Please install `make` as well, since we use make extensively
One can use docker to setup and use `klargest` module.
```bash
# Build docker image
make docker-build

# Run pytests tests on docker
make docker-test

# Run interactive shell into docker to run comands directly
make docker-run

## Or run directly `python -m klargest 3 --input-file bin/input` inside docker
make docker-run-test-file
```

For cleanup can use `make docker-clean`, this will remove any images and containers by module.

## Local Setup
Requirements are, `pip3, pip3.7` and `python3, python3.7` to be pre-installed. `make` is used thoughout, extact commands can be looked up and executed instead from `Makefile`.

The module only uses std libraries of `python3` for implementation.
External requirements are only for the testing framework used, `pytest`.

Inorder to setup use the `make` command, as
```bash
make install
```

## Tests
Make command for running the tests are as follows
```bash
make test
make test-slow
```
Currently there are 24 tests and 1 slow test. Following is the snipet of running all tests
```
============================= test session starts ==============================
platform linux -- Python 3.9.4, pytest-5.4.3, py-1.8.2, pluggy-0.13.1 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /usr/local/app
collecting ... collected 25 items

klargest/tests/test_models.py::test_k_largest[0] PASSED                  [  4%]
klargest/tests/test_models.py::test_k_largest[1] PASSED                  [  8%]
klargest/tests/test_models.py::test_k_largest[2] PASSED                  [ 12%]
klargest/tests/test_models.py::test_k_largest[3] PASSED                  [ 16%]
klargest/tests/test_models.py::test_k_largest[4] PASSED                  [ 20%]
klargest/tests/test_models.py::test_k_largest[5] PASSED                  [ 24%]
klargest/tests/test_models.py::test_k_largest_from_list_of_tuples_input[0] PASSED [ 28%]
klargest/tests/test_models.py::test_k_largest_from_list_of_tuples_input[1] PASSED [ 32%]
klargest/tests/test_models.py::test_k_largest_from_list_of_tuples_input[2] PASSED [ 36%]
klargest/tests/test_models.py::test_k_largest_from_list_of_tuples_input[3] PASSED [ 40%]
klargest/tests/test_models.py::test_k_largest_from_list_of_tuples_input[4] PASSED [ 44%]
klargest/tests/test_models.py::test_k_largest_from_list_of_tuples_input[5] PASSED [ 48%]
klargest/tests/test_models.py::test_input_without_keys PASSED            [ 52%]
klargest/tests/test_models.py::test_models_from_list_input PASSED        [ 56%]
klargest/tests/test_models.py::test_model_with_invalid_k_value[0.1] PASSED [ 60%]
klargest/tests/test_models.py::test_model_with_invalid_k_value[-1] PASSED [ 64%]
klargest/tests/test_models.py::test_model_with_invalid_k_value[test] PASSED [ 68%]
klargest/tests/test_models.py::test_model_with_invalid_k_value[k3] PASSED [ 72%]
klargest/tests/test_models.py::test_k_gt_input_lenght PASSED             [ 76%]
klargest/tests/test_models.py::test_large_input[10] PASSED               [ 80%]
klargest/tests/test_models.py::test_large_input[100] PASSED              [ 84%]
klargest/tests/test_models.py::test_large_input[1000] PASSED             [ 88%]
klargest/tests/test_models.py::test_large_input[10000] PASSED            [ 92%]
klargest/tests/test_models.py::test_large_input[100000] PASSED           [ 96%]
klargest/tests/test_models.py::test_very_large_input_slowtest PASSED     [100%]

======================= 25 passed in 12.20s ========================
```

# Application
Inorder to run the app, it would be preferable to run using python directives itself rather than make commands, although we have options for both.
Running application directly can be run from the package folder
```bash
python3 -m klargest --help

# eg. with example input file
python3 -m klargest 3 --input-file bin/input
```
Output from help shows how to run the app, and all arguments related.
- K (for k largest values) is a required variable
- Input file is optional, if not specified, stdin is used to read
- If output file is specified, then output is only writen to file not std out
```
python3 -m klargest --help
usage: __main__.py [-h] [--input-file INPUT_FILE] [--output-file OUTPUT_FILE]
                   K

Process stream to get K Largest uids.

positional arguments:
  K                     int for returning number of uids

optional arguments:
  -h, --help            show this help message and exit
  --input-file INPUT_FILE
                        optional file name to read stream (default: stdin)
  --output-file OUTPUT_FILE
                        optional file output to write (default: stdout)
```

# DevOps
Using the github actions for CI/CD workflows directly build docker images and push to dockerhub, and run pytest.

## Dockerfile
Using the base image of python alpine. Creating a working dir at `/usr/local/app` and copy code to it.

A `appuser` which is a non root user for running the application, which is the default docker user.
`make` command is avaibale as well in the docker container itself.

## Build and Push Docker image
When any commit is made to the `main` branch, directly or via a merged pull request, triggers this workflow.
The docker image is build, tagged and pushed to docker hub.

Docker tag for the images are of the form, `anmol1696/klargest:{date}-{git-short-commit}`. The latest image is also tagged with
tag of `latest`.

Pushed Docker hub image via workflow: https://hub.docker.com/repository/docker/anmol1696/klargest/tags?page=1&ordering=last_updated <br>
Github actions: https://github.com/Anmol1696/klargest/actions/workflows/build.yaml

Inorder to use docker image from dockerhub via make command
```bash
make docker-run DOCKER_TAG=latest

# Might have to delete the local latest image
make docker-clear DOCKER_TAG=latest
```

## Run Tests on Docker
When a pull request is created for `main`, or commit pushed to `main` branch, trggers this test workflow.
This creates a test docker image and runs pytests.

Have a look at the github actions at https://github.com/Anmol1696/klargest/actions/workflows/test.yaml <br>
Sample test triggered via a pull request: https://github.com/Anmol1696/klargest/pull/1/checks

# Future Improvements
- Have more tests
- Validations on `add` function needs to be improved
- Better initialization to avaoid extra checks on `add` function
- Raise custom exceptions instead of generic `Exception` where ever used
- Make devops workflows more generic, to be runable for any branchs, not just `main`
- Break large documentation into smaller parts
