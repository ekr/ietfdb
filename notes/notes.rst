==============================================================================
			Datatracker Development Notes
==============================================================================

Introduction
============

This file should be ordered with the most recent entries at the top.

Before March 2014, notes on choices made and paths taken, to the extent they
have been written, has been sent by email and thus don't exist as a collection
in one place.

With my recent investigations of code analysis tools, I thought it might be
a good idea to start collecting these in one place for the project.

					`Henrik <henrik@levkowetz.com>, 23 Mar 2014`


Code Analysis Tools
===================

PyFlakes
--------

Pyflakes has proved robust and easy to work with, and has shown no false
positives in the messages provided.  It has been included in the form of a
standalone management command, as well as a test suite test.


Vulture
-------

Vulture has been a disappointment.  Given that the purpose of using it was to
discover dead code, it was necessary to extend the Vulture class to also parse
and process variables in template files, as these are points where reference
back to object methods and object attributes can be made.

Unfortunately, once this extension was in place, it turned out that the amount
of remaining false positives was unreasonably large, because Vulture fails to
understand that the declarative style of Django models (from
django.models.Model) and admin classes (from django.contrib.admin.ModelAdmin)
doesn't in fact constitute unused class attributes.

Finally, it turns out that Vulture is really simpleminded about what
constitutes usage.  It has one set of global lists for used functions, used
attributes, and used variables; any instance of overlapping function, method,
variable, or attribute naming across modules will result in one instance of
use in one module masking lack of usage in all other modules.

At the moment, it looks like it might be a better way forward to see if
PyFlakes could be extended with some dead code capability, than to continue to
pound on what seems to be a broken framework in Vulture.


PyLint
------

PyLint has been excluded from futher consideration because it doesn't only
parse the code, it also executes it, which comes with both a speed penalty and
the possibility of triggering unwanted side effects of doing an analysis run.


PyChecker
---------

PyChecker turned out to require much more fiddling than PyFlakes in order to
do the right thing, but once it was made to run on the datatracker code, and
ignore the django code, it didn't report anything that PyFlakes hadn't already
caught.


					`Henrik <henrik@levkowetz.com>, 23 Mar 2014`
