# ytdl_split

[YouTube-dl](https://github.com/ytdl-org/youtube-dl) is a Python code to obtain YouTube data.
However, it stores collected metadata in the file names.

**ytdl_split** obtains the metadata for the files, collected with the help of youtube-dl code.

It also formats the year corresponding the following format type “dd-mm-yy”. The data is encoded as UTF-8 CSV file. 


# Requirements
1. os Python package
2. csv Python package

Videos from YouTube may be collected with the help of youtube-dl, using the following code line:

```youtube-dl -o '%(channel)s-ghj-%(title)s-ghj-%(upload_date)s-ghj-%(duration)s-ghj-%(view_count)s-ghj-%(like_count)s' ACCOUNT```

# How to use
1. Add a path to the folder with the videos (row 5).
2. Change the desired CSV file name (row 23).
3. Run

``` py ytdl_split.py```

# Converted metadata
* Channel's name
* Video's title
* Upload date
* Video's duration
* Views
* Likes
