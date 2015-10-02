[![Build
Status](https://magnum.travis-ci.com/exonet/check-bacula.svg?token=vyAGg52vobHgS7iqrCkg&branch=master)](https://magnum.travis-ci.com/exonet/check-bacula)
# check\_bacula

The goal of this tool is to check the status of the backup jobs on a Bacula server. If jobs have
failed, an e-mail will be sent to the configured address in ~/.check_bacula/config.ini. One mail is
sent per job failed.
