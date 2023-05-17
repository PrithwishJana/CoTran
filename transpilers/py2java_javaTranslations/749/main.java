public void bit_check ( n ) {
    if (( ( n & ( n - 1 ) ) == 0 )) {
        return true;
    }
     return false;
}
if (var __name__ == '__main__') {
    var n = 14;
    if (( bit_check ( n ) )) {
        System.out.println ( '1' );
    }
     else{
        System.out.println ( '0' );
    }
}
 