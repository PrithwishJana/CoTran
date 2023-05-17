import math;
public void bit ( x ) {
    var ans = 0;
    while (( x )) {
        x /= 2;
        ans = ans + 1;
    }
     return ans;
}
public void check ( d , x ) {
    if (( bit ( x / d ) <= bit ( d ) )) {
        return true;
    }
     return false ;;
}
public void bs ( n ) {
    var l = 1;
    r = int ( math . sqrt ( n ) );
    while (( l < r )) {
        m = int ( ( l + r ) / 2 );
        if (( check ( m , n ) )) {
            r = m;
        }
         else{
            l = m + 1;
        }
    }
     if (( check ( l , n ) == false )) {
        return math . floor ( l + 1 );
     }
     else{
        return math . floor ( l );
    }
}
public void countDivisor ( n ) {
    return n - bs ( n ) + 1;
}
var n = 5;
System.out.println ( countDivisor ( n ) );
