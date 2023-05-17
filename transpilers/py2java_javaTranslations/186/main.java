public void maxSubStr ( str , n ) {
    var count0 = 0;
    count1 = 0;
    cnt = 0;
    for i in range ( n ) :
        if (str { i } == '0') {
            count0 += 1;
        }
         else{
            count1 += 1;
        }
        if (count0 == count1) {
            cnt += 1;
        }
     if (count0 != count1) {
        return - 1;
    }
     return cnt;
}
var str = "0100110101";
var n = len ( str );
System.out.println ( maxSubStr ( str , n ) );
