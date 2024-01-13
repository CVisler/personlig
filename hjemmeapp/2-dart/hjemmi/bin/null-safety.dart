void main() {
    // to make a variable nullable add a question mark
    int? age;

    // Nice because it can eliminate null checks which is annoying
    // Can run into issues, though, when trying to assign nullable var to non-null var
    String? name;
    String _name = name!; // '!' is the assert operator which tells Dart that you know the value is not null

    class Animal {
      late final String _size; // late keyword tells Dart that the value will be set later
      // Value isnt assigned until method is called

      void goBig() {
        _size = 'big';
        print(_size);
      }
    }
  }
