var x = int ( input ( ) );
System.out.println ( f'{x:032b}' );
System.out.println ( f'{~x & 0xffffffff:032b}' );
System.out.println ( f'{x << 1 & 0xffffffff:032b}' );
System.out.println ( f'{x >> 1:032b}' );
