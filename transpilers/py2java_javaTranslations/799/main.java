import itertools.combinations;
public void find ( lst , n ) {
    System.out.println ( 'YES' if { 1 for r in range ( 1 , len ( lst ) + 1 ) for subset in combinations ( lst , r ) if sum ( subset ) == n } else 'NO' );
}
find ( { - 1 , 2 , 4 , 121 } , 5 );
