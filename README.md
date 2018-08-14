# arkham_horror

A terminal utility to automate randomisation for Arkham Horror LCG.

Disclaimer: I do not own any rights to the Arkham Horror property, etc., etc. The script is provided without any warranty under the GNU general public license.

## using this utility

clone the repo using

`git clone https://github.com/vmikulik/arkham_horror.git`

navigate to the resulting directory, and run the script using 

`python arkham.py [-h] [-a ADD] [-r RM] CAMPAIGN DIFFICULTY`

`
positional arguments:
  CAMPAIGN           The name of the campaign being played
  DIFFICULTY         The difficulty level

optional arguments:
  -h, --help         show this help message and exit
  -a ADD, --add ADD  Add this token to the specified pool
  -r RM, --rm RM     Remove this token from the specified pool
`
