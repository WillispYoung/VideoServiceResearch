# Findings in Measurement on Video Providers

## YouTube

### 1. Page Loading Process

Take URL "https://www.youtube.com/watch?v=z0grXGgO9DY" as example:

* GET https://www.youtube.com/watch?v=z0grXGgO9DY(the response contains CDN server's domain that is used by this page for the most of time)
* GET https://i.ytimg.com/generate_204 (triggered by fetch event of <link> element; this domain seems important as YouTube image)
* GET https://r5---sn-i3b7knld.googlevideo.com/generate_204 (this domain is the CDN server used most of the time, might be inferred based on the result of 1.2)
* GET https://r5---sn-i3b7knld.googlevideo.com/generate_204?conn2 (unknown)
* fetch several JS, CSS, font and other resource files (with base.js the most important)
* send multiple state data to YouTube server
* GET https://r6---sn-i3b7kn7z.googlevideo.com/videoplayback?*** (called by base.js; fetch video block file from CDN servers; this domain sometimes changes as playing procedure prolongs, possibly due to load balancing)

As the response to the 2nd request contains CDN server's domain, this hints another solution to capture more CDN domains with much less traffic consumed.

### 2. Preload

There are 2 `<link rel="preload" href="*" as="fetch">` elements in the response to the 1st request (`GET https://www.youtube.com/watch?v=z0grXGgO9DY`.) As these `<link>`s are directed to the CDN server that video block files are fetched from, it's presumably that `<link>`s with **preload** attribute could sharply accelerate video loading process. 

This conforms with the behavior of YouTube browsing. Yet is this the reason that YouTube video is loaded way faster than other elements (such as sidebar recommendations and footbar user comments) ?

### 3. Multicasting

Multicasting allows the server only accesses resource files once, but delivers the same block of files to multiple clients via multicasting channels. For video services, as video caching is required, block of video files that represent the same period of videos can be distributed to users that are not watching this period. Dispite the on-demand characteristic of video serviecs, resource caching fills the gap between current time point and distributed video block. 

### 4. CDN Characteristics

* **DNS stability**: run `python analyze.py -diff {location} {website}`. Highly stable, IP address for a domain will not change.

* **Frequency stability**: run `python analyze.py -freq {location} {website}`. Varies sharply in Hong Kong, mildly in Singapore and Silicon Valley.

* **Delay stability**: run `python analyze.py -delay {location} {website}`. Relatively stable.

* **Quality proportion**: run `python analyze.py -quality {location} {website}`. Results:

    Domain proportion: bad CDNs among all CDNs while getting all URLs

    Frequency proportion: frequency of bad CDNs among frequency of all CDNs while getting all URLs

    Location | Domain Proportion| Frequency Proportion
    ---|---|---
    Hong Kong | 0.76 ~ 0.78 | 0.17 
    Singapore | 0.79 ~ 0.82 | 0.10 ~ 0.14
    Silicon   | 0.32 | 0.04

* Are poorly-performing CDNs clustered in certain subnets?

    No, a subnet contains both well-performing and poorly-performing CDNs. Run `python analyze.py -subnet {location} {website}`.

    Location | Date | Subnets
    ---|---|---
    Silicon Valley | 19-8-1 | 172.217, 173.194, 209.85, 74.125,
    - | 19-8-2 | 172.217, 173.194, 209.85, 74.125,
    - | 19-8-3 | 173.194, 74.125,
    - | 19-8-5 | 172.217, 173.194, 209.85, 74.125,
    Hong Kong | 19-7-30 | 173.194, 172.217, 209.85, 74.125,
    - | 19-7-31 | 173.194, 172.217, 209.85, 74.125,
    - | 19-8-1 | 173.194, 172.217, 74.125, 209.85,
    - | 19-8-2 | 173.194, 172.217, 74.125, 209.85,
    Singapore | 19-7-31 | 172.217, 173.194, 209.85, 74.125,
    - | 19-8-1 | 172.217, 173.194, 209.85, 74.125,
    - | 19-8-2 | 172.217, 173.194, 209.85, 74.125,
    - | 19-8-3 | 172.217, 173.194, 209.85, 74.125,

    inetnum: 
    
        69.194.128.0 - 76.255.255.255
        209.43.0.0 - 209.162.127.255
        173.0.0.0 - 173.212.191.255
        172.103.96.0 - 172.240.255.255


