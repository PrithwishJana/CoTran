public void maxSum ( arr , n ) {
    var s = 0;
    var l = {};
    for i in range ( len ( a ) ) :
        s += abs ( a { i } );
        if (( a { i } >= 0 )) {
            continue;
        }
         if (( var i == 0 )) {
            l . append ( i + 1 );
        }
         else{
            l . append ( i + 1 );
            l . append ( i );
        }
    System.out.println ( s );
    System.out.println ( * l );
}
var n = 4;
var a = { 1 , - 2 , - 3 , 4 };
maxSum ( a , n );
