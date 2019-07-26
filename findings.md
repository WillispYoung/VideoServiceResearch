# Findings in Measurement on Video Providers

## YouTube

1. Page Loading Process

Take URL "https://www.youtube.com/watch?v=z0grXGgO9DY" as example:

    1.1 GET https://www.youtube.com/watch?v=z0grXGgO9DY
    1.2 GET https://i.ytimg.com/generate_204 (triggered by fetch event of <link> element; this domain seems important)
    1.3 GET https://r5---sn-i3b7knld.googlevideo.com/generate_204 (this domain is the CDN server used most of the time, might be inferred based on the result of 1.2)
    1.4 GET https://r5---sn-i3b7knld.googlevideo.com/generate_204?conn2 (unknown)
    1.5 fetch several JS, CSS, font and other resource files (with base.js the most important)
    1.6 send multiple state data to YouTube server
    1.7 GET https://r6---sn-i3b7kn7z.googlevideo.com/videoplayback?*** (called by base.js; get blocked video file from CDN servers; this domain sometimes changes as playing procedure prolongs, possibly due to load balancing)