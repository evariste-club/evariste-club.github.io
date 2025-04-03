# Let's begin

The most important command you should be aware of is `man`, it stands for manual page and it opens up the documentation of any command that supports it (which is every single command!). I asked you to `ssh` into the box, so let's take a quick look at the `man page` of `ssh` with

```sh
man ssh
```

Output:
![Output of man ssh](image.png)

Take a look at the highlighted part, I mentioned you should `ssh` into `192.168.33.113` (which is our *host*) as user `first_time`, so that makes our final command to be

```sh
ssh first_time@192.168.33.113
```

Executing this for the first time, you will get something like this:
![Host authenticity](image-1.png)

You get this because `ssh` cannot verify if I'm a good guy or not, say *yes* to that. After that you'll be asked to put in the password `GH{}()[]`, then you'll be greeted and we'll wait for me to automatically redirect you to a virtual machine I've set up (I don't want you snooping around on my laptop!). You don't have to worry about this step, but just in case you were curious, this is why you will see two IP addresses when you exit.

## Now the challenge actually starts

You may notice you are greeted with a very... limiting looking terminal, you get absolutely no information about where you are, who you are and whatever else the terminal you used to get here showed you. This is classic `sh` shell that decades old Unix shipped with, you might wish to try out the *B*ourne *A*gain *SH*ell (let's see if you can find the command to do so).

Take a look now at the commands I've mentioned you might need, take a look at the `man` pages of them, try out running the command with `--help` or `-h` for some shorter info. Fun fact, you can type `man man` to see what the `man` command does!

That's it for this one, I'll keep adding stuff here till you finally get to the flag. (1256, 3 Apr)
