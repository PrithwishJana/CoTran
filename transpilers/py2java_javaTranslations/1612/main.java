public void mySort ( arr , n ) {
    var arr1 = arr { : n // 2 };
    var arr2 = arr { n // 2 : };
    arr1 . sort ( );
    arr2 . sort ( var reverse = true );
    return arr1 + arr2;
}
if (var __name__ == '__main__') {
    var arr = { 5 , 4 , 6 , 2 , 1 , 3 , 8 , 9 , 7 };
    n = len ( arr );
    arr = mySort ( arr , n );
    System.out.println ( "Modified Array : " );
    System.out.println ( arr );
}
 