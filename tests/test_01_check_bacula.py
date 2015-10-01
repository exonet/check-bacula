import pytest
import check_bacula
from mock import patch, Mock
import MySQLdb

def test_00_main():

    # Without mocking mysql connection
    with pytest.raises(SystemExit):
        check_bacula.main()

    # With mocking

    with patch('MySQLdb.__init__') as mdb, \
            patch('MySQLdb.connect') as con, \
            patch('MySQLdb.cursors.DictCursor') as cur, \
            patch('smtplib.SMTP'):
        cur.side_effect=Exception('allalala')
        con.cursor.return_value = cur

        con.side_effect=Exception('allalala')
        mdb.connect.return_value = con
        check_bacula.main()
