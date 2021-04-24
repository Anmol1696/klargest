# KLargest
A python module to provide K largest values from an input.

## Implementation
Using a min heap of constant size(k), storing the k largest values is implemented as model class `KLargest`.

In order to add values to object function, `add(self, num, *args)` where the `num` is the value and args could be any values related to the key. The k largest values are selected based on `num`.

The class stores k largest values in object variable `heap`, which can be extracted using class property `values` as a genetrator

For forming a class object from an input iterator(stream, list, iterable), use the a classmethod `from_input_iter(cls, k, input_iter, extractor=lambda x: x, **kwargs)`.
As per the current implementation, `input_iter` must be an iterable, and k must be a positive integer. `extractor` is function used for ectraction of values from the iterable and passing to `add` func. The signature of extraction should be of tuple form. So depending on the input iterable, extractor is defined.

### Example usage
Example usage with only numbers
```
k = 2
k_largest_obj = KLargest(k)
k_largest_obj.add(10)
k_largest_obj.add(11)
k_largest_obj.add(12)
k_largest_obj.add(12)

## Extract largest value
print("k largest values:", k_largest_obj.values)
```

Example 2, with extra keys
```
k = 2
k_largest_obj = KLargest(k)
k_largest_obj.add(10, "key:10")
k_largest_obj.add(11, "key:11")
k_largest_obj.add(12, "key:12")
k_largest_obj.add(12, "key:12+1")

## Extract largest value
print("k largest values:", k_largest_obj.values)
## Keys assosiated k largest values
print("k largest keys:", k_largest_obj.keys)
```

Example 3, from iterator, you can pass an iterator to use a class method to compute k largest vaules
```
k = 2
data = [10, 11, 12, 12]
k_largest_obj = KLargest.from_input_iter(k, data, extractor=lambda x: (x,))

## Extract largest value
print("k largest values:", k_largest_obj.values)
```

Example 4, from iterator, you can pass an iterator with a key to use a class method to compute k largest vaules
```
k = 2
data = [(10, "0010"), (11, "0011"), (12, "0012"), (12, "1012")]
k_largest_obj = KLargest.from_input_iter(k, data)

## Extract largest value
print("k largest values:", k_largest_obj.values)
```

## Time and Space complexity
### Time Complexity
- Build min heap of first k elements from input, `O(k)`
- For each element after k, compare to root, switch if smaller, hepify, `O((n-k)*log(k))`

Total time complexity, `O(k + (n-k)*logk)`. For large values on n, simplifies to `O(nlogk)`

### Space complexity
Using min heap, of size k, space complexity becomes `O(k)`

## Run
### Setup
Requirements are, `pip3, pip3.7` and `python3, python3.7` to be pre-installed. `make` is used thoughout, extact commands can be looked up and executed instead from `Makefile`.

The module only uses std libraries of `python3` for implementation.
External requirements are only for the testing framework used, `pytest`.

Inorder to setup use the `make` command, as
```
make install
```

### Tests
Make command for running the tests are as follows
```
make test
make test-slow
```
Currently there are 20 tests and 1 slow test.

### Docker
Requires Docker, tested on version `18`
One can use docker to setup and use `klargest` module.
```
# Build docker image
make docker-build
# Run pytests tests on docker
make docker-test
# Run interactive shell into docker to run comands directly
make docker-exec
```

For cleanup can use `make docker-clean`, this will remove any images and containers by module.

### App
Inorder to run the app, it would be preferable to run using python directives itself rather than make commands, although we have options for both.
Running application directly can be run from the package folder
```
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

## Future Improvements
- Have more tests
- Validations on `add` function needs to be improved
- Better initialization to avaoid extra checks on `add` function
- Raise custom exceptions instead of generic `Exception` where ever used
