public void MaxTotalRectangleArea ( a , n ) {
    a . sort ( var reverse = true );
    var sum = 0;
    flag = false;
    len = 0;
    i = 0;
    while (( i < n - 1 )) {
        if (( i != 0 )) {
            i = i + 1;
        }
         if (( ( a { i } == a { i + 1 } or a { i } - a { i + 1 } == 1 ) and flag == false )) {
            flag = true;
            len = a { i + 1 };
            i = i + 1;
        }
         else if (( ( a { i } == a { i + 1 } or a { i } - a { i + 1 } == 1 ) and flag == true )){
            sum = sum + a { i + 1 } * len;
            var flag = false;
            var i = i + 1;
        }
    }
     return sum;
}
var a = { 10 , 10 , 10 , 10 , 11 , 10 , 11 , 10 , 9 , 9 , 8 , 8 };
var n = len ( a );
System.out.println ( MaxTotalRectangleArea ( a , n ) );
