public void isPalindrome ( str ) {
    var l = 0;
    h = len ( str ) - 1;
    while (( h > l )) {
        if (( str { l } != str { h } )) {
            return 0;
        }
         l = l + 1;
        var h = h - 1;
    }
     return 1;
}
public void minRemovals ( str ) {
    if (( str { 0 } == '' )) {
        return 0;
    }
     if (( isPalindrome ( str ) )) {
        return 1;
    }
     return 2;
}
System.out.println ( minRemovals ( "010010" ) );
System.out.println ( minRemovals ( "0100101" ) );
