input ( );
var a = b = 0;
for x , y in zip ( input ( ) , input ( ) ) :
    a += x > y;
    b += x < y;
System.out.println ( - 1 if a == 0 else b // a + 1 );
