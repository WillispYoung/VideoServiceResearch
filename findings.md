# Findings in Measurement on Video Providers

## YouTube

1. Page Loading Process

Take URL "https://www.youtube.com/watch?v=z0grXGgO9DY" as example:

* GET https://www.youtube.com/watch?v=z0grXGgO9DY (the response contains CDN server's domain that is used by this page for the most of time)
* GET https://i.ytimg.com/generate_204 (triggered by fetch event of <link> element; this domain seems important as YouTube image)
* GET https://r5---sn-i3b7knld.googlevideo.com/generate_204 (this domain is the CDN server used most of the time, might be inferred based on the result of 1.2)
* GET https://r5---sn-i3b7knld.googlevideo.com/generate_204?conn2 (unknown)
* fetch several JS, CSS, font and other resource files (with base.js the most important)
* send multiple state data to YouTube server
* GET https://r6---sn-i3b7kn7z.googlevideo.com/videoplayback?*** (called by base.js; fetch video block file from CDN servers; this domain sometimes changes as playing procedure prolongs, possibly due to load balancing)

As response to the 2st request contains CDN server's domain, this hints another solution to capture more CDN domains with much less traffic consumed.

2. Preload

There are 2 `<link rel="preload" href="*" as="fetch">` elements in the response to the 1st request (`GET https://www.youtube.com/watch?v=z0grXGgO9DY`.) As these `<link>`s are directed to the CDN server that video block files are fetched from, it's presumably that `<link>`s with **preload** attribute could sharply accelerate video loading process. 

This conforms with the behavior of YouTube browsing. Yet is this the reason that YouTube video is loaded way faster than other elements (such as sidebar recommendations and footbar user comments) ?

3. Multicasting

Multicasting allows the server only accesses resource files once, but delivers the same block of files to multiple clients via multicasting channels. For video services, as video caching is required, block of video files that represent the same period of videos can be distributed to users that are not watching this period. Dispite the on-demand characteristic of video serviecs, resource caching fills the gap between current time point and distributed video block. 