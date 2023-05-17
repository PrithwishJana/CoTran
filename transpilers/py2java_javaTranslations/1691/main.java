num , var k = { int ( x ) for x in input ( ) . split ( ) };
var arr = { int ( x ) for x in input ( ) . split ( ) };
var different = set ( );
var temp = 0;
arr . sort ( );
for (int x = 0; x < arr.length; x++){
    if (( x % k != 0 or not x // k in different )) {
        different . add ( x );
    }
     temp = max ( len ( different ) , temp );
}
System.out.println ( temp );
