var s = list ( input ( ) );
var x = true;
dt = {};
for (int i = 0; i < s.length; i++){
    if (i in dt) {
        dt { i } += 1;
    }
     else{
        dt { i } = 1;
    }
}
cnt = 0;
x = true;
for key , value in dt . items ( ) :
    if (value % 2 != 0 and cnt < 1) {
        cnt += 1;
    }
     else if (value % 2 != 0 and cnt >= 1){
        x = false;
        break;
    }
if (x) {
    System.out.println ( "First" );
}
 else if (not x and len ( s ) % var 2 == 0){
    System.out.println ( "Second" );
}
else if (not x and len ( s ) % 2 != 0){
    System.out.println ( "First" );
}
