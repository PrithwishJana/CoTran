import itertools;
public void compute ( ) {
    var cond = lambda i : all ( sorted ( str ( i ) ) == sorted ( str ( j * i ) ) for j in range ( 2 , 7 ) );
    var ans = next ( i for i in itertools . count ( 1 ) if cond ( i ) );
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 