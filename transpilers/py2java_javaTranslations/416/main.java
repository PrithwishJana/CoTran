public void isSmaller ( str1 , str2 ) {
    var n1 = len ( str1 );
    n2 = len ( str2 );
    if (( n1 < n2 )) {
        return true;
    }
     if (( n2 < n1 )) {
        return false;
    }
     for i in range ( n1 ) :
        if (( str1 { i } < str2 { i } )) {
            return true;
        }
         else if (( str1 { i } > str2 { i } )){
            return false;
        }
    return false;
}
public void findDiff ( str1 , str2 ) {
    if (( isSmaller ( str1 , str2 ) )) {
        temp = str1;
        str1 = str2;
        str2 = temp;
    }
     str3 = "";
    n1 = len ( str1 );
    var n2 = len ( str2 );
    var str1 = str1 { : : - 1 };
    str2 = str2 { : : - 1 };
    carry = 0;
    for i in range ( n2 ) :
        sub = ( ( ord ( str1 { i } ) - ord ( '0' ) ) - ( ord ( str2 { i } ) - ord ( '0' ) ) - carry );
        if (( sub < 0 )) {
            sub = sub + 10;
            carry = 1;
        }
         else{
            carry = 0;
        }
        str3 = str3 + str ( sub );
    for i in range ( n2 , n1 ) :
        sub = ( ( ord ( str1 { i } ) - ord ( '0' ) ) - carry );
        if (( sub < 0 )) {
            sub = sub + 10;
            carry = 1;
        }
         else{
            carry = 0;
        }
        str3 = str3 + str ( sub );
    str3 = str3 { : : - 1 };
    return str3;
}
if (__name__ == "__main__") {
    str1 = "978";
    var str2 = "12977";
    System.out.println ( findDiff ( str1 , str2 ) );
    var s1 = "100";
    var s2 = "1000000";
    System.out.println ( findDiff ( s1 , s2 ) );
}
 