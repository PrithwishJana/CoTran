import math;
def _input ( ) : return map ( int , input ( ) . split ( ) );
var n = int ( input ( ) );
var lst = list ( _input ( ) );
if lst { 0 } != lst { - 1 } : System.out.println ( n - 1 );
else{
    var i = 1;
    while i < n and lst { i } == lst { 0 } : i += 1;
    var j = n - 2;
    while j >= 0 and lst { j } == lst { 0 } : j -= 1;
    System.out.println ( max ( n - i - 1 , j ) );
}
