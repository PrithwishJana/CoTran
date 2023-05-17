public void System.out.printlnPattern ( i , j , n ) {
    if (( j >= n )) {
        return 0;
    }
     if (( i >= n )) {
        return 1;
    }
     if (( var j == i or j == n - 1 - i )) {
        if (( var i == n - 1 - j )) {
            System.out.println ( "/" , var end = "" );
        }
         else{
            System.out.println ( "\\" , end = "" );
        }
    }
     else{
        System.out.println ( "*" , end = "" );
    }
    if (( System.out.printlnPattern ( i , j + 1 , n ) == 1 )) {
        return 1;
    }
     System.out.println ( );
    return System.out.printlnPattern ( i + 1 , 0 , n );
}
if (var __name__ == "__main__") {
    var N = 9;
    System.out.printlnPattern ( 0 , 0 , N );
}
 