* Does YouTube assign CDNs really considering geolocation?

    Actually **NO**. From the perspective of subnet, subnets of CDNs used in different geolocations are exactly identical; with regard to CDN intersection (see table below), run `python analyze.py -geo {website}`, the result also proves NO.

    Location | Intersection Size
    ---|---
    Hongkong (2585) - Singapore (2905) | 2204
    Hongkong (2585) - Silicon (1914) | 1911
    Singapore (2905) - Silicon (1914) | 1631

* Is assigned CDN related to page URL?

    Hard to tell, yet seemingly not. Another finding: poorly-performing CDN is always accompanied with a better CDN, as in the case when mulitple (always 2) CDNs are contained in the response to the 1st request. I suppose this is a remedy solution to avoid over-using poorly-performing CDN. 

    We may need to know the proportion of traffic volume directed to poorly-performing CDNs.

### 5. Optimization

Given the fact that frequency of poorly-performing CDNs doesn't exceed $0.17$, by simple calculation, $0.17^3 = 0.004913$, which ensures that within 3 times page refreshing, the possibility for at least 1 well-performing CDN being used is more than 99%.

Although afore-mentioned hypothesis may not be valid enough, other problems occur: how to evaluate if a video is well-served, and what is the difference of effect between well- and poorly-performing CDNs? And as poorly-performing CDN is always accompanied with well-performing CDN, would the former even affect video quality?

### 6. TODO

Replay the case when poorly-performing CDN is used. It's required that network information can be accessed in real time. Probable solutions are:

1. Use `Logging` functionality in Selenium to access _console_ and _network_ information recorded in Chrome. Requires knowledge on the log files.

2. Utilize transparent proxy to access network information directly. However, because of the existence of GFW, 2 proxies, or a self-developed proxy is needed to access network information. 

3. According to data/*/youtube/freq.txt, which shows the frequency of suggested CDNs for a web browserinig, wihtin 10 pages, the case of double-CDNs appears. Try **manual testing**.

---

#### Result of Manual Testing:

Of the 12 pages I've tested, the double-CDN case never happened, and the video playback flows are processed properly even video quality is very high (720p 60). 

---

Another direction I think is: implement the hypothesized solution to show the possibility of such solution.

Yet another one: use `tcpdump` to get more network information (RTT, ECN, loss rate, bandwidth capacity).

Inband Network Telemetry: capture network information on the switches (and accessible for end-users).

### 7. Video Transmission Format

As many video providers now use **.ts** (Transport Stream) format to stream video files, such streaming task is conducted in JavaScript. By setting certain **EventListener**s, JavaScript codes are able to cache a video block within specified byte range, as long as the server supports such functionality. 

See https://developers.google.com/web/fundamentals/media/fast-playback-with-video-preload.

### 8. Google's CDN

> 1st Party: 

R. Krishnan, H. V. Madhyastha, S. Srinivasan, S. Jain, A. Krishnamurthy, T. Anderson, and J. Gao, **“Moving Beyond End-to-End Path Information to Optimize CDN Performance,”** in IMC, 2009.

Y. Zhu, B. Helsley, J. Rexford, A. Siganporia, and S. Srinivasan, **“LatLong: Diagnosing wide-area latency changes for CDNs,”** in Transactions on Network and Service Management, 2012.

T. Flach, N. Dukkipati, A. Terzis, B. Raghavan, N. Cardwell, Y. Cheng, A. Jain, S. Hao, E. Katz-Bassett, and R. Govindan, **“Reducing Web Latency: The Virtue of Gentle Aggression,”**  SIGCOMM, vol. 43, no. 4, pp. 159–170, 2013.

> 3rd Party:

Google Cloud CDN. https://cloud.google.com/cdn/.

> Load balancing: 

Google Cloud Load Balancer. https://cloud.google.com/load-balancing/
