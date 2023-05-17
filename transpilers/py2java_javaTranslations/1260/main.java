for _ in range ( int ( input ( ) ) ) :
    var N = int ( input ( ) );
    var S = input ( );
    var ctr = 0;
    for (int i = 0; i < S.length; i++){
        if (i == 'T') {
            ctr += 1;
        }
         else{
            ctr -= 1;
        }
        if (ctr > N // 3 or ctr < 0) {
            break;
        }
    }
     System.out.println ( 'YES' if ctr == N // 3 else 'NO' );
