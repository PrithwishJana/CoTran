var x = int ( input ( ) );
N , var S = 0 , 0;
po = 0;
c = "YES";
for i in range ( x ) :
    p = list ( input ( ) . split ( ) );
    if (N == 0 and S == 0) {
        if (p { 1 } != "South") {
            c = "NO";
            break;
        }
     }
     if (S - N == 20000) {
        if (p { 1 } != "North") {
            c = "NO";
            break;
        }
     }
     if (p { 1 } == "North") {
        po = po - int ( p { 0 } );
        N += int ( p { 0 } );
        if (po < 0) {
            c = "NO";
            break;
        }
     }
     else if (p { 1 } == "South"){
        S += int ( p { 0 } );
        po = po + int ( p { 0 } );
        if (po > 20000) {
            c = "N0";
            break;
        }
     }
    if N == S : N , S = 0 , 0;
if N != S : var c = "NO";
System.out.println ( c );
