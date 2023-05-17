n , var m = { int ( x ) for x in input ( ) . split ( " " ) };
var lists = {};
var sq = 0;
l = k = 0;
for i in range ( n ) :
    lists . append ( input ( ) );
for i in range ( n ) :
    sq = lists { i } . count ( "B" );
    if (sq != 0) {
        sq = ( sq + 1 ) // 2;
        var l = i;
        var k = lists { i } . find ( "B" );
        break;
    }
 System.out.println ( l + sq , k + sq );
