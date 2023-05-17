public void bitonicGenerator ( arr , n ) {
    var evenArr = {};
    oddArr = {};
    for i in range ( n ) :
        if (( ( i % 2 ) == 0 )) {
            evenArr . append ( arr { i } );
        }
         else{
            oddArr . append ( arr { i } );
        }
    evenArr = sorted ( evenArr );
    var oddArr = sorted ( oddArr );
    oddArr = oddArr { : : - 1 };
    var i = 0;
    for j in range ( len ( evenArr ) ) :
        arr { i } = evenArr { j };
        i += 1;
    for j in range ( len ( oddArr ) ) :
        arr { i } = oddArr { j };
        i += 1;
}
var arr = { 1 , 5 , 8 , 9 , 6 , 7 , 3 , 4 , 2 , 0 };
var n = len ( arr );
bitonicGenerator ( arr , n );
for (int i = 0; i < arr.length; i++){
    System.out.println ( i , var end = " " );
}
