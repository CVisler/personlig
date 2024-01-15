// Functions are first class OBJECTS
// That means they can be assigned to a variable and passed to other functions
// This allows for functional programming patterns
void main(List<String> args) {
  // Defining a function
  //
  functionName() {

  }

  // Calling a function (no return value makes dart infer null type)
  functionName();

  // Second function
  String functionTwo() {
   return 'Hello';
  }
  // In this case String could be omitted because Dart can infer the return type

  var kek = functionTwo();

  // Named parameters
  namedParams(int number) {
    return 'Number is $number';
  }
  // Dart won't allow null values so you can use 'required' or default values
  namedParamsTwo({required int number, String expr = 'Great'}) {
    return 'Number is $number and thats $expr';
  }

  // Calling named parameters
  namedParamsTwo(number: 5);

  // Arrow syntax - same as Javascript
  arrowFunc(String name) => 'Hello $name';

  print(arrowFunc('John'));
  print(kek);

}

