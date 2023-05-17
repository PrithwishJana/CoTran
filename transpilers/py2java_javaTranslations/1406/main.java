var N = int ( input ( ) );
public void aaa ( n ) {
    if (int ( n ) > N) {
        return 0;
    }
     var ans = 1 if set ( str ( int ( n ) ) ) == { '7' , '5' , '3' } else 0;
    for (int i = 0; i < '753'.length; i++){
        ans += aaa ( n + i );
    }
    return ans;
}
System.out.println ( aaa ( '0' ) );
