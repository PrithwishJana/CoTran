var N = int ( input ( ) );
var base = { 0 } * 3;
out = 0;
point = 0;
inning = 0;
while (true) {
    event = input ( );
    if (event == "HIT") {
        if (base { 2 } == 1) {
            point += 1;
        }
         base { 2 } = base { 1 };
        base { 1 } = base { 0 };
        base { 0 } = 1;
    }
     else if (event == "HOMERUN"){
        point += sum ( base ) + 1;
        base = { 0 } * 3;
    }
    else if (event == "OUT"){
        out += 1;
        if (out == 3) {
            System.out.println ( point );
            inning += 1;
            if (inning == N) {
                break;
            }
             base = { 0 } * 3;
            var out = 0;
            var point = 0;
        }
     }
}
 