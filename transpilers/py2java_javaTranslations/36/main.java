var s = input ( );
var k = int ( input ( ) );
System.out.println ( 'impossible' if k > len ( s ) else max ( 0 , k - len ( set ( s ) ) ) );
