# ComicShelf

ComicShelf creates a visual library of your digital comic files. Each file is uploaded into ComicShelf in a compressed format. The app processes the name of the file and extract information like the comic's title, issue number and release year. 
This information and more is saved onto a database, and the archive is then uncompressed. ComicShelf then shows the user a thumbnail of each comic they have uploaded. Comics can be sorted by name or publisher, making them easy to find. ComicShelf enhaces your comic reading experience, allowing you to read in the browser

![ComicShelf](https://33.media.tumblr.com/d7fc59ae71111e19b917539b5bb704d4/tumblr_nu10xtm0ap1u6majmo1_1280.gif)
[![ComicShelf Video](http://img.youtube.com/vi/8uFe3LLzVRk/0.jpg)](https://youtu.be/8uFe3LLzVRk)




### Why I chose this project

The idea for this project has been around in my head for quite a while, but only after attending Hackbright Academy did I have the necessary skills to bright make it real. 
I love reading comic books. I love staring at the beautiful art that my favorite artists create. Artists like Jim Lee and Joe Madureira. My digital comic library is extensive, which made it difficult to remember where I left off reading. I'm a very visual person, for me a visual cue will help me remember what book I was reading a lot faster. As an artist, I often draw inspiration from the amazing art in these books. Staring at pretty pictures is clearly also a hobby of mine!.


### Thoughts && Challenges
For this project I chose to apply and learn more about other technologies such as PostgreSQL, REGEX, using the rarFile module for Python. As well as the os module. 
At first I assumed learning and using regular expressions would be my biggest challenge. It turned out to be the one I had most fun with, and not as bad as I thought. Figuring out how to uncompress rarfiles turned out to be the biggest challenge. Along the way I even learned a bit about bash scripting, which I hope to use some time soon. 
The best part about this project was being able to work alone in my own space, and yet still have someone to pair program with to fix an error that I couldn't fix by myself. 


### Version
1.0

### Tech

* [Python] - highly readable scripting language!
* [Flask] - a lightweight Python web framework
* [PostgreSQL] - open source SQL database
* [JQuery] - naturally!
* [Javascript] - a high level programming language
* [Jinja] - templating language
* [HTML] - structuring the web since 1993!
* [CSS] - styling all the things for 18 years.
* [rarfile] - Python RAR archive reading module by [Marko Kreen]
* [MixitUp JQuery plugin] - jQuery plugging for animated filtering and sorting by [KunkaLabs]
* [REGEX ] - regular expressions
* [Sublime Editor] - cross-platform text editor
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [Wikipedia API] - used to get publisher info

## How it works

**REGEX**

ComicShelf uses REGEX (regular expressions), to pull out information from the file's name. 
The format of the file's name is usually as follow:

> (Comic name)      -  (Issue #)-(Year)

> Red Hood and the Outlaws 02 (2011)

The file name may have other information in it, but it is of no use to the app, thus it is ignored. This information is then stored in a dictionary, and later on passed on to the database. This process on takes place when the user uploads a file with the .cbr, .cbz, or .cbt extensions. Anything else is ignored by the function. 
> Refer to [extract_comics.py]


**Unpacking comic books!**

The digital comics books most often come in a few popular formats. 
* .cbr (rarfile)
* .cbz (zipfile)
* .cbt (tarfile)

As you can see these merely common compression formats. The [cb] merely stands for comic book. The challenge in this instance was handling the ever so popular.cbr format. Python already comes with a library for unpacking a zipfile. It does not come with one for rarfiles. I found a RAR archive reader for Python which then made it possible for my app to handle .cbr files. 
Inside these archives there are all the images that make up the comic book. Which will be used to show a thumbnail of the cover page, and to read the whole book. 


**Upload**

ComicShelf can handle multiple file uploads. The user simply needs to select all the archives they wish to upload into their library. In the upload menu they should also select the name of the publisher, and a genre that best fits the book. Its important to pick the right publisher, because this will be used later for appropriate sorting within the app. 
Once the user selects their comics, the app will process them and extract information such as the comic's name, issue and year. It will also find the first image in each comic, and keep the path to that image. A path to the rest of the images is also kept. These paths are used to show the user thumbnail images of their books, and to allow them to read the comic when they wish. 
All of this is then stored in a database. 


**Database**

ComicShelf uses a database called PostgreSQL. It is open source and quite advanced. 
The database stores informatin about the user, the comics they have uploaded, the publishers and genres associated with the book. 
The database is made to allow more features to be added to the app, such as bookmarks and comments without changing the model. 
Queries are run in the app's routes to retrieve info from the database. These can retrieve the publishers, books, user information and more. 
When the user wants to read a comic, an AJAX call retrieves the selected comic book and brings up in the viewer. 



**Frontend**

ComicShelf makes extensive use of the jQuery plugin, MitItUp by Kunkalabs.
With Mixitup, the app creates a visual library of all the comics. It also allows the comic to be filtered by name and publisher, as well as sorting in ascending or descending order. This way the user can see only the arc they want to read, or see all the books they have for a certain publisher. 
MixItUp uses data attributes in HTML to do the sorting and filtering. These data attributes are simply the name and publisher of the comic, in lowercase and without spaces. These alternate info is stored in the database and accessed to make the library of comics. 
Every time a user uploads a comic, these change to reflect the changes made. 

The comic viewer in ComicShelf makes use of the Bootstrap modal and carousel. Clicking on a comic triggers an AJAX call to bring up the appropriate comic book. The viewer consists of a carousel that lives inside a modal window. 
The carousel is then populated with the images dynamically. This allows the user to read a different comic book each time. 

The upload menu is hidden at all times. It is revealed by the use of jQuery after a click event on the upload button, on the right hand side. 



### Version 2.0

 - Write Tests
 - Add magnify on modal viewer
 - Improve comic viewer on modal
 - Integrate facebook, twitter api [login, post]
 - Implement shared reading session with friends
 - Add bookmarks. 
 - Comments
 - Database search
 - Remove/Edit comic
 - Star Rating 
 - Save/ Search user tags
 - Add Artist/Author information
 - Better profile page
 - Faster Upload/ comic book processing
 
 


License
----

MIT


**Free Software, Hell Yeah!**

- [MixItUp](https://mixitup.kunkalabs.com/)
- [ElevateZoom](http://www.elevateweb.co.uk/image-zoom)
- [rarFile](http://rarfile.readthedocs.org/en/latest/#)
