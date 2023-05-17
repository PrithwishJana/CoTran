var n = int ( input ( ) );
var s = input ( );
i = 0;
x = 0;
ans = 0;
for j in range ( 1 , n ) :
    if (s { j } == s { i } == 'x') {
        x += 1;
    }
     else{
        if (x > 1) {
            ans += x - 1;
        }
         var x = 0;
    }
    var i = j;
if (x > 1) {
    ans += x - 1;
}
 System.out.println ( ans );
