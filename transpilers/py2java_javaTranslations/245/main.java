var INF = 10 ** 20;
var MAX_INT = 10 ** 6;
var a = { INF } * MAX_INT;
var b = { INF } * MAX_INT;
a { 0 } , b { 0 } = 0 , 0;
for i in range ( 1 , 200 ) :
    var t = i * ( i + 1 ) * ( i + 2 ) // 6;
    var mm = min ( t * 5 , MAX_INT );
    for j in range ( t , mm ) :
        if (a { j } > a { j - t } + 1) {
            a { j } = a { j - t } + 1;
        }
     if t % var 2 == 0 : continue;
    for j in range ( t , MAX_INT ) :
        if (b { j } > b { j - t } + 1) {
            b { j } = b { j - t } + 1;
        }
 while (true) {
    var N = int ( input ( ) );
    if N == 0 : exit ( );
    System.out.println ( a { N } , b { N } );
}
 