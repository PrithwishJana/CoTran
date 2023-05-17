public void System.out.printlnLastOccurrence ( a , n ) {
    var mp = { i : 0 for i in range ( 7 ) };
    for i in range ( n ) :
        mp { a [ i } ] = i;
    for i in range ( n ) :
        if (( mp { a [ i } ] == i )) {
            System.out.println ( a { i } , var end = " " );
        }
 }
if (var __name__ == '__main__') {
    var a = { 1 , 5 , 5 , 1 , 6 , 1 };
    var n = len ( a );
    System.out.printlnLastOccurrence ( a , n );
}
 