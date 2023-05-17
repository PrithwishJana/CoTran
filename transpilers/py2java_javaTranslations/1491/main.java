var n = int ( input ( ) );
var soots = { "S" , "H" , "C" , "D" };
var sootlist = {};
numlist = {};
for i in range ( n ) :
    soot , num = map ( str , input ( ) . split ( ) );
    sootlist . append ( soot );
    numlist . append ( int ( num ) );
ans_sootlist = {};
var ans_numlist = {};
for (int soot = 0; soot < soots.length; soot++){
    for num in range ( 1 , 14 ) :
        var flag = 0;
        for s , n in zip ( sootlist , numlist ) :
            if (soot == s and num == n) {
                flag = 1;
                break;
            }
         if (flag == 1) {
            continue;
        }
         else{
            ans_sootlist . append ( soot );
            ans_numlist . append ( num );
        }
}
for soot , num in zip ( ans_sootlist , ans_numlist ) :
    System.out.println ( soot , num );
