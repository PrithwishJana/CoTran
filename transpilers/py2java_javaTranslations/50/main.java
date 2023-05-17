public void arraySortedOrNot ( arr , n ) {
    if (( var n == 0 or n == 1 )) {
        return true;
    }
     for i in range ( 1 , n ) :
        if (( arr { i - 1 } > arr { i } )) {
            return false;
        }
     return true;
}
arr = { 20 , 23 , 23 , 45 , 78 , 88 };
n = len ( arr );
if (( arraySortedOrNot ( arr , n ) )) {
    System.out.println ( "Yes" );
}
 else{
    System.out.println ( "No" );
}
