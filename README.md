# VideoServiceResearch

This repository holds files that conduct experiments on video providers.

---

### Chrome startup options used:

1. --remote-debugging-port=9222 (**required**)
2. --media-cache-size=4096 (optional but effective, size in *bytes*)
3. --disable-gpu-program-cache (opitonal)

---

### File and directory format:

1. line feed: use **\n** instead of **\r\n**

---

### Video websites:

1. YouTube
2. Vimeo
3. Netflix
4. Hulu

---

### Measurement

1. **CDNs** used on video webpages
2. **DNS results** for CDN domains
3. **ping delays** or **RTT** to these domains
4. **trace route** to these domains (**TODO**)
5. **locations** of these domains
6. capture video palying procedure ?
7. find hints from **other network requests / responses** ?

---

### TODO:

1. find a solution to crawl 500+ (or even 1000+) video pages with limited network consumption. If achieved, crawl only once a week. *Done!*

	1.1  First solution might be to optimize **find_cdns_yt.js** and utilize certain Chrome options. This is achieved by adjusting code structure, see **find_cdns_youtube_v2.js**.

	1.2 Second solution is using **Wireshark** to record network information while using chromedriver to navigate into URLs. Although it local traffic is encrypted in HTTPS, reversel DNS might solve this problem. Once an IP's relative domain name matches certain pattern, it's what we are looking for. **TODO**

	1.3 Third solution: measure different part of URLs each day, finish all of them in 1 week? As 1.1 has successfully solved runnability and traffic problem, this solution is dismissed.
	
---

### Clarification:

Purpose of this work is utilizing (**finding** and **using**) better CDN servers when browsing certain video websites from the perspective of a client. 

Fistly, it's necessary to characterize video websites. Questions to be answered include: what kind of domain strategy (**single domain** or **random prefix domains**) that a video website uses; does the video website take location into consideration; how many and how often would **bad** CDNs be recommended? 

Secondly, with different answers to these questions, different optimizaiton strategies are considered. If a video website uses single domain strategy, it suffices to modify local DNS cache so that DNS resolution of this domain directs the client to machines (labeled by IP address) that have better **performance**. Problems to be solved for this case: where to find better CDN servers, how often would bad CDN servers be recommended, and how to decide if a server performs good. One solution to find better CDN servers, according to **CoNEXT Drongo** paper, is utilizing DNS client subnet option to disguise the client as all the hops along the route from the client to the CDN server, and select from all the DNS recommendations of these hops. Also in this paper, ping delay is the metric used to characterize CDN performance.

If a video website uses random prefix domain strategy, we need first find out as many random domains used by this website as possible, so that we can characterize this website more precisely. Then we need to find out how often and how many **bad** CDN servers would be used: if both results are innegligible, then it's meaningful to avoid being recommended with these bad CDN servers. However, this requries massive measurements on the video website.

According to multiple literatures, works that conduct research on YouTube CDNs capture traffic data from ISPs, however it's not possible for me to acquire such data. From the perspective of a client and a researcher, I can only acquire data using **multiple virtual machines** located in different locations, and through massive measurement on as **many webpages** as possible to characteristics of certain video providers. 