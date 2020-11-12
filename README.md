

![](https://image.flaticon.com/icons/png/128/889/889105.png)
# Image Crawling from Flickrs

Flickr - almost certainly the best online photo management and sharing application in the world. You can find any photos you want. Most of them can be used as a dataset. 
(Note:Flickr has API which is called flickrapi. It can be installed with python)

### Step 1
Install flickrapi on python
```bash
pip install flickrapi
```
### Step 2
Get Your personal API Key and Secret from [here](https://www.flickr.com/services/apps/create/)
> After you finish all the tasks you can proceed to scrapping the image data

**flickr_GetUrls.py** fetches all image links from flickr website. Run python file from terminal with search tag and maximum number of images you want. For example:
```bash
python flickr_GetUrls.py orange 100
```
After all links are fetched it will save the image links to csv file with tag name

**image_download.py** creates folder with tag name and downloads all images through links save in csv file. Run python file from terminal:
```bash
python image_download.py orange.csv
```

> Note: The image file name you download will be used from its links. In case you want to rename image data files in order to sort you use rename_files.py

Run **rename_files.py**:
```bash
python renam_files.py <folder_name>
```
It will modify file names to numbers starting from 1(1.jpg, 2.jpg, 3.jpg...)

### References
You can find documentation file [here](https://www.flickr.com/services/api)
