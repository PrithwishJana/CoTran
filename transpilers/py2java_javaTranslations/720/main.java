import itertools.permutations;
var nums = list ( map ( int , input ( ) . split ( ) ) );
var o = input ( ) . split ( );
System.out.println ( min ( eval ( "min(((a{0}b){1}c){2}d,(a{0}b){2}(c{1}d))" . format ( * o ) ) for a , b , c , d in permutations ( nums ) ) );
