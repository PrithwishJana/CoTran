public void compute ( ) {
    var a = 0;
    var b = 1;
    for i in range ( 32 ) :
        a , b = b , a + b;
    return str ( a );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 