# Benjamin

You should `ssh` into `192.168.33.113` as `star1` with password `star1`. (It doesn't matter which network you're connected to. If you are outside campus, use the VPN. For a guide to using `ssh`, check out the [hints](../hints_for_ellie.html) I wrote for Ellie.)

This time, the flag is not in the machine you'll land in! You're gonna have to search for a server named `desmond`, and the flag is on one of the services running on `desmond`.

In pointers:

- Search for a server named `desmond` on the same subnet mask (that is `255.255.255.0`).
- Find all the services running on `desmond`, the flag shall be revealed when you enter te correct pin (*you will not find it though*).
- Search online! That'll be your best friend. Take a look at [Hack The Box](https://app.hackthebox.com/starting-point), most of the stuff has just been adapted from there.

As always, hints and a walkthrough will be uploaded and updated here. The challenge will end in a week, around the 22nd of April.

A non-exhaustive list of commands you might need: `ls`, `cd`, `du`, `grep`, `find`, `nmap`, `nc`, `man`, `help`, `<command> --help`.

When you've found the flag, please mail it to us at [evariste@sc.iitd.ac.in](mailto:evariste@sc.iiitd.ac.in).

If you've found this one interesting, and would like to explore further, I recommend checking out [Hack The Box](https://app.hackthebox.com/starting-point).
