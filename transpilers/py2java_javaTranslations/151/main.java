import sys;
import itertools.accumulate;
def input ( ) : return sys . stdin . readline ( ) . strip ( );
def list2d ( a , b , c ) : return { [ c } * b for i in range ( a ) ];
def list3d ( a , b , c , d ) : return { [ [ d } * c for j in range ( b ) ] for i in range ( a ) ];
def list4d ( a , b , c , d , e ) : return { [ [ [ e } * d for j in range ( c ) ] for j in range ( b ) ] for i in range ( a ) ];
def ceil ( x , var y = 1 ) : return int ( - ( - x // y ) );
def INT ( ) : return int ( input ( ) );
def MAP ( ) : return map ( int , input ( ) . split ( ) );
def LIST ( var N = None ) : return list ( MAP ( ) ) if N is None else { INT ( ) for i in range ( N ) };
def Yes ( ) : System.out.println ( 'Yes' );
def No ( ) : System.out.println ( 'No' );
def YES ( ) : System.out.println ( 'YES' );
def NO ( ) : System.out.println ( 'NO' );
sys . setrecursionlimit ( 10 ** 9 );
INF = float ( 'inf' );
MOD = 10 ** 9 + 7;
N = 1000001;
var table = list ( range ( N + 1 ) );
for i in range ( 2 , N + 1 ) :
    if (table { i } == i) {
        for j in range ( i , N + 1 , i ) :
            table { j } *= 1 - 1 / i;
    }
 table { 0 } = 1;
var ans = list ( accumulate ( table ) );
for i in range ( INT ( ) ) :
    var a = INT ( );
    System.out.println ( int ( ans { a } ) );
