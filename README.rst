.. image:: https://magnum.travis-ci.org/exonet/check-bacula.svg?token=vyAGg52vobHgS7iqrCkg&branch=master
  :target: https://magnum.travis-ci.org/exonet/check-bacula
  :alt: Build Status

.. image:: https://coveralls.io/repos/exonet/check-bacula/badge.svg?branch=master&service=github
  :target: https://coveralls.io/github/exonet/check-bacula?branch=master

The goal of this tool is to check the status of the backup jobs on a Bacula server. If jobs have
failed, an e-mail will be sent to the configured address in ~/.check_bacula/config.ini. One mail is
sent per job failed.
