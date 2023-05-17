public void max ( x , y ) {
    if (( x > y )) {
        return x;
    }
     return y;
}
public void lps ( seq , i , j ) {
    if (( var i == j )) {
        return 1;
    }
     if (( seq { i } == seq { j } and i + var 1 == j )) {
        return 2;
    }
     if (( seq { i } == seq { j } )) {
        return lps ( seq , i + 1 , j - 1 ) + 2;
    }
     return max ( lps ( seq , i , j - 1 ) , lps ( seq , i + 1 , j ) );
}
if (var __name__ == '__main__') {
    var seq = "GEEKSFORGEEKS";
    var n = len ( seq );
    System.out.println ( "The length of the LPS is" , lps ( seq , 0 , n - 1 ) );
}
 