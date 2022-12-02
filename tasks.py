import os
def HLS():

    # RESIZE THE VIDEO TO MULTIPLE RESOLUTIONS
    # TRANSCODE THE VIDEO TO MULTIPLE BITRATES
    #CREATING HLS PLAYLIST (m3u8)
    #CREATE AN HLS MASTER PLAYLIST (m3u8)

    c = 'ffmpeg -i BBB.mp4 \
        -filter_complex \
        "[0:v]split=3[v1][v2][v3]; \
        [v1]copy[v1out]; [v2]scale=w=1280:h=720[v2out]; [v3]scale=w=640:h=360[v3out]" \
        -map [v1out] -c:v:0 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:0 5M -maxrate:v:0 5M -minrate:v:0 5M -bufsize:v:0 10M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
        -map [v2out] -c:v:1 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:1 3M -maxrate:v:1 3M -minrate:v:1 3M -bufsize:v:1 3M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
        -map [v3out] -c:v:2 libx264 -x264-params "nal-hrd=cbr:force-cfr=1" -b:v:2 1M -maxrate:v:2 1M -minrate:v:2 1M -bufsize:v:2 1M -preset slow -g 48 -sc_threshold 0 -keyint_min 48 \
        -map a:0 -c:a:0 aac -b:a:0 96k -ac 2 \
        -map a:0 -c:a:1 aac -b:a:1 96k -ac 2 \
        -map a:0 -c:a:2 aac -b:a:2 48k -ac 2 \
        -f hls \
        -hls_time 2 \
        -hls_playlist_type vod \
        -hls_flags independent_segments \
        -hls_segment_type mpegts \
        -hls_segment_filename stream_%v/data%02d.ts \
        -master_pl_name master.m3u8 \
        -var_stream_map "v:0,a:0 v:1,a:1 v:2,a:2" stream_%v.m3u8'
    os.system(c)

def MPD():
    os.environ['PATH'] += ':/home/roger/Bento4/cmakebuild' #add path to Bento4 tools

    #FRAGMENT MP4 FILE
    c1 = 'mp4fragment BBB.mp4 BBB-fragmented.mp4'

    #ENCRYPT AND DASH FRAGMENTED FILE (MARLIN DRM)
    c2 = 'python3 /home/roger/Bento4/Source/Python/utils/mp4-dash.py ' \
         '--marlin --encryption-key=121a0fca0f1b475b8910297fa8e0a07e:a0a1a2a3a4a5a6a7a8a9aaabacadaeaf ' \
         'BBB-fragmented.mp4'

    os.system(c1)
    os.system(c2)

def livestream():

    c = 'ffmpeg -i BBB.mp4 -v 0 -vcodec libx264 -f mpegts udp://127.0.0.1:23000'
    os.system(c)
    #Type 'ffplay udp://127.0.0.1:23000' in a terminal to watch the live stream


print('-------------------  P3 - VIDEO STREAMING    -------------------\n\n'
      '1. Create an HLS transport stream container with bbb.\n'
      '2. Create a MPD video file. Fragment, encrypt and dash the file. \n'
      '3. Livestream with ffmpeg. \n\n')

i = int(input('Select the exercise (1/2/3):'))

if i==1:
    HLS()
if i==2:
    MPD()
if i==3:
    print('Type "ffplay udp://127.0.0.1:23000" in a terminal to watch the live stream')
    print('Stream ending')
    livestream()



