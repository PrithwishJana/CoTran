public void solve ( a , b ) {
    var l = len ( a );
    var min = 0;
    var max = 0;
    for i in range ( l ) :
        if (( a { i } == '+' or b { i } == '+' or a { i } != b { i } )) {
            max += 1;
        }
         if (( a { i } != '+' and b { i } != '+' and a { i } != b { i } )) {
            min += 1;
        }
     System.out.println ( min + max );
}
if (var __name__ == '__main__') {
    var s1 = "a+c";
    var s2 = "++b";
    solve ( s1 , s2 );
}
 