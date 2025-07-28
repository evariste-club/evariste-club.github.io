var ptx_lunr_search_style = "textbook";
var ptx_lunr_docs = [
{
  "id": "prosort",
  "level": "1",
  "url": "prosort.html",
  "type": "Section",
  "number": "1",
  "title": "Prosort Euler",
  "body": " Prosort Euler   An event we're doing with FooBar for ESYA'25     The first exercise   Some introduction     First    Hint      Second          "
},
{
  "id": "subsection-1-1",
  "level": "2",
  "url": "prosort.html#subsection-1-1",
  "type": "Checkpoint",
  "number": "1.1",
  "title": "The first exercise.",
  "body": " The first exercise   Some introduction     First    Hint      Second        "
},
{
  "id": "pwnhub",
  "level": "1",
  "url": "pwnhub.html",
  "type": "Section",
  "number": "2",
  "title": "PWNHUB",
  "body": " PWNHUB  CTF's we started organizing. This website will be updated in due time, but till then, find the old website here .   Ellie  Our very first box! The goal was to familiarize myself and others with the basic infrastructure, ssh 'ing into a box and using simple commands to retrieve a flag.   Let's begin  The most important command you should be aware of is man , it stands for manual page and it opens up the documentation of any command that supports it (which is every single command!). I asked you to ssh into the box, so let's take a quick look at the man page of ssh with     Output: Output of man ssh  Take a look at the highlighted part, I mentioned you should ssh into 192.168.33.113 (which is our host ) as user first_time , so that makes our final command to be     Executing this for the first time, you will get something like this: Host authenticity  You get this because ssh cannot verify if I'm a good guy or not, say yes to that. After that you'll be asked to put in the password GH{}()[] , then you'll be greeted and we'll wait for me to automatically redirect you to a virtual machine I've set up (I don't want you snooping around on my laptop!). You don't have to worry about this step, but just in case you were curious, this is why you will see two IP addresses when you exit.   Now the challenge actually starts  You may notice you are greeted with a very... limiting looking terminal, you get absolutely no information about where you are, who you are and whatever else the terminal you used to get here showed you. This is the classic sh shell that decades old Unix shipped with, you might wish to try out the B ourne A gain SH ell (let's see if you can find the command to do so).  Take a look now at the commands I've mentioned you might need, take a look at the man pages of them, try out running the command with --help or -h for some shorter info. Fun fact, you can type man man to see what the man command does!  That's it for this one, I'll keep adding stuff here till you finally get to the flag. (1256, 3 Apr)    Walkthrough  I mentioned the flag is in the least updated directory, let's take a look at the manual page of ls with man ls . Output: Out of man ls  Take a look at the -a and -c flags, that's what we need. We can also use the -l flag, that'll help us too.  Output ls -alc  You'll see my terminal probably looks better than yours, that's because I'm using bash which provided a bunch of helpful features. But mainly, look at the output (ignore the .ssh , .bashrc , .hushlogin , . , and .. ). The .orisit directory is what we need. Let us now change into that directory with cd . The command to do so is     Now we have a bunch of files, the flag is in the human readable file, taking a look at the man page of file , we see it tells us exactly what we need.   man file   Now you could go ahead and run file for every single file, but a better way is to use the glob, * , which encompasses everything all at once. But running file * would give you a ton of errors, that's because some files start with a hyphen ( - ) and most linux utilities think that means a different switch should follow, take a look at the ls command we ran, we turned on switches a , l and c . We fix this issue by prepending the glob with .\/ , this expands to     and not something like     Take a look at the following screenshot   main   You'll see the command I ran is significantly more complicated, I want you try and see what grep does (take a look at the manual!) and what the pipe operator ( | ) does. Play around with what happens when you don't do this.  Take a look at the arguments I gave to file . All hidden files or directories in Linux are denoted by a . at the start of their name, so if we wish to include them, we must use .* to capture them.  All human readable files are ASCII, that's why I filtered them down so. Now, finally, our flag is in the file which starts with - . The only such file is - orisit17 .  To read the contents, we use the cat command (or anything else like more or less ).   (you'll see I used a \\ to escape the space in the name, you could either use quotes to enclose the name)    flag   We now have the flag. (1321, April 4)    Other methods     cat -- - orisit17 also works, the -- part tells Unix that it shall no longer interpret anything as switches after this. ( Priyanshu Kumar )    find \/* -name -* 2>\/dev\/null finds every file starting with a hyphen from the root ( \/ ) of the filesystem, and errors are redirected to nothingness ( \/dev\/null is always nothing, 2> redirects stderr  (the errors) to \/dev\/null instead of the terminal, with is \/dev\/stdout ). Play around with this, it's interesting. (adding -type f would've made it search only files.) ( Arpit Rajput )    grep -r flag ~ 2> \/dev\/null is another interesting one, -r , or --recursive searches for the string you provided in each file starting from whatever you mentioned, here, ~ , which expands to \/home\/first_time , your home. This works because the file actually has the word flag in it, so, be careful. (adding the -i flag would've made it a little more foolproof.) ( Mohd Irfan Raza )         Benjamin  The second one!       Let's start  I said you'll have to scan for a server named desmond on a network with the same subnet mask, that was 255.255.255.0 , which could be abbreviated as \/24 , take a look at the following table  For a complete list, take a look here . NetworkChuck has a good video explaining what this means.  Let's first take a look at the IP address of the server we're currently in by running     This will give us an IP, that, along with our subnet mask knowledge tells us that desmond must have an IP whose first three quartets are the same (that's what 255 denotes), while the last one can be anything (that's what 0 signifies).  We now wish to find desmond 's IP address, we can run that by running a no-ports scan via nmap .  Output of man nmap : man nmap  Let's see if you figure out what the command should be now (you could either try the glob character * , or use \/24 with the IP).  When you find it, run nmap with only it's IP and find the services running on there.   Everything is misconfigured.    Another one   another one   When you're knee deep, you'll be asked for something related to FRACTRAN , we held an event regarding this a while back, and I released a write-up. We always send everything on telegram, or on mail.    Walkthrough  If you read the hints for Ellie, I mentioned that you're actually ssh ing into my personal laptop, after which you re automatically redirected to a virtual machine. Hence the IP you put in may not be the IP of the machine you land it, to get the correct IP, we run     Output: first  Nice! So our IP is 192.168.124.168 . We know want to discover another host living on the same network and the same subnet mask, that is 255.255.255.0 , this means that the first three quartets must be the same, so our IP for desmond must look like 192.168.124.* . We'll use nmap for this task, specifically the no-ports option as that'll speed things up.     Output: Second Note that I used the sP , and not sn , like I previously mentioned (look at the documentation!).  An alternate command that also works is     (take a look at the table above, this method is preferred)  We have now found desmond at 192.168.124.247 , let's run nmap again, but this time searching for ports. We'll do      third   We find an ftp server, which stands for the file transfer protocol. Fascinating, let's see if we can access it.      fourth   I put my login credentials, we got nowhere. Let's take a look at the man page.   fifth   What's this? Let's try it     sixth We're in!  Let's now explore, typing ls , we see a flag and hint file. Take a look at what you get when you type help in the terminal, which command could you use to view this file?  You might try get but that'll give you permission errors. Let's try less   seventh   Ope! Not that easy! Let's exit this, and try again with nmap .   eigth      -p- tells nmap to scan every port.   ninth   Whoa, there's a lot more stuff going on here!  Let's use a few powerful features nmap provides to dig deeper. This time I'll limit the ports to only the ones shown by including -p696,3002,6379 (we're done with the ftp service).  One more look at the man page: tenth  Let's run      ele   Fascinating, what's netcat ? If we take a look at the commands I said you might need, theres something called nc , let's take a look   twe   This looks promising! Let's run     as that's the service that told us about nc .   fourt   Fair enough, not much information, let's try it on port 3002.   fift   We found something! No idea about the PIN though, but there's another service called redis going on. Let's try typing redis in our terminal. That didn't get us anything, let's search for redis on the web.   sixt   Found this on their GitHub repository, let's run redis-cli . We get something, let's take a look at the help section.  (as a side note, running apropos redis would have also revealed what we needed, apropos is the search utility in linux, take a look at the man page!)   seven   Ok, so now let's run     We get... Something. This time, the man page isn't helpful. But, take a look at the help out above, we see something like AUTH username pass , let's run that. If I put in star1 I get an error. Remember, I said everything is misconfigured. Let's try some common passwords, like     admin    administrator    root    anon    anonymous     Trying and checking, we'll see that auth root gets us in and we get an OK message.  If you took a look at HTB, we're doing the same thing as one of their boxes, go check them out!  We now note that redis is a key-value NoSQL database, so there must be keys I could find. If I type keys in the terminal, I am hinted at providing a pattern , lets run keys * to find everything. We can now get the value associated to the specific key , the min and max look interesting, so let's get them.   eig   Huh, if we get the what key aswell, we see the PIN is constrained, and we just found the min and max of... something, our PIN probably lies between these!  Let's find the min first, creating a simple python script, something like the following   nine   And then summing them up, we find that the minimum is 17710 .  The maximum is an interesting one, our keyword is FRACTRAN, and we did an event for this, for which I released a writeup, let's search for it.  twne (on gmail)  wef (on telegram)  Nice, let's open up this PDF  fesrd A compiler, that's what we need! Let's download and run this (take a look at the code if you like).  eegr Running -h . We need PRIMEGAME, let's run it with -p !  This is what we get: alt text  Hence we get a maximum value of 19268 .  We're almost done, I swear!  Last time referencing the hints for Ellie, I used the pipe operator | , say we run A | B , it takes the (standard) output of A and gives it to B as the standard input, effectively meaning that you don't have to manually give it to B .  Back to port 3002, we need to manually give it a PIN, but we can use the echo command to automate it, take a look:   efegr   Now all we need is a simple for loop going from the min to the max, and we echo that variable, and see if we get something. Take a look at this bash cheat sheet  alt text (found at this link )  Let's do it!   alt text   And now we're spamming desmond and getting a ton of output, for the tiniest instant you'll see a longer output, press Control-C to stop and scroll up, you'll find   the flag   There are, of course, better ways to do it, for example, consider   s   In text:     (which is slightly different than the one I actually ran)  This straight away gives us the PIN, but there's a lot going on here. Let's break it down.  alt text This might help.     grep returns an exit code of 0 (or success) when it's able to find something matching the search criteria.    It returns something non-zero when it can't,    The variable ? , accessed via $? stores the exit code of the last run command.    Redirecting the output (with the > redirect) to \/dev\/null , which is a file that has nothing, a black hole, if you will. We do this so we don't see the output of the command we're running - we're only interested in the exit code.    -eq is the equality operator (for numbers).     I guess that's explanation enough, if you still need help with something, please send me a mail, and I'll update this file.  We're done! We're done! This was a lot, took me an hour to make this walkthrough! Hope you had fun playing.    A few points     If you don't like this inline stuff, you could've gone into the \/tmp directory and wrote the script, with vi there.    If you followed the exact same steps above (or in the ballpark), but didn't get the flag, it's very likely someone else was also on the machine running nmap , which, unfortunately, breaks the script accepting the PIN, and it takes me (another script) about 40 cycles to bring it back up, so if that's you, please send me a mail.        "
},
{
  "id": "sec-walkthrough-ellie-21",
  "level": "2",
  "url": "pwnhub.html#sec-walkthrough-ellie-21",
  "type": "Paragraph (with a defined term)",
  "number": "",
  "title": "",
  "body": "We now have the flag. "
},
{
  "id": "the-meme",
  "level": "2",
  "url": "pwnhub.html#the-meme",
  "type": "Figure",
  "number": "2.1",
  "title": "",
  "body": "   "
},
{
  "id": "ch-let-s-start-11",
  "level": "2",
  "url": "pwnhub.html#ch-let-s-start-11",
  "type": "Paragraph (with a defined term)",
  "number": "",
  "title": "",
  "body": "Everything is misconfigured. "
},
{
  "id": "sec-walkthrough-benjamin-60",
  "level": "2",
  "url": "pwnhub.html#sec-walkthrough-benjamin-60",
  "type": "Paragraph (with a defined term)",
  "number": "",
  "title": "",
  "body": "17710 "
},
{
  "id": "sec-walkthrough-benjamin-68",
  "level": "2",
  "url": "pwnhub.html#sec-walkthrough-benjamin-68",
  "type": "Paragraph (with a defined term)",
  "number": "",
  "title": "",
  "body": "19268 "
},
{
  "id": "blogfiles",
  "level": "1",
  "url": "blogfiles.html",
  "type": "Section",
  "number": "3",
  "title": "Blog Files",
  "body": " Blog Files   A sort of blog I'm hoping to maintain (based on the input of one of our team member, 8 or so months ago).   "
}
]

var ptx_lunr_idx = lunr(function () {
  this.ref('id')
  this.field('title')
  this.field('body')
  this.metadataWhitelist = ['position']

  ptx_lunr_docs.forEach(function (doc) {
    this.add(doc)
  }, this)
})
