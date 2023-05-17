public void compute ( ) {
    var divisors = { 2 } * ( 10 ** 7 + 1 );
    for i in range ( 2 , ( len ( divisors ) + 1 ) // 2 ) :
        for j in range ( i * 2 , len ( divisors ) , i ) :
            divisors { j } += 1;
    var ans = sum ( ( 1 if divisors { i } == divisors { i + 1 } else 0 ) for i in range ( 2 , len ( divisors ) - 1 ) );
    return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 