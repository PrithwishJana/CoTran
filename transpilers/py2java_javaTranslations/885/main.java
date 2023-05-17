public void extractMaximum ( ss ) {
    num , var res = 0 , 0;
    for i in range ( len ( ss ) ) :
        if (ss { i } >= "0" and ss { i } <= "9") {
            num = num * 10 + int ( int ( ss { i } ) - 0 );
        }
         else{
            res = max ( res , num );
            var num = 0;
        }
    return max ( res , num );
}
var ss = "100klh564abc365bg";
System.out.println ( extractMaximum ( ss ) );
