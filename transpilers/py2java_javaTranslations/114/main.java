import collections.deque;
public void run_tasks ( A , B ) {
    var total_time = 0;
    while (( len ( A ) > 0 )) {
        var x = A . popleft ( );
        y = B . popleft ( );
        if (( x == y )) {
            total_time += 1;
        }
         else{
            B . appendleft ( y );
            A . append ( x );
            total_time += 2;
        }
    }
     return total_time;
}
if (var __name__ == '__main__') {
    var A = deque ( );
    A . append ( 3 );
    A . append ( 2 );
    A . append ( 1 );
    A . append ( 4 );
    var B = deque ( );
    B . append ( 4 );
    B . append ( 1 );
    B . append ( 3 );
    B . append ( 2 );
    System.out.println ( run_tasks ( A , B ) );
}
 