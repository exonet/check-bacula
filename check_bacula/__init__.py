import os
import sys
import MySQLdb
import smtplib
import socket
from ConfigParser import SafeConfigParser


def init(configDir):

    cfg = SafeConfigParser()

    if not os.path.isdir(configDir):
        os.mkdir(configDir, 0700)
    else:
        # Ensure proper permissions.
        os.chmod(configDir, 0700)

    if os.path.isfile(os.path.join(configDir, 'config.ini')):
        cfg.read(os.path.join(configDir, 'config.ini'))

    else:
        # Create a default config.ini.
        cfg.add_section('database')
        cfg.set('database', 'hostname', 'localhost')
        cfg.set('database', 'database', 'bacula')
        cfg.set('database', 'username', 'bacula')
        cfg.set('database', 'password', '')

        cfg.add_section('mail')
        cfg.set('mail', 'smtpserver', '')
        cfg.set('mail', 'from', '')
        cfg.set('mail', 'to', '')

        with open(os.path.join(configDir, 'config.ini'), 'wb') as fh:
            cfg.write(fh)

    return cfg


def main():
    cfg = init(os.path.join(os.path.expanduser("~"), '.check_bacula'))

    fromaddr = cfg.get('mail', 'from')
    to = cfg.get('mail', 'to')

    # Try creating a database connection.
    try:
        con = MySQLdb.connect(cfg.get('database', 'hostname'), cfg.get('database', 'username'),
                              cfg.get('database', 'password'), cfg.get('database', 'database'))
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0], e.args[1])
        print "Check %s for correct database credentials." % os.path.join(
            os.path.expanduser("~"), '.check_bacula/config.ini')
        sys.exit(1)

    cur = con.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("""SELECT JobID, Name FROM Job WHERE JobStatus<>'T'
    AND StartTime > DATE_SUB(NOW(), INTERVAL 1 DAY)
    AND EndTime > DATE_SUB(NOW(), INTERVAL 1 DAY)""")
    if cur.rowcount:
        errorrow = cur.fetchone()
        while errorrow is not None:
            smtp = smtplib.SMTP(cfg.get('mail', 'smtpserver'))

            # Send error mail.
            hostname = socket.gethostname()
            subject = "Bacula job %s (%s) failed on %s" % (
                errorrow['JobID'], errorrow['Name'], hostname)
            msg = ""

            # Get log messages.
            logcur = con.cursor(MySQLdb.cursors.DictCursor)
            logcur.execute("SELECT Time, LogText FROM Log WHERE JobId=%s", errorrow['JobID'])
            if logcur.rowcount:
                logrow = logcur.fetchone()
                while logrow is not None:
                    msg += "%s: %s" % (logrow['Time'], logrow['LogText'])
                    logrow = logcur.fetchone()

            mail = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (fromaddr, to, subject, msg)

            smtp.sendmail(fromaddr, [to], mail)
            errorrow = cur.fetchone()
