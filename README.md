# Traceroute application

Application works like `traceroute` util in Linux, macOS or `tracert` in Windows.

## Usage 
Application works on socket cause of it you should run it using `sudo`
```shell
sudo python3 traceroute.py
```
or
```shell
sudo python traceroute.py
```

## Examples
```shell
user traceroute % sudo python traceroute.py
Enter the address to traceroute: ya.ru
traceroute to ya.ru (87.250.250.242) using port 33512
1   192.168.0.1     (dlinkrouter.dlink)
2   10.8.124.1      (10.8.124.1)
3   5.19.0.178      (5x19x0x178.static-business.spb.ertelecom.ru)
4   188.234.140.226 (188-234-140-226.ertelecom.ru)
5   188.234.140.227 (188-234-140-227.ertelecom.ru)
6   *
    *
    *
7   *
    *
    *
8   87.250.250.242  (ya.ru)
```

```shell
user traceroute % sudo python3 traceroute.py
Enter the address to traceroute: google.com
traceroute to google.com (108.177.14.139) using port 33513
1   192.168.0.1     (dlinkrouter.dlink)
2   10.8.124.1      (10.8.124.1)
3   5.19.0.178      (5x19x0x178.static-business.spb.ertelecom.ru)
4   188.234.131.158 (net131.234.188-158.ertelecom.ru)
5   188.234.131.159 (net131.234.188-159.ertelecom.ru)
6   *
    *
    *
7   74.125.244.129  (74.125.244.129)
8   74.125.244.180  (74.125.244.180)
9   142.251.51.187  (142.251.51.187)
10  216.239.56.101  (216.239.56.101)
11  142.250.56.217  (142.250.56.217)
12  *
    *
    *
13  *
    *
    *
14  *
    *
    *
15  *
    *
    *
16  *
    *
    *
17  *
    *
    *
18  *
    *
    *
19  *
    *
    *
20  108.177.14.139  (lt-in-f139.1e100.net)
```