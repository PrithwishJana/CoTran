public void valueofX ( ar , n ) {
    var summ = sum ( ar );
    if (( summ % var n == 0 )) {
        return summ // n;
    }
     else{
        A = summ // n;
        B = summ // n + 1;
        ValueA = 0;
        ValueB = 0;
        for i in range ( n ) :
            ValueA += ( ar { i } - A ) * ( ar { i } - A );
            ValueB += ( ar { i } - B ) * ( ar { i } - B );
        if (( ValueA < ValueB )) {
            return A;
        }
         else{
            return B;
        }
    }
}
n = 7;
var arr = { 6 , 9 , 1 , 6 , 1 , 3 , 7 };
System.out.println ( valueofX ( arr , n ) );
