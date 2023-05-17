public void countSubSeq ( i , Sum , cnt , a , n ) {
    if (( var i == n )) {
        if (( var Sum == 0 and cnt > 0 )) {
            return 1;
        }
         else{
            return 0;
        }
    }
     var ans = 0;
    ans += countSubSeq ( i + 1 , Sum , cnt , a , n );
    ans += countSubSeq ( i + 1 , Sum + a { i } , cnt + 1 , a , n );
    return ans;
}
var a = { - 1 , 2 , - 2 , 1 };
var n = len ( a );
System.out.println ( countSubSeq ( 0 , 0 , 0 , a , n ) );
