import flickrapi
import xml

key = u'a4b698792ceedf048aa579118b4d7ef5'
secret = u'c8f60618dab0ed74'
username = '144402257@N07'
flickr = flickrapi.FlickrAPI(key,secret, token_cache_location='tests/')


def upload_img(img_path):
    flickr.authenticate_via_browser(perms='write')
    id = flickr.upload(img_path, is_public='0')[0].text
    photo = flickr.photos.getSizes(photo_id=id)
    the_url = photo[0][-1].get('source')
    return id , the_url

def delete_img(img_id):
    flickr.authenticate_via_browser(perms='delete')
    flickr.photos.delete(photo_id=img_id)

def replace_img(img_path,img_id):
    flickr.authenticate_via_browser(perms='write')
    flickr.replace(filename=img_path,photo_id=img_id)
    photo = flickr.photos.getSizes(photo_id=img_id)
    the_url = photo[0][-1].get('source')
    return img_id , the_url