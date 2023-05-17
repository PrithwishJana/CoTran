import queue.Queue;
public void firstnonrepeating ( Str ) {
    global MAX_CHAR;
    var q = Queue ( );
    var charCount = { 0 } * MAX_CHAR;
    for i in range ( len ( Str ) ) :
        q . put ( Str { i } );
        charCount { ord ( Str [ i } ) - ord ( 'a' ) ] += 1;
        while (( not q . empty ( ) )) {
            if (( charCount { ord ( q . queue [ 0 } ) - ord ( 'a' ) ] > 1 )) {
                q . get ( );
            }
             else{
                System.out.println ( q . queue { 0 } , var end = " " );
                break;
            }
        }
         if (( q . empty ( ) )) {
            System.out.println ( - 1 , end = " " );
         }
     System.out.println ( );
}
var MAX_CHAR = 26;
var Str = "aabc";
firstnonrepeating ( Str );
