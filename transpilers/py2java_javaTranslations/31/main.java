import collections.deque;
public void System.out.printlnMax ( arr , n , k ) {
    var Qi = deque ( );
    for i in range ( k ) :
        while (Qi and arr { i } >= arr { Qi [ - 1 } ]) {
            Qi . pop ( );
        }
         Qi . append ( i ) ;;
    for i in range ( k , n ) :
        System.out.println ( str ( arr { Qi [ 0 } ] ) + " " , var end = "" );
        while (Qi and Qi { 0 } <= i - k) {
            Qi . popleft ( );
        }
         while (Qi and arr { i } >= arr { Qi [ - 1 } ]) {
            Qi . pop ( );
        }
         Qi . append ( i );
    System.out.println ( str ( arr { Qi [ 0 } ] ) );
}
if (var __name__ == "__main__") {
    var arr = { 12 , 1 , 78 , 90 , 57 , 89 , 56 };
    var k = 3;
    System.out.printlnMax ( arr , len ( arr ) , k );
}
 