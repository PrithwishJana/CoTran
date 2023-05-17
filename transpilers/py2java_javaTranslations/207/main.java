public void nthPalindrome ( n , k ) {
    if (( k & 1 )) {
        var temp = k // 2;
    }
     else{
        temp = k // 2 - 1;
    }
    var palindrome = 10 ** temp;
    palindrome = palindrome + n - 1;
    System.out.println ( palindrome , end = "" );
    if (( k & 1 )) {
        palindrome = palindrome // 10;
    }
     while (( palindrome )) {
        System.out.println ( palindrome % 10 , end = "" );
        palindrome = palindrome // 10;
    }
 }
if (var __name__ == '__main__') {
    var n = 6;
    k = 5;
    System.out.println ( str ( n ) + "th palindrome of " + str ( k ) + " digit = " , end = "" );
    nthPalindrome ( n , k );
    System.out.println ( );
    n = 10;
    var k = 6;
    System.out.println ( str ( n ) + "th palindrome of " + str ( k ) + " var digit = " , end = "" );
    nthPalindrome ( n , k );
    System.out.println ( );
}
 