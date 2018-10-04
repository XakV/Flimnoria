This plugin is to interface with the Fedora Accounts System.

TO INSTALL:
1) Move the plugin to a directory where Supybot can access it.
   - ZV - make sure you auth as bot owner in a priv msg
2) @load Fedora
   - ZV - This now seems to coincide with the name of the plugin directory
   - ZV - Name of plugin is probably set in package, but I haven't gotten there yet
3) If you are not using the main FAS, run
     @config plugins.fedora.fas.url [rooturl]
   - ZV - here I've used our staging instance
   - ZV - note I've also limited the user download to FAS names starting with Q
4) In a PRIVMSG (/msg) to your bot, say
     config plugins.fedora.fas.username [username]
     config plugins.fedora.fas.password [password]
   (This information can only be accessed by bot owners.)
   - ZV - I beleive this takes the name of the plugin directory
5) @reload Fedora (or supybot-fedora, again, name of directory)

