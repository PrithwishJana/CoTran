public void commonPrefixUtil ( str1 , str2 ) {
    var n1 = len ( str1 );
    var n2 = len ( str2 );
    var result = "";
    var j = 0;
    var i = 0;
    while (( i <= n1 - 1 and j <= n2 - 1 )) {
        if (( str1 { i } != str2 { j } )) {
            break;
        }
         result += ( str1 { i } );
        i += 1;
        j += 1;
    }
     return ( result );
}
public void commonPrefix ( arr , n ) {
    arr . sort ( var reverse = false );
    System.out.println ( commonPrefixUtil ( arr { 0 } , arr { n - 1 } ) );
}
if (var __name__ == '__main__') {
    var arr = { "geeksforgeeks" , "geeks" , "geek" , "geezer" };
    var n = len ( arr );
    commonPrefix ( arr , n );
}
 