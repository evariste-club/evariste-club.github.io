# Let's start

I said you'll have to scan for a server named `desmond` on a network with the same subnet mask, that was `255.255.255.0`, which could be abbreviated as `/24`, take a look at the following table

| Network Bits | Subnet Mask | Number of hosts |
| --- | --- | --- |
| /24 | 255.225.225.0 | 254 |
| /23 | 255.255.254.0 | 510 |
| /16 | 255.255.0.0 | 65534 |
| /8 | 255.0.0.0 | 16777214 |

For a complete list, take a look [here](https://www.cloudaccess.net/cloud-control-panel-ccp/157-dns-management/322-subnet-masks-reference-table.html).
[NetworkChuck](https://youtube.com/@networkchuck?si=w-Nr39dWBydAlSCi) has a good video explaining what this means.

Let's first take a look at the IP address of the server we're currently in by running

```sh
ip a
```

This will give us an IP, that, along with our subnet mask knowledge tells us that `desmond` must have an IP whose first three *quartets* are the same (that's what 255 denotes), while the last one can be anything (that's what 0 signifies).

We now wish to find `desmond`'s IP address, we can run that by running a *no-ports* scan via `nmap`.

Output of `man nmap`:
![man nmap](image.png)

Let's see if you figure out what the command should be now (you could either try the glob character `*`, or use `/24` with the IP).

When you find it, run `nmap` with only it's IP and find the services running on there.

**Everything is misconfigured.**
