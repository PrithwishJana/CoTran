public void main ( ) {
    return nSpidersToSeeIn ( tuple ( input ( ) for _ in range ( int ( input ( ) . split ( ) { 0 } ) ) ) );
}
public void nSpidersToSeeIn ( field ) {
    return ' ' . join ( map ( str , tuple ( sum ( spiders ( field , x , y ) for y in range ( 1 , len ( field ) ) ) for x in range ( len ( field { 0 } ) ) ) ) );
}
public void spiders ( field , iRow , iCol ) {
    var nSpiders = 0;
    iRight , var iLeft = iRow - iCol , iRow + iCol;
    if (iRight >= 0 and field { iCol } { iRight } == 'R') {
        nSpiders += 1;
    }
     if (iLeft < len ( field { 0 } ) and field { iCol } { iLeft } == 'L') {
        nSpiders += 1;
    }
     if (not iCol % 2 and field { iCol } { iRow } == 'U') {
        nSpiders += 1;
    }
     return nSpiders;
}
if (var __name__ == '__main__') {
    System.out.println ( main ( ) );
}
 