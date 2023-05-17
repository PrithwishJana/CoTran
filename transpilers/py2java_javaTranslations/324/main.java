public void numbersWith3Divisors ( n ) {
    var prime = { true } * ( n + 1 ) ;;
    prime { 0 } = prime { 1 } = false ;;
    var p = 2 ;;
    while (( p * p <= n )) {
        if (( prime { p } == true )) {
            for i in range ( p * 2 , n + 1 , p ) :
                prime { i } = false ;;
        }
         p += 1 ;;
    }
     System.out.println ( "Numbers with 3 divisors :" ) ;;
    var i = 0 ;;
    while (( i * i <= n )) {
        if (( prime { i } )) {
            System.out.println ( i * i , var end = " " ) ;;
        }
         i += 1 ;;
    }
 }
var n = 96 ;;
numbersWith3Divisors ( n ) ;;
