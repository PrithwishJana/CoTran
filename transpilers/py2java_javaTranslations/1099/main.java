import queue.Queue;
public void checkStackPermutation ( ip , op , n ) {
    var Input = Queue ( );
    for i in range ( n ) :
        Input . put ( ip { i } );
    output = Queue ( );
    for i in range ( n ) :
        output . put ( op { i } );
    tempStack = {};
    while (( not Input . empty ( ) )) {
        ele = Input . queue { 0 };
        Input . get ( );
        if (( ele == output . queue { 0 } )) {
            output . get ( );
            while (( len ( tempStack ) != 0 )) {
                if (( tempStack { - 1 } == output . queue { 0 } )) {
                    tempStack . pop ( );
                    output . get ( );
                }
                 else{
                    break;
                }
            }
        }
          else{
            tempStack . append ( ele );
         }
    }
     return ( Input . empty ( ) and len ( tempStack ) == 0 );
}
if (__name__ == '__main__') {
    Input = { 1 , 2 , 3 };
    var output = { 2 , 1 , 3 };
    var n = 3;
    if (( checkStackPermutation ( Input , output , n ) )) {
        System.out.println ( "Yes" );
    }
     else{
        System.out.println ( "Not Possible" );
    }
}
 