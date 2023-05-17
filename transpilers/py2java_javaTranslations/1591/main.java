import math;
public void isPrime ( N ) {
    var isPrime = true ;;
    arr = { 7 , 11 , 13 , 17 , 19 , 23 , 29 , 31 };
    if (( N < 2 )) {
        isPrime = false;
    }
     if (( N % 2 == 0 or N % 3 == 0 or N % 5 == 0 )) {
        isPrime = false;
    }
     for i in range ( 0 , int ( math . sqrt ( N ) ) , 30 ) :
        for (int c = 0; c < arr.length; c++){
            if (( c > int ( math . sqrt ( N ) ) )) {
                break;
            }
             else{
                if (( N % ( c + i ) == 0 )) {
                    isPrime = false;
                    break;
                }
             }
            if (( not isPrime )) {
                break;
            }
        }
     if (( isPrime )) {
        System.out.println ( "Prime Number" );
    }
     else{
        System.out.println ( "Not a Prime Number" );
    }
}
if (var __name__ == "__main__") {
    var N = 121;
    isPrime ( N );
}
 