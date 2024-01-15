void main(List<String> args) {
  // <> means generic type and [] is the literal list
  List<int> numbers = [1, 2, 3, 4, 5];
  // Can be indexed as usual - hint: numbers.sublist(1, 3) returns [2, 3]
  var nums2 = List.filled(5, 0); 
  // fills the list with 0's - fills the list with 5 0's
  //
  for (int i in numbers) {
    print(i);
  }

  // List methods
  // map runs a callback on each item to transform the items into a new list
  var doubled = numbers.map((int i) => i * 2);

  // List combiner
  var combined = [...numbers, ...doubled];
  print(combined);
  combined.forEach(print);

  bool depressed = false;
  var cart = [
    'milk', 
    'eggs', 
    if (depressed) 'Vodka',
  ];

  print('${cart.length} items in your cart');

}
