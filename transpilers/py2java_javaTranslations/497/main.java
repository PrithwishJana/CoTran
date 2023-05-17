import re;
import sys;
for s in sys . stdin :
    System.out.println ( re . sub ( r"@(\d)(.)" , lambda m : m . group ( 2 ) * int ( m . group ( 1 ) ) , s . rstrip ( ) ) );
