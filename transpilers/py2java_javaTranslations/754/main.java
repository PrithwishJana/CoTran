public void isPeak ( arr , n , num , i , j ) {
    if (( i >= 0 and arr { i } > num )) {
        return false;
    }
     if (( j < n and arr { j } > num )) {
        return false;
    }
     return true;
}
public void isTrough ( arr , n , num , i , j ) {
    if (( i >= 0 and arr { i } < num )) {
        return false;
    }
     if (( j < n and arr { j } < num )) {
        return false;
    }
     return true;
}
public void System.out.printlnPeaksTroughs ( arr , n ) {
    System.out.println ( "Peaks : " , var end = "" );
    for i in range ( n ) :
        if (( isPeak ( arr , n , arr { i } , i - 1 , i + 1 ) )) {
            System.out.println ( arr { i } , end = " " );
        }
     System.out.println ( );
    System.out.println ( "Troughs : " , end = "" );
    for i in range ( n ) :
        if (( isTrough ( arr , n , arr { i } , i - 1 , i + 1 ) )) {
            System.out.println ( arr { i } , end = " " );
        }
 }
var arr = { 5 , 10 , 5 , 7 , 4 , 3 , 5 };
var n = len ( arr );
System.out.printlnPeaksTroughs ( arr , n );
