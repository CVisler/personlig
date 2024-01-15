void main() {
  int age = 20;
  double height = 1.80;
  String name = 'John Doe';

  print((age + height).runtimeType);

  // String interpolation
  print('My name is $name and I am $age years old and $height meters tall.');

  // Reassignable variables -> like saying idgaf about type here
  // Type becomes 'dynamic'. If Dart can infer the type it will e.g. String
  var myAge = 20;

  // 'Constant' variables -> value cannot be changed
  final String myName = 'John Doe';

  // Const is like final but it creates an immutable compile-time constant
  // Value therefore must be known at compile time -> if you have a constant which will change at runtime use final instead
  const double myHeight = 1.80;
  const double myWeight = 80.0;
  // const double myBMI = myWeight / (myHeight * myHeight); // error
}
