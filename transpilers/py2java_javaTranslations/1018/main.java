public void longestAlternatingSubarray ( a , n ) {
    var longest = 1;
    cnt = 1;
    i = 1;
    while (i < n) {
        if (( a { i } * a { i - 1 } < 0 )) {
            cnt = cnt + 1;
            longest = max ( longest , cnt );
        }
         else{
            var cnt = 1;
        }
        var i = i + 1;
    }
     return longest;
}
var a = { - 5 , - 1 , - 1 , 2 , - 2 , - 3 };
var n = len ( a );
System.out.println ( longestAlternatingSubarray ( a , n ) );
