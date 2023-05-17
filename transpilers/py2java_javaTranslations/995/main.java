public void countFreq ( a , n ) {
    var hm = dict ( );
    for i in range ( n ) :
        hm { a [ i } ] = hm . get ( a { i } , 0 ) + 1;
    var cumul = 0;
    for i in range ( n ) :
        cumul += hm { a [ i } ];
        if (( hm { a [ i } ] > 0 )) {
            System.out.println ( a { i } , "->" , cumul );
        }
         hm { a [ i } ] = 0;
}
var a = { 1 , 3 , 2 , 4 , 2 , 1 };
var n = len ( a );
countFreq ( a , n );
