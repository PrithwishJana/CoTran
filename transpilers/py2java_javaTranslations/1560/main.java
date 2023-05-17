import itertools;
public void compute ( ) {
    var arr = list ( range ( 10 ) );
    var temp = itertools . islice ( itertools . permutations ( arr ) , 999999 , None );
    return "" . join ( str ( x ) for x in next ( temp ) );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 