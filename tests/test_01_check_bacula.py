import pytest
import check_bacula
from mock import patch


def test_00_main():

    # Without mocking mysql connection.
    with pytest.raises(SystemExit):
        check_bacula.main()

    # With mocking.
    with patch('MySQLdb.__init__') as mdb, \
            patch('MySQLdb.connect') as con, \
            patch('smtplib.SMTP'):

        con.return_value.cursor.return_value.fetchone.side_effect = [
            {'JobID': 1, 'Name': 'foo'},
            {'Time': 1, 'LogText': 'foo'},
            None
        ]
        mdb.connect.return_value = con
        with pytest.raises(StopIteration):
            check_bacula.main()
