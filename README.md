# 🐶 dogf

dogf is a super simple static site generator, simple as in you'll only need two
commands.

live demo: [dogf](https://blog-943yc.ondigitalocean.app/)

## installation

Luckily for you, there's a setup file in the repo, so you can just download
that and run it, something like this:
```
wget https://raw.githubusercontent.com/bsantanad/dogf/master/setup
chmod +x setup
./setup
```

If you don't trust the setup file, just go read it, it's super short, and not
invasive.

## usage

### new blog

```
dogf new <blog-name> 
```
This will create a directory with the `blog-name` you wrote, the directory will
look something like this:
```
.
├── config.yml
└── posts
    └── example.md
```
As you can see it only creates two things, one is the config file, where you
can set blog name, colours, author, and so on. The other one is a posts
directory with an example on how a post looks.

Take a look at the header of the `example.md` file, the posts you write need
to have that header, changing it accordingly to the post at hand. The rest of
the example is just a simple markdown file.

### build blog 

You have finished writing your posts, or you just added a new one. It's time
to build the actual site.

Inside the blog directory, just run:
```
dogf build
```
If nothing shows up, everything went well.

You'll see that a new directory popped up `site`. Here are the HTML files and
so on.

If you want to test it, go inside the `site` directory and open index.html with
a web browser. Or even better, you could do:

```
python -m http.server
```

And it will start serve the site, so you can check it in other devices in your
local network.

## acknowledgements

The look and feel from the site has heavily inspired on
[unixsheikh.com](https://unixsheikh.com).

## why? 

Why making yet another static site generator, and a crappier one than say
[hugo](gohugo.io) or [gatsby](https://www.gatsbyjs.com/)? Well I wrote a post
about it in my dogf blog ;) [#FIXME](bsantanad.com), so go ahead and read it.
