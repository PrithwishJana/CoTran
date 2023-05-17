public void Reverseorder ( n ) {
    var prime = { true } * ( n + 1 ) ;;
    var p = 2 ;;
    while (( p * p <= n )) {
        if (( prime { p } == true )) {
            for i in range ( ( p * 2 ) , ( n + 1 ) , p ) :
                prime { i } = false ;;
        }
         p += 1 ;;
    }
     for p in range ( n , 1 , - 1 ) :
        if (( prime { p } )) {
            System.out.println ( p , var end = " " ) ;;
        }
 }
var N = 25 ;;
System.out.println ( "Prime number in reverse order" ) ;;
if (( N == 1 )) {
    System.out.println ( "No prime no exist in this range" ) ;;
}
 else{
    Reverseorder ( N ) ;;
}
