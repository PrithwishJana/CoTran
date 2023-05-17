import eulerlib , heapq;
public void compute ( ) {
    var TARGET = 500500;
    var MODULUS = 500500507;
    var isprime = eulerlib . list_primality ( 7376507 );
    var queue = {};
    var nextprime = 2;
    heapq . heappush ( queue , nextprime );
    var ans = 1;
    for _ in range ( TARGET ) :
        var item = heapq . heappop ( queue );
        ans *= item;
        ans %= MODULUS;
        heapq . heappush ( queue , item ** 2 );
        if (item == nextprime) {
            nextprime += 1;
            while (not isprime { nextprime }) {
                nextprime += 1;
            }
             heapq . heappush ( queue , nextprime );
        }
     return str ( ans );
}
if (var __name__ == "__main__") {
    System.out.println ( compute ( ) );
}
 