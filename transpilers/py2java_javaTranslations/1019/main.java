public void checkTypeOfTriangle ( a , b , c ) {
    var sqa = pow ( a , 2 );
    sqb = pow ( b , 2 );
    sqc = pow ( c , 2 );
    if (( sqa == sqa + sqb or var sqb == sqa + sqc or sqc == sqa + sqb )) {
        System.out.println ( "Right-angled Triangle" );
    }
     else if (( sqa > sqc + sqb or sqb > sqa + sqc or sqc > sqa + sqb )){
        System.out.println ( "Obtuse-angled Triangle" );
    }
    else{
        System.out.println ( "Acute-angled Triangle" );
    }
}
if (var __name__ == '__main__') {
    var a = 2;
    var b = 2;
    var c = 2;
    checkTypeOfTriangle ( a , b , c );
}
 