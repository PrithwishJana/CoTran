import math as mt;
public void findAnswer ( str1 , str2 , n ) {
    l , var r = 0 , 0;
    ans = 2;
    for i in range ( n ) :
        if (( str1 { i } != str2 { i } )) {
            l = i;
            break;
        }
     for i in range ( n - 1 , - 1 , - 1 ) :
        if (( str1 { i } != str2 { i } )) {
            r = i;
            break;
        }
     if (( r < l )) {
        return 26 * ( n + 1 );
    }
     else if (( var l == r )){
        return ans;
    }
    else{
        for i in range ( l + 1 , r + 1 ) :
            if (( str1 { i } != str2 { i - 1 } )) {
                ans -= 1;
                break;
            }
         for i in range ( l + 1 , r + 1 ) :
            if (( str1 { i - 1 } != str2 { i } )) {
                ans -= 1;
                break;
            }
         return ans;
    }
}
var str1 = "toy";
var str2 = "try";
var n = len ( str1 );
System.out.println ( findAnswer ( str1 , str2 , n ) );
