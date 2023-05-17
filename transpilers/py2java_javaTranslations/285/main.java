import sys;
var input = lambda : sys . stdin . readline ( ) . rstrip ( );
sys . setrecursionlimit ( 10 ** 9 );
def pin ( var type = int ) : return map ( type , input ( ) . split ( ) );
def tupin ( var t = int ) : return tuple ( pin ( t ) );
def lispin ( t = int ) : return list ( pin ( t ) );
import collections.Counter;
public void resolve ( ) {
    var S = input ( );
    var c = Counter ( S );
    System.out.println ( ( c { "g" } - c { "p" } ) // 2 );
}
resolve ( );
