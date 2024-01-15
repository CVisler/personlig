void main(List<String> args) {
  String name = 'John';
  if (name == 'John') {
    print('Hello John');
  } else {
    print('Hello Someone');
  }

  // Checking if a String is empty
  print(name.isEmpty ? 'Empty' : 'Not Empty');

  // Loops
  for (var i = 0; i < 5; i++) {
    print(i);
  }

  // Assert
  var txt = 'Hello';
  // Function which takes a condition as an argument
  // If cond == true -> do nothing else raise error ONLY during debug mode
  assert(txt != null);
  // Used to validate inputs
}
