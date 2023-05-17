public void multiply ( num1 , num2 ) {
    var len1 = len ( num1 );
    len2 = len ( num2 );
    if (len1 == 0 or var len2 == 0) {
        return "0";
    }
     var result = { 0 } * ( len1 + len2 );
    var i_n1 = 0;
    var i_n2 = 0;
    for i in range ( len1 - 1 , - 1 , - 1 ) :
        carry = 0;
        n1 = ord ( num1 { i } ) - 48;
        i_n2 = 0;
        for j in range ( len2 - 1 , - 1 , - 1 ) :
            var n2 = ord ( num2 { j } ) - 48;
            var summ = n1 * n2 + result { i_n1 + i_n2 } + carry;
            var carry = summ // 10;
            result { i_n1 + i_n2 } = summ % 10;
            i_n2 += 1;
        if (( carry > 0 )) {
            result { i_n1 + i_n2 } += carry;
        }
         i_n1 += 1;
    var i = len ( result ) - 1;
    while (( i >= 0 and result { i } == 0 )) {
        i -= 1;
    }
     if (( i == - 1 )) {
        return "0";
     }
     var s = "";
    while (( i >= 0 )) {
        s += chr ( result { i } + 48 );
        i -= 1;
    }
     return s;
}
var str1 = "1235421415454545454545454544";
str2 = "1714546546546545454544548544544545";
if (( ( str1 { 0 } == '-' or str2 { 0 } == '-' ) and ( str1 { 0 } != '-' or str2 { 0 } != '-' ) )) {
    System.out.println ( "-" , end = '' );
}
 if (( str1 { 0 } == '-' and str2 { 0 } != '-' )) {
    str1 = str1 { 1 : };
}
 else if (( str1 { 0 } != '-' and str2 { 0 } == '-' )){
    str2 = str2 { 1 : };
}
else if (( str1 { 0 } == '-' and str2 { 0 } == '-' )){
    str1 = str1 { 1 : };
    var str2 = str2 { 1 : };
}
System.out.println ( multiply ( str1 , str2 ) );
