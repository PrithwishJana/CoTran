var numbers = list ( map ( int , input ( ) . split ( ) ) );
var start = 0;
arr = {};
count = 0;
for i in range ( 0 , numbers { 0 } ) :
    string = "";
    next = start;
    for j in range ( 0 , numbers { 0 } ) :
        if (count < numbers { 1 }) {
            if (j == next) {
                string += 'L';
                count += 1;
                next += 2;
                if (next >= numbers { 0 }) {
                    start = 1 if start == 0 else 0;
                }
             }
             else{
                string += "S";
            }
        }
         else{
            string += "S";
        }
    arr . append ( string );
if (count < numbers { 1 }) {
    System.out.println ( "NO" );
}
 else{
    System.out.println ( "YES" );
    for (int i = 0; i < arr.length; i++){
        System.out.println ( i );
    }
}
