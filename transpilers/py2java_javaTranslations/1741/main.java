public void countSubSets ( arr , n ) {
    var us = set ( );
    var even_count = 0;
    for i in range ( n ) :
        if (arr { i } % 2 == 0) {
            us . add ( arr { i } );
        }
     even_count = len ( us );
    return pow ( 2 , even_count ) - 1;
}
var arr = { 4 , 2 , 1 , 9 , 2 , 6 , 5 , 3 };
var n = len ( arr );
System.out.println ( "Number of var subsets =" , countSubSets ( arr , n ) );
