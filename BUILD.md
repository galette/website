# Build Galette website

Galette website uses [Jekyll](https://jekyllrb.com) and several plugins.

To install all required dependencies, you must have a working jekyll installed on your workstation.
From the cloned directory, just run:

```
$ bundle install
```

Then you can run on internal server:

```
$ bundle exec jekyll serve
```

## SEO issue

Plugins [translation](https://github.com/kurtsson/jekyll-multiple-languages-plugin/)
and [SEO](https://github.com/jekyll/jekyll-seo-tag/) one are not really compatible; this leads i18n
keys to be displayed instead of their content:

```
<!-- What we get -->
<title>pages.home</title>
<!-- What we expect -->
<title>Home</title>
```

There is a parameter that take care of the `title` element from the SEO
plugin, so it can be handled outside plugin. but this is not enough, there
is more than just the title.
In order to get correct headers, I've hacked the default template from
the plugin (stored in _layouts/seo.html).

Just replace plugin template with this file:

```
$ cp _layouts/seo.html vendor/ruby/2.6.0/gems/jekyll-seo-tag-2.6.1/lib/template.html
```

The provided `seo-tag-galette-fix.patch` shows what is modified. First parts has been
proposed upstream (pr 393)
