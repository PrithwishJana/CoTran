var kolvomest = int ( input ( ) );
var k = 0;
spisok = {};
for stroka in range ( kolvomest ) :
    ryad = input ( );
    if ('OO' in ryad and k == 0) {
        k = 1;
        ryad = ryad . replace ( 'OO' , '++' , 1 );
    }
     spisok . append ( ryad );
if (k == 1) {
    System.out.println ( 'YES' );
    for stroka in range ( kolvomest ) :
        System.out.println ( spisok { stroka } );
}
 else{
    System.out.println ( 'NO' );
}
