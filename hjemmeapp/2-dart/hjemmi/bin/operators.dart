void main(List<String> args) {
  // Pretty much the same as in Javascript
  // Cute examples
  var x = 1;
  x++;
  x--;

  // Assignment
  String? name;
  name??= 'John Doe';
  // Assign value if null
  // If something is already assigned -> do nothing
  //
  // Ternary operator
  String color = 'red';
  var isThisRed = color == 'red' ? true : false;
  // Syntex: condition ? expr1 (if true) : expr2 (if false)
  //
  // Cascade operator
  // Used to perform a sequence of operations on the same object
  dynamic Paint;
  // In this case dynamic creates an object called Paint
  // How do I know it's an object? Because it's capitalized

  var paint = Paint();
    ..color = Colors.blue;
    ..strokeCap = StrokeCap.round;
    ..strokeWidth = 5.0;

    // TODO: I dont understand the purpose of this yet - review

    // Typecast operator
    var number = 23 as String;
    number is String; // true
}
