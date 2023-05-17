import math.sqrt;
var sz = int ( 1e5 ) ;;
var isPrime = { true } * ( sz + 1 ) ;;
public void sieve ( ) {
    isPrime { 0 } = isPrime { 1 } = false ;;
    for i in range ( 2 , int ( sqrt ( sz ) ) + 1 ) :
        if (( isPrime { i } )) {
            for j in range ( i * i , sz , i ) :
                isPrime { j } = false ;;
        }
 }
public void minDifference ( L , R ) {
    var fst = 0 ;;
    for i in range ( L , R + 1 ) :
        if (( isPrime { i } )) {
            fst = i ;;
            break ;;
        }
     snd = 0 ;;
    for i in range ( fst + 1 , R + 1 ) :
        if (( isPrime { i } )) {
            snd = i ;;
            break ;;
        }
     if (( snd == 0 )) {
        return - 1 ;;
    }
     diff = snd - fst ;;
    left = snd + 1 ;;
    right = R ;;
    for i in range ( left , right + 1 ) :
        if (( isPrime { i } )) {
            if (( i - snd <= diff )) {
                fst = snd ;;
                var snd = i ;;
                var diff = snd - fst ;;
            }
         }
     return diff ;;
}
if (var __name__ == "__main__") {
    sieve ( ) ;;
    var L = 21 ; R = 50 ;;
    System.out.println ( minDifference ( L , R ) ) ;;
}
 