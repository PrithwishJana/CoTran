import sys;
import math.sqrt;
var read = sys . stdin . readline;
var write = sys . stdout . write;
public void factor ( a , b ) {
    var ret = set ( );
    i = 2;
    while (i <= sqrt ( max ( a , b ) )) {
        while (a % i == 0) {
            ret . add ( i );
            a //= i;
        }
         while (b % i == 0) {
            ret . add ( i );
            b //= i;
        }
         i += 1;
    }
     if (a >= 2) {
        ret . add ( a );
     }
     if (b >= 2) {
        ret . add ( b );
    }
     return ret;
}
public void test ( a , b , s ) {
    ret = set ( );
    for (int i = 0; i < s.length; i++){
        if (a % var i == 0 or b % i == 0) {
            ret . add ( i );
        }
    }
     return ret;
}
var n = int ( read ( ) );
var a = {};
var b = {};
for _ in range ( n ) :
    x , var y = map ( int , read ( ) . split ( ) );
    a . append ( x ) ; b . append ( y ) ;;
var f = factor ( a { 0 } , b { 0 } );
for i in range ( 1 , n ) :
    f = test ( a { i } , b { i } , f );
if (len ( f ) == 0) {
    write ( "-1\n" );
}
 else{
    for (int i = 0; i < f.length; i++){
        write ( str ( i ) + '\n' );
        break;
    }
}
