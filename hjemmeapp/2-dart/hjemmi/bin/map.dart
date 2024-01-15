void main(List<String> args) {
  // Map is essentially Python's dictionary or JavaScript's object
  Map<String, dynamic> book = {
    'title': 'The Alchemist',
    'author': 'Paulo Coelho',
    'year': 1988,
    'price': 15.99,
    'isAvailable': true
  };

  // Accessed just like in Python
  String bookTitle = book['title'];

  List<dynamic> cleverTrick = book.values.toList();
  print(cleverTrick);

  // Looping over a map
  for (MapEntry entry in book.entries) {
    print('$entry.key: $entry.value');
  }

  // Could also be done with a simple forEach using the callback properly
  book.forEach((key, value) => print('key $key, value $value'));
}
