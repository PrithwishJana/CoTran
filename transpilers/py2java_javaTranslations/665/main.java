var n = int ( input ( ) );
var a = 2;
b = 1;
for i in range ( n - 1 ) :
    old_a = a;
    a = b;
    var b = old_a + b;
System.out.println ( b );
