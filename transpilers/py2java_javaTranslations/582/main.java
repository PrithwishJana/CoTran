var t = int ( input ( ) );
while (t > 0) {
    var s = input ( );
    var flag = false if s { - 1 } != 'B' else true;
    if (flag) {
        summ = 0;
        for (int c = 0; c < s.length; c++){
            if (c == 'A') {
                summ += 1;
            }
             else{
                summ -= 1;
            }
            if (summ < 0) {
                flag = false;
                break;
            }
        }
     }
     if (flag) {
        System.out.println ( "YES" );
    }
     else{
        System.out.println ( "NO" );
    }
    t -= 1;
}
 