import sys;
var input = sys . stdin . readline;
var t = int ( input ( ) );
for testcases in range ( t ) :
    a , b , c , var r = map ( int , input ( ) . split ( ) );
    var MINC = c - r;
    var MAXC = c + r;
    if (var a == b) {
        System.out.println ( 0 );
    }
     else if (a < b){
        if (a <= c <= b) {
            System.out.println ( max ( 0 , MINC - a ) + max ( 0 , b - MAXC ) );
        }
         else if (c < a){
            System.out.println ( min ( b - a , max ( 0 , b - MAXC ) ) );
        }
        else if (c > b){
            System.out.println ( min ( b - a , max ( 0 , MINC - a ) ) );
        }
    }
    else{
        if (a >= c >= b) {
            System.out.println ( max ( 0 , MINC - b ) + max ( 0 , a - MAXC ) );
        }
         else if (c < b){
            System.out.println ( min ( a - b , max ( 0 , a - MAXC ) ) );
        }
        else if (c > a){
            System.out.println ( min ( a - b , max ( 0 , MINC - b ) ) );
        }
    }
