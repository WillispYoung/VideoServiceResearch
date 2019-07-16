# VideoServiceResearch
This repository holds files that conduct experiments on video providers.

---

Chrome startup options used:

1. --remote-debugging-port=9222 (**required**)
2. --media-cache-size=4096 (optional but effective, size in *bytes*)
3. --disable-gpu-program-cache (opitonal)

---

File and directory format:

1. directory structure: location/date/website/{cdns, ips, delays, location}.txt
2. line feed: use **\n** instead of **\r\n**

---

Video websites:

1. YouTube
2. Vimeo
3. Netflix
4. Hulu

---

TODO:

1. find a solution to crawl 500+ (or even 1000+) video pages with limited network consumption. If achieved, crawl only once a week.

---

Clarification:

Purpose of this work is utilizing (**finding** and **using**) better CDN servers when browsing certain video websites from the perspective of a client. 

Fistly, it's necessary to characterize video websites. Questions to be answered include: what kind of domain strategy (<u>single domain</u> or <u>random prefix domains</u>) that a video website uses; does the video website take location into consideration; how many and how often would _bad_ CDNs be recommended? 

Secondly, with different answers to these questions, different optimizaiton strategies are considered. If a video website uses single domain strategy, 


 The first step is finding better CDN servers to be used, which is achieved by massive measurement; the second step is using these better CDN servers as a client. However, the pre-requisites of usability and effectiveness of such strategy is that *bad* CDN servers are recommended