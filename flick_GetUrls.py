from flickrapi import FlickrAPI
import pandas as pd
import sys

key=''
secret=''
#https://www.flickr.com/services/api/ API documentation
def get_urls(image_tag,MAX_COUNT):
    
    if type(image_tag) == list:
        image_tag = '_'.join(image_tag) #if the search tag has more than 1 word, we concatenate it

    flickr = FlickrAPI(key, secret)
    photos = flickr.walk(text=image_tag,
                            tag_mode='all',
                            tags=image_tag,
                            extras='url_o', #extra types(Note: change it to "url_o" to get the original image)
                            per_page=50,    #url_sq, url_t, url_s, url_q, url_m, url_n, url_z, url_c, url_l, url_o (from smallest to original)
                            sort='relevance')
    count=0
    urls=[]
    for photo in photos:
        if count< MAX_COUNT:
            count=count+1
            print("Fetching url for image number {}".format(count))
            try:
                url=photo.get('url_o')
                urls.append(url)
            except:
                print("Url for image number {} could not be fetched".format(count))
        else:
            print("Done fetching urls, fetched {} urls out of {}".format(len(urls),MAX_COUNT))
            break
    urls=pd.Series(urls)
    print("Writing out the urls in the current directory")

    urls.to_csv(image_tag+"_urls.csv")
    print("Done!!!")

def main():
    tag=sys.argv[1:-1] #receive tag name from terminal(Take 2nd to before last inputs)
    MAX_COUNT=int(sys.argv[-1]) #receive count number(Last input)
    get_urls(tag,MAX_COUNT) 
if __name__=='__main__':
    main()