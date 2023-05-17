import queue.Queue;
public void reverseQueueFirstKElements ( k , Queue ) {
    if (( Queue . empty ( ) == true or k > Queue . qsize ( ) )) {
        return;
    }
     if (( k <= 0 )) {
        return;
    }
     var Stack = {};
    for i in range ( k ) :
        Stack . append ( Queue . queue { 0 } );
        Queue . get ( );
    while (( len ( Stack ) != 0 )) {
        Queue . put ( Stack { - 1 } );
        Stack . pop ( );
    }
     for i in range ( Queue . qsize ( ) - k ) :
        Queue . put ( Queue . queue { 0 } );
        Queue . get ( );
}
public void Print ( Queue ) {
    while (( not Queue . empty ( ) )) {
        System.out.println ( Queue . queue { 0 } , var end = " " );
        Queue . get ( );
    }
 }
if (var __name__ == '__main__') {
    var Queue = Queue ( );
    Queue . put ( 10 );
    Queue . put ( 20 );
    Queue . put ( 30 );
    Queue . put ( 40 );
    Queue . put ( 50 );
    Queue . put ( 60 );
    Queue . put ( 70 );
    Queue . put ( 80 );
    Queue . put ( 90 );
    Queue . put ( 100 );
    var k = 5;
    reverseQueueFirstKElements ( k , Queue );
    Print ( Queue );
}
 