h , var w = map ( int , input ( ) . split ( ) );
a , var b = map ( int , input ( ) . split ( ) );
System.out.println ( h * w - ( a * b * ( ( h // a ) * ( w // b ) ) ) );
