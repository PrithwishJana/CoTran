public void smallestPermute ( n ) {
    var res = { "" } * ( n + 1 );
    if (( n % 2 == 0 )) {
        for i in range ( n ) :
            if (( i % 2 == 0 )) {
                res { i } = chr ( 48 + i + 2 );
            }
             else{
                res { i } = chr ( 48 + i );
            }
    }
     else{
        for i in range ( n - 2 ) :
            if (( i % 2 == 0 )) {
                res { i } = chr ( 48 + i + 2 );
            }
             else{
                res { i } = chr ( 48 + i );
            }
        res { n - 1 } = chr ( 48 + n - 2 );
        res { n - 2 } = chr ( 48 + n );
        res { n - 3 } = chr ( 48 + n - 1 );
    }
    res = '' . join ( res );
    return res;
}
if (var __name__ == "__main__") {
    var n = 7;
    System.out.println ( smallestPermute ( n ) );
}
 