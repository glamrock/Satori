##Satori

###Distributed, tamper-resistant circumvention tools

An unfiltered internet is critical to free speech and self-determination -- the most precious of liberties. Free flow of ideas is particularly crucial in areas with intense internet filtering, as these are the areas pushing oppressive policies onto their people.

What Satori does is provide access to verifiable bundles of privacy-enhancing software to those who need it most.

**Note:** I need people who use a language other than English to help test.

###Features
* language detection to offer the right download
* distributed downloads, with options on Github, Amazon, and the Chrome Web Store itself
* SHA256sum checker to help verify software integrity

###Danger! High Voltage!!
This software is currently ***alpha***.

###Code notes
* Distributing a hash for the outer container when using Chrome as backbone is tricky, as the outer container can vary slightly. The inner TBB will always have the same checksum, however. (Thanks DCF for testing with this).

###Licenses
**Note: All of the software distributed can be used for free, and are open-source.**

Satori uses Artistic License 2.0, a [supervillain-friendly](http://i.imgur.com/1xV099o.jpg) license.

* [Google Closure](https://code.google.com/p/closure-library/) (compiled.js) licensed under Apache 2.0.
* [GPG4Win](https://gpg4win.org) is provided under [GNU Public License](http://gpg4win.org/license.html). 
* [Tor](https://torproject.org) Browser Bundle [has several licenses](https://gitweb.torproject.org/builders/tor-browser-bundle.git/tree/HEAD:/Bundle-Data/Docs/Licenses). 
* [TorBirdy](https://addons.mozilla.org/en-us/thunderbird/addon/torbirdy/) is released under the BSD license.
* [Enigmail]()


###Thanks

**People**<br>
Many thanks to all of the people who gave feedback, particularly David Fifield, who found several annoying issues with an early version. (And who has seriously *legit* musical taste).

Katie Krauss offered great advice early on, and recommended a feature to alert users that their selection was downloading.

And as always, thanks to those who *must* remain anonymous, for taking the time to test against filters and give usability feedback. :love_letter:

Also thanks to Redacted, for answering my question about SHA256sum checking at LibrePlanet. Truly, your help has been redacted redacted.  Redacted!

**Music**
* *Black Marble* "A Different Arrangement"
* *She Wants Revenge* discography
* *Lincoln County Historical Society* "Die Bastards"
* *St. Vincent* "Actors" & "St. Vincent"
* *Thomas Azier* "Hylas 002" & "Verwandlung" EPs
* *Au Revoir Simone* "Still Night, Still Light"

**Credits**
Polygon script by <a href="http://codepen.io/Wryte/details/qKgGd" target="_blank">Wryte</a>, used with <a href="https://twitter.com/Craigstra/status/448976757836619776"> permission</a>.

As mentioned above, Satori uses [Google's Closure API](http://docs.closure-library.googlecode.com/git/namespace_goog_crypt.html) to generate sha256 checksums for software.

###[Contact](https://github.com/glamrock/contact)
griffin [@](at) cryptolab.net
