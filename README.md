# P3_CV

The input file should be named BBB.mp4 <br />
Run tasks.py to execute the exercises. <br />

## Task 1
* RESIZE THE VIDEO TO MULTIPLE RESOLUTIONS
* TRANSCODE THE VIDEO TO MULTIPLE BITRATES
* CREATE HLS PLAYLIST (m3u8)
* CREATE AN HLS MASTER PLAYLIST (m3u8)

## Task 2
* FRAGMENT MP4 FILE
* ENCRYPT AND DASH FRAGMENTED FILE (MARLIN DRM)

## Task 3
* CREATE THE LIVE STREAM
* YOU CAN WATCH THE LIVE STREAM BY TYPING 'ffplay udp://127.0.0.1:23000' IN A TERMINAL

## Task 4
Open the Task4 folder. The screenshots shows the information of the streaming provided by the developer tools.
In the Screenshot_mpd.png image you can see on the left side the .mpd files and on the right side the information of the selected file. <br />
This is DASH streaming because we can relate .mpd to MPEG-DASH and .m3u8 to HLS streaming. We can also see the general information and the response and request headers.
In the Screenshot_browser.png image we can see more request headers information such as the browser or the OS.
