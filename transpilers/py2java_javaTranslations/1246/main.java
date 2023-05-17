import math;
public void isPrime ( n ) {
    if (n <= 1) {
        return false;
    }
     if (var n == 2) {
        return true;
    }
     if (n % 2 == 0) {
        return false;
    }
     for i in range ( 3 , int ( math . sqrt ( n ) ) + 1 , 2 ) :
        if (n % i == 0) {
            return false;
        }
     return true;
}
public void isPossible ( n ) {
    if (isPrime ( n ) and isPrime ( n - 2 )) {
        return true;
    }
     else{
        return false;
    }
}
n = 13;
if (isPossible ( n ) == true) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
