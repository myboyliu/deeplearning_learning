import pycurl
from io import StringIO
from io import BytesIO
b = BytesIO();
def write(bytes):
    print(bytes)

c = pycurl.Curl()
c.setopt(c.HEADERFUNCTION, b.write)
c.setopt(c.POST, 1)
c.setopt(c.URL, "http://127.0.0.1:8888/file")
c.setopt(c.HTTPPOST, [("file", (c.FORM_FILE, "/Users/william/Desktop/1.jpeg"))])
c.perform()
print(b.getvalue().decode('utf-8'))
b.close()
c.close()
print( "that's it")



