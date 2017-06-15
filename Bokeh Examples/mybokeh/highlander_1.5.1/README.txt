/*------------------------------------------------------------------
Project:    Highland
Author:     Simpleqode
URL:        http://simpleqode.com/
            https://twitter.com/YevSim
            https://www.facebook.com/simpleqode
Version:    1.5.1
Created:        11/03/2014
Last change:    06/07/2015
-------------------------------------------------------------------*/

=====================
THE HIGHLAND TEMPLATE
=====================

GENERAL INSTRUCTIONS
====================

Setting up the contact form
---------------------------

This template contains a fully functioning PHP contact form with spam protection powered by reCaptcha. 
Note: The contact form will not work in your local environment without a server that supports PHP. 
In order to set up the contact form, please follow the steps below:

1. Open the /config.php file and fill out the required information:

 - reCaptcha Site ($publickey) and Secret ($privatekey) keys.
 Please go to https://www.google.com/recaptcha/admin/create if you don't have the keys yet.
 - Sender name and email address ($mail_sender)
 This is a name and email address you will see in the вЂњFrom:вЂќ line of new emails you will receive.
 - Your email address ($to_email)
 This is an email address new emails will be sent to.
 - Email subject ($mail_subject)
 This is a subject of new emails you will receive.

2. In /contact.html you need to insert your reCaptcha Site key (see Step 1) at the end of this line:

<div class="g-recaptcha" data-sitekey="YOUR_SITE_KEY"></div> (e.g. <div class="g-recaptcha" data-sitekey="6LcU9QETAAAAABOKm4BoKrhzTvdIsrzXTsl4sgpY"></div>)

3. Save all files.


SOURCES AND CREDITS
===================

We've used the following third party images, icons, and other files listed:

General
-------

1. Bootstrap

URL:        http://getbootstrap.com/
AUTHOR:     @mdo and @fat
LICENSE:    MIT License

2. Font Awesome

URL:        http://fontawesome.io/
AUTHOR:     Dave Gandy
LICENSE:    MIT license


CSS Files: 
----------

1. CSS Animation

URL:        https://daneden.me/animate/
AUTHOR:     Dan Eden
LICENSE:    MIT license


JS Plugins
----------

1. Scroll to top script

URL:        http://www.dynamicdrive.com/dynamicindex3/scrolltop.htm
AUTHOR:     Dynamic Drive
LICENSE:    http://www.dynamicdrive.com/notice.htm

2. Isotope

URL:        http://isotope.metafizzy.co/
AUTHOR:     David DeSandro
LICENSE:    Commercial Developer Lisence (licenses/isotope_commercial_developer_license.pdf)

3. Imagesloaded

URL:        http://imagesloaded.desandro.com/
AUTHOR:     https://github.com/desandro/imagesloaded/graphs/contributors
LICENSE:    MIT license


Images
------

1. Showcase

URL: http://www.pixeden.com/psd-web-elements/responsive-showcase-psd
AUTHOR: Pixeden.com
LICENSE: Royalty free for use in both personal and commercial projects

2. Pictures: 

Showcase: 

URL: http://www.flickr.com/photos/8106459@N07/3060682780/sizes/o/in/photostream/
AUTHOR: David-O
LICENSE: Creative Commons

Other:

URL: http://www.flickr.com/photos/xjrlokix/
AUTHOR: Ben Fredericson
LICENSE: Creative Commons


reCAPTCHA
---------

Copyright (c) 2007 reCAPTCHA -- http://recaptcha.net

AUTHORS: Mike Crawford
         Ben Maurer


=========
CHANGELOG
=========

Version 1.5.1 - 06.07.2015

 - Update Bootstrap to v3.3.5
 - Update Isotope to v2.2.0
 - Update reCaptcha (contact.js, sendmail.php, contact.html)
 - Remove /recaptcha folder

Version 1.5.0 - 20.02.2015

 - Update Bootstrap to v3.3.2
 - Update Font Awesome to v4.3.0
 - Update Isotope to v2.1.0
 - Update jQuery to v1.11.2
 - Move original Bootstrap CSS, JS and font files into separate folders
 - Rename Font Awesome folder
 - Move Isotope JS into /js folder
 - Remove Isotope CSS
 - Add imagesloaded plugin
 - Improve homepage services block markup and CSS
 - Improve gallery bubbles and gallery text blocks markup, CSS and JS
 - Correct @media breakpoints values in custom.css
 - Add missing input labels to sign-up form
 - Replace lost password javascript with native collapse plugin
 - Use .embed-responsive instead of .google-maps for responsive embed
 - Fix 404 error page background for IE
 - Remove UI elements sidebar affix
 - Add functional PHP contact form to contact.html


Version 1.4 - 07/03/2014

 - NEW: Isotope Plugin added
 - NEW: Homepage Slider added
 - UPDATED: Twitter Bootstrap 3.1.1
 - IMPROVED: Local FontAwesome folder included
 - Small bugs corrected


Version 1.3 - 04/01/2014

 - IMPROVED: Sticky Footer added
 - NEW: Blog Timeline page added
 - NEW: Gallery Text Blocks page added
 - NEW: Gallery Bubbles page added
 - NEW: Gallery Item page added
 - NEW: Tags element added
 - UPDATED: Twitter Bootstrap 3.0.3
 - UPDATED: Font Awesome 4.0.3
 - Small bugs corrected

Version 1.2 - 26/11/2013

 - IMPROVED: Profile page redesign
 - NEW: Email and PM contact forms on the Profile page
 - NEW: Avatar upload form on the Profile page
 - NEW: Lost password form on the Sign In page
 - NEW: Profile Edit page added
 - NEW: PM Inbox Page added
 - NEW: PM Dialogs Page added
 - UPDATED: Twitter Bootstrap 3.0.2
 - REMOVED: Panorama showcase removed. Support upon request.

Version 1.1 - 23/11/2013

 - NEW: Panorama showcase added
 - NEW: Scroll to top plugin added