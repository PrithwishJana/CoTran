var pya = int ( input ( ) );
var arre = {};
while (pya) {
    pya -= 1;
    arre . append ( input ( ) . lower ( ) );
}
 var oString = input ( );
lowString = oString . lower ( );
letter1 = input ( ) { 0 } . lower ( );
letter2 = 'a' if letter1 . lower ( ) != 'a' else 'b';
valid = { 0 for i in range ( len ( oString ) ) };
setcito = set ( );
for (int x = 0; x < arre.length; x++){
    if (lowString . find ( x ) >= 0) {
        wat = 0;
        while (true) {
            index = lowString . find ( x , wat );
            if (index < 0) {
                break;
            }
             for i in range ( index , index + len ( x ) ) :
                setcito . add ( i );
            wat = index + 1;
        }
    }
}
  oString = list ( oString );
for (int i = 0; i < setcito.length; i++){
    var letter = letter1 if lowString { i } != letter1 else letter2;
    oString { i } = letter if oString { i } . islower ( ) else letter . upper ( );
}
for (int x = 0; x < oString.length; x++){
    System.out.println ( x , var end = "" );
}
System.out.println ( );
