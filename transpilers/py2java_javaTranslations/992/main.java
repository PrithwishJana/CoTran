import heapq.heapify , heappushpop;
N , * var A = map ( int , open ( 0 ) . read ( ) . split ( ) );
L , C , var R = A { : N } , A { N : 2 * N } , A { 2 * N : };
F = { sum ( L ) };
heapify ( L );
for (int c = 0; c < C.length; c++){
    F . append ( F { - 1 } + c - heappushpop ( L , c ) );
}
R = { - r for r in R };
var B = { sum ( R ) };
heapify ( R );
for c in reversed ( C ) :
    B . append ( B { - 1 } - c - heappushpop ( R , - c ) );
System.out.println ( max ( f + b for f , b in zip ( F , reversed ( B ) ) ) );
