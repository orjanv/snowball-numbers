## Finding Snowball Numbers with Python

Inspired by an article at futilitycloset.com (http://www.futilitycloset.com/2014/12/28/snowball-numbers), I wrote a python program to look for such numbers. 

Basically, it takes a number and translates it into its english name and look for letter counts that ends up as a rolling snowball (ie. each letter counts increment by 1). If the current number isn't such a snowball number, the next number is looked at (+1). This is done until you stop the program.

![](http://www.futilitycloset.com/wp-content/uploads/2014/12/2014-12-28-snowball-numbers-11.png "Example snowball")

When such a number is found it is recorded to a file and sent by email to a given email address.

Note, this might take a while for two reasons, the program is far from optimized for speed and we need to look a long time for such numbers

### Running the script

Run the script as follows:

´´´python
$ python snowball.py NUMBER
´´´
where NUMBER is your starting point, ex 1 og 1000 or 100000000


### TODO

* Optimize the algorithms to run faster
* See if some tests can be shortened and improved
