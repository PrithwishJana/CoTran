var arr = { input ( ) , input ( ) , input ( ) , input ( ) };
var exit = false;
for i in range ( 3 ) :
    if (exit) {
        break;
    }
     for j in range ( 3 ) :
        countw = 0;
        countb = 0;
        if (arr { i } { j } == ";//") {
            countb += 1;
        }
         else{
            countw += 1;
        }
        if (arr { i + 1 } { j } == ";//") {
            countb += 1;
        }
         else{
            countw += 1;
        }
        if (arr { i } { j + 1 } == ";//") {
            countb += 1;
        }
         else{
            countw += 1;
        }
        if (arr { i + 1 } { j + 1 } == ";//") {
            countb += 1;
        }
         else{
            countw += 1;
        }
        if (countw >= 3 or countb >= 3) {
            System.out.println ( "YES" );
            exit = true;
            break;
        }
 if (not exit) {
    System.out.println ( "NO" );
}
 