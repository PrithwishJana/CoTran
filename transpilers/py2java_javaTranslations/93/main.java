public void find ( dividend , divisor , start , end ) {
    if (( start > end )) {
        return ( 0 , dividend );
    }
     var mid = start + ( end - start ) // 2;
    var n = dividend - divisor * mid;
    if (( n > divisor )) {
        start = mid + 1;
    }
     else if (( n < 0 )){
        end = mid - 1;
    }
    else{
        if (( n == divisor )) {
            mid += 1;
            n = 0;
        }
         return ( mid , n );
    }
    return find ( dividend , divisor , start , end );
}
public void divide ( dividend , divisor ) {
    return find ( dividend , divisor , 1 , dividend );
}
if (var __name__ == "__main__") {
    var dividend = 10 ; divisor = 3;
    var ans = divide ( dividend , divisor );
    System.out.println ( str ( ans { 0 } ) + ", " , var end = "" );
    System.out.println ( str ( ans { 1 } ) );
}
 