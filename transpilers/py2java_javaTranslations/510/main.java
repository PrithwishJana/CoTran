public void fix ( A ) {
    var s = set ( );
    for i in range ( len ( A ) ) :
        s . add ( A { i } );
    for i in range ( len ( A ) ) :
        if (i in s) {
            A { i } = i;
        }
         else{
            A { i } = - 1;
        }
    return A;
}
if (var __name__ == "__main__") {
    var A = { - 1 , - 1 , 6 , 1 , 9 , 3 , 2 , - 1 , 4 , - 1 };
    System.out.println ( fix ( A ) );
}
 