var n = int ( input ( ) );
var X = { int ( x ) for x in input ( ) . split ( ) };
var Y = { int ( x ) for x in input ( ) . split ( ) };
System.out.println ( 'Yes' if sum ( Y ) <= sum ( X ) else 'No' );
