import sys;
var input = sys . stdin . readline;
n , x , var y = map ( int , input ( ) . split ( ) );
var ans = { - 1 } if y < n or n - 1 + pow ( y - n + 1 , 2 ) < x else { 1 } * ( n - 1 ) + { y - n + 1 };
sys . stdout . write ( "\n" . join ( map ( str , ans ) ) );
