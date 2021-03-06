.. roamPy documentation master file, created by
   sphinx-quickstart on Fri Feb 11 12:55:18 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to roamPy's documentation!
==================================
roamPy is a python library of API wrapper functions to retrieve data from the
`roam.plus <https://roam.plus>`__ platform. Includes the ``Roam`` python
class which has one method corresponding to each API endpoint including,
Subscriptions, SubscriptionPeriods, Products and Licenses.

Installation
------------

``pip install roamPy``

Get Started
-----------

How to test connection to the Roam server:

::

   from roamPy import Roam
   import os

   #API Key stored as system variable
   token = os.environ.get('Roam_API_Key')

   #Instantiate object of Roam class
   roam = Roam(url=<base url of roam instance>, token=token)

   #Test connection
   print(roam.checkHeartbeat())

Successful Connection Output:

::

   {'data': None, 'meta': {'message': 'API ready for requests'}}

Request metadata for a given subscription using its id number:

::

   #Return Data for Subscription using ID.
   sub = roam.getOneSubscription(id = 'id number')

   print(sub)

Retreive data for all subscription periods between two dates:

::

   allSPBetween = roam.getSubscriptionPeriodsBetween(startDate='2020-01-01', endDate='2021-01-01')

   print(allSPBetween)

Retreive all licenses and relations:

::

   licRel = roam.getLicenseswRels(['licensePeriods', 'publisher'])

   print(licRel)



.. toctree::
   :maxdepth: 2
   :caption: Contents:

   source/api/Roam
  
  


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
