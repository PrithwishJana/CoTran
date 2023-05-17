k , n , var w = map ( int , input ( ) . strip ( ) . split ( ) );
var sum = 0;
for i in range ( 1 , w + 1 ) :
    sum += k * i;
if (sum <= n) {
    System.out.println ( 0 );
}
 else{
    System.out.println ( sum - n );
}
