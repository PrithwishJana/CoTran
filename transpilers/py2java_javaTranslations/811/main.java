var N = int ( input ( ) );
var X = input ( );
var D = int ( input ( ) );
ans = list ( X );
done = { false } * N;
for i in range ( N ) :
    if (D == 0) {
        break;
    }
     if (ans { i } == "0") {
        ans { i } = "1";
        done { i } = true;
        D -= 1;
    }
 for i in range ( N ) { : : - 1 } :
    if (D == 0) {
        break;
    }
     if (ans { i } == "1" and not done { i }) {
        ans { i } = "0";
        D -= 1;
    }
 System.out.println ( "" . join ( ans ) );